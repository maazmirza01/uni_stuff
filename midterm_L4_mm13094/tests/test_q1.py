import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import pikachu_says


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q1_testcases = [
    # Visible Testcases (from Sample Interaction)
    (90, 50, 75, "Pika Pika!", True),
    (70, 90, 50, "Pika Chu!", True),
    (40, 50, 85, "Pika!", True),
    (90, 50, 60, "Pika...?", True),

    # Hidden Testcases - pikachu_status boundaries (49/50, 74/75)
    (49, 0, 100,
     "53838878ae7fbdfc1a0c049fb4c50482fcedb386978d3d482d4514dc0246da33", False),
    (50, 71, 0,
     "f4ca13a5a9422a674671315919dabcf4ab293eb5f8ded275cadcd8f06de0566e", False),
    (74, 71, 0,
     "f4ca13a5a9422a674671315919dabcf4ab293eb5f8ded275cadcd8f06de0566e", False),
    (75, 0, 71,
     "ef1020e0daeb368a924142e20fd9ad33a8a26ce022e101bed6acb33fa09b0379", False),

    # Hidden Testcases - Super charged + spark boundary (>70, not >=70)
    (90, 0, 70,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),
    (90, 0, 71,
     "ef1020e0daeb368a924142e20fd9ad33a8a26ce022e101bed6acb33fa09b0379", False),
    (100, 0, 100,
     "ef1020e0daeb368a924142e20fd9ad33a8a26ce022e101bed6acb33fa09b0379", False),
    (100, 100, 0,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # Super charged, spark too low -> default

    # Hidden Testcases - Energetic + mood boundary (>70, not >=70)
    (60, 70, 0,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),
    (60, 71, 0,
     "f4ca13a5a9422a674671315919dabcf4ab293eb5f8ded275cadcd8f06de0566e", False),
    (60, 100, 0,
     "f4ca13a5a9422a674671315919dabcf4ab293eb5f8ded275cadcd8f06de0566e", False),
    (60, 0, 100,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # Energetic, mood too low -> default

    # Hidden Testcases - Low energy OR boundary (spark>80 or mood>80, not >=80)
    (20, 80, 80,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # both exact 80 -> FAIL (default)
    (20, 0, 81,
     "53838878ae7fbdfc1a0c049fb4c50482fcedb386978d3d482d4514dc0246da33", False),  # spark just above -> PASS
    (20, 81, 0,
     "53838878ae7fbdfc1a0c049fb4c50482fcedb386978d3d482d4514dc0246da33", False),  # mood just above -> PASS
    (20, 81, 81,
     "53838878ae7fbdfc1a0c049fb4c50482fcedb386978d3d482d4514dc0246da33", False),  # both above -> PASS
    (0, 100, 100,
     "53838878ae7fbdfc1a0c049fb4c50482fcedb386978d3d482d4514dc0246da33", False),  # both max
    (0, 0, 0,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # both min -> FAIL (default)

    # Hidden Testcases - default fallback for each status independently
    (10, 50, 50,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # Low energy, neither condition met

    # Hidden Testcases - absolute extremes
    (100, 100, 100,
     "ef1020e0daeb368a924142e20fd9ad33a8a26ce022e101bed6acb33fa09b0379", False),  # all max -> Pika Pika!
    (0, 10, 10,
     "e4ec7dcaf0c64541b1dae42251473347d4816d8e5ea5f4ed43e5ba5bc9181063", False),  # energy=0 exact, default
    (100, 0, 100,
     "ef1020e0daeb368a924142e20fd9ad33a8a26ce022e101bed6acb33fa09b0379", False),  # energy=100 exact, Super charged
]


@pytest.mark.parametrize("energy, mood, spark, expected, visible", q1_testcases)
def test_q1(energy, mood, spark, expected, visible):
    if visible:
        assert pikachu_says(energy, mood, spark) == expected
    else:
        assert hashcode(pikachu_says(energy, mood, spark)) == expected