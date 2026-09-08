def get_room_rate(room_code):
    if room_code == "1PR":
        cost = 115.11
    elif room_code == "SFR":
        cost = 235.23
    elif room_code == "LFR":
        cost = 340.34
    return cost


def get_room_cost(num_rooms, room_code):
    cost_per_room = get_room_rate(room_code=room_code)
    total_cost = num_rooms * cost_per_room
    return total_cost


def main():
    s, sf, lf = input().split(" ")
    s = int(s)
    sf = int(sf)
    lf = int(lf)

    s_cost = get_room_cost(s, room_code="1PR")
    sf_cost = get_room_cost(sf, room_code="SFR")
    lf_cost = get_room_cost(lf, room_code="LFR")

    room_required = s + sf + lf
    total_cost = (s_cost + sf_cost + lf_cost) * 2
    total_cost = round(total_cost, 2)
    print(f"Rooms required: {room_required}", f"All rooms will cost: ${total_cost}", sep="\n")

main()