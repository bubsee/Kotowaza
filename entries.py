building_entries = {
    'my house': (838,567),
    'main palace': (610,264),
    'food shop': (337,576),
    'shop': (469,573),
    'tall palace': (124,204),
    'bell tower': (886,243),
    'dojo': (1162,444)}

def check_entry(player_x, player_y):
    for building in building_entries:
        if abs(player_x - building_entries[building][0]) < 10 and abs(player_y - building_entries[building][1]) < 10:
            return building
    return False