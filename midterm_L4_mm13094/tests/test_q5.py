import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import potion_power_score


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q5_testcases = [
    # Visible Testcases (from Sample Interaction)
    ("ivy", 1, "a", 0, 70, 3,
     "Brewing Style: Overbrewed\nPotion Power Score: 54\nFailed Potion - back to the drawing board.", True),
    ("sage", 1, "mint", 1, 15, 40,
     "Brewing Style: Balanced\nPotion Power Score: 121\nCommon Potion - needs improvement.", True),
    ("sage", 2, "mint", 2, 25, 300,
     "Brewing Style: Balanced\nPotion Power Score: 328.0\nRare Potion - a strong contender.", True),
    ("wolfsbane", 3, "moonstone", 2, 20, 487,
     "Brewing Style: Balanced\nPotion Power Score: 1138.0\nLegendary Potion! Hogwarts takes the trophy!", True),

    # Hidden Testcases - ingredient_value (vowel/consonant accumulation, position offset)
    ("a", 1, "a", 0, 15, 1,
     "8e2c0bf269ba61d76e14416952de9a054113380d92981f9cc0b02e614cb3886a", False),
    ("b", 1, "a", 0, 15, 1,
     "8e2c0bf269ba61d76e14416952de9a054113380d92981f9cc0b02e614cb3886a", False),
    ("bcd", 1, "a", 0, 15, 1,
     "ac282efe418c6c0d85a7e48c0ae3ff430cde46b27b5372f5a83fc1b19061e345", False),
    ("aeiou", 1, "a", 0, 15, 1,
     "ba333982a7329eb19a371675443f855392610eaef912a3f80243988a8491fa68", False),

    # Hidden Testcases - ingredient_score (quantity bonus/prime boundaries)
    ("ab", 2, "a", 0, 15, 1,
     "7c788da6fe6bf4235866a53fa6185645587b56b44a290be012854e6b2040fbc1", False),
    ("ab", 5, "a", 0, 15, 1,
     "00d62b250169af8e0cada18ff448256cf029ac4de095d25352abc0473ca31d18", False),
    ("ab", 6, "a", 0, 15, 1,
     "4bedd94cd39bbeb6e231deb946fd3a83a57281ab745b750a22f9188a639d719c", False),
    ("ab", 7, "a", 0, 15, 1,
     "096e2fc8cea5424cd165d420822406a09fcee489e1fe8e3fae94ad0f80858d03", False),
    ("ab", 9, "a", 0, 15, 1,
     "c15b5a513b4da16e7109b1f6954688df7fd5893fe63aca68fd2666c04f8f8548", False),

    # Hidden Testcases - brewing_time_label / brewing_time_value boundaries
    ("ivy", 1, "a", 0, 9, 1,
     "1792e722975fd8191e42a80e9d453da3ef3f7a8e19e369e0aa991d8448e15bda", False),
    ("ivy", 1, "a", 0, 10, 1,
     "8406782c1a22c31421954762a19f6d3523ddcd0646586537573ed2c8f7069d34", False),
    ("ivy", 1, "a", 0, 30, 1,
     "8406782c1a22c31421954762a19f6d3523ddcd0646586537573ed2c8f7069d34", False),
    ("ivy", 1, "a", 0, 31, 1,
     "dc26ec6002252e49336fad9bdb32e9a0eee87bb23ae285e045ed605726d59cfc", False),
    ("ivy", 1, "a", 0, 60, 1,
     "dc26ec6002252e49336fad9bdb32e9a0eee87bb23ae285e045ed605726d59cfc", False),
    ("ivy", 1, "a", 0, 61, 1,
     "ba6b0ed069c6ef11fde8df0f9c9a7674e4a211deb271aa648b64dd173f3a6a4a", False),

    # Hidden Testcases - magical_energy_factor (digit accumulation, even/odd)
    ("ivy", 1, "a", 0, 15, 23,
     "166203d347c8a747f6436a34496c4d64a6b82fa4f74ac430e8f7d342c1a4bed3", False),
    ("ivy", 1, "a", 0, 15, 123,
     "bc3b5fab6a7632c28f601cd918d0119645643d16ccf9c0daff39dbb94264a5fa", False),
    ("ivy", 1, "a", 0, 15, 999999,
     "65b859779cb458f4d82c9a6e861f7e74c56d8ba01e2ba07c28b8f714e7eb17cb", False),

    # Hidden Testcases - classification boundaries (exactly at and just below each threshold)
    ("ab", 7, "rue", 6, 20, 1,
     "b619cd12ec47901ea92a71344e5e27f060dc7b42f1206387fd203cfbd5de5420", False),
    ("ab", 9, "oak", 10, 20, 1,
     "2fac91cba54ced4329997d400e20e2f7e75c6ea03f56c54894a0a6f82733e3e1", False),
    ("a", 1, "sage", 5, 20, 1,
     "1bc0d890ab2d7bc2a0711c51199993d69d53e02b20f83bbfe98824425c0153ab", False),
    ("a", 2, "rue", 4, 20, 1,
     "d988c78d942adebfd8f70d970f5e2042f6fdc0bdc266e8a5b675a32f4246f65e", False),
    ("a", 0, "ash", 2, 20, 1,
     "d8dc3592686cf5757ee3d3aa457a279f67685713491eb72037b24f327ed54c4b", False),
    ("a", 7, "ab", 10, 20, 1,
     "e6bf5c71f518e6b2348ffb5cc884606e973434ecd355a17e62e30803b6079b39", False),
]


@pytest.mark.parametrize(
    "name1, quantity1, name2, quantity2, brewing_time, energy, expected, visible",
    q5_testcases
)
def test_q5(name1, quantity1, name2, quantity2, brewing_time, energy, expected, visible, capsys):
    potion_power_score(name1, quantity1, name2, quantity2, brewing_time, energy)
    captured = capsys.readouterr().out.rstrip("\n")

    if visible:
        assert captured == expected
    else:
        assert hashcode(captured) == expected