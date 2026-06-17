building_entries = {
    'my house': (838,567),
    'main palace': (610,264),
    'food shop': (337,576),
    'shop': (469,573),
    'tall palace': (124,204),
    'bell tower': (885,265),
    'dojo': (1162,455),
    'tall house': (980,140),
    'big house': (1078,138)}

def check_entry(player_x, player_y):
    for building in building_entries:
        if abs(player_x - building_entries[building][0]) < 10 and abs(player_y - building_entries[building][1]) < 10:
            return building
    return False