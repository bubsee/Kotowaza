import objects
def show_everything_under_sprite(screen):
    for item in object_records:
        if item[2] == 0:
            screen.blit(item[0], item[1])

def show_everything_over_sprite(screen):
    for item in object_records:
        if item[2] == 1:
            screen.blit(item[0], item[1])

object_records = [
    #in front
    [objects.gate, (72, 280), 1], # gate
    [objects.bottom_bridge_railing, (260, 391), 1],
    [objects.side_hedge, (985, 195), 1],
    [objects.side_hedge, (1101, 195),1 ],
    [objects.side_hedge, (1141, 195), 1],
    [objects.side_hedge, (1181, 195), 1],
    [objects.side_hedge, (945, 195), 1],

    #behind
# ---------------BUILDINGS------------------
    [objects.big_house, (750, 435), 0],
    [objects.main_palace, (474, 0), 0],
    [objects.food_shop, (328, 530), 0],
    [objects.shop, (418, 531), 0],
    [objects.tall_palace, (46, 0), 0],
    [objects.tall_building, (864, 120), 0],
    [objects.wide_house, (1040, 62), 0],
    [objects.tall_house, (960, 43), 0],
    [objects.regular_house, (1150, 63), 0],
    [objects.dojo, (1100, 375), 0],

    # ----------------DETAILS-------------------
    [objects.lake_tile, (275, 400), 0],
    [objects.lake_tile, (300, 400), 0],
    [objects.lake_tile, (315, 400), 0],
    [objects.sakura, (775, 90), 0],  # right side sakura
    [objects.sakura, (775, 140), 0],
    [objects.sakura, (775, 190), 0],
    [objects.sakura, (775, 240), 0],
    [objects.sakura, (432, 90), 0],  # left side sakura
    [objects.sakura, (432, 140), 0],
    [objects.sakura, (432, 190), 0],
    [objects.sakura, (432, 240), 0],
    #[objects.pond, (591, 360), 0],  # pond
    [objects.tree, (854, 245), 0],  # left side trees
    [objects.tree, (854, 275), 0],
    [objects.tree, (854, 305), 0],
    [objects.tree, (854, 335), 0],
    [objects.tree, (924, 245), 0],  # right side trees
    [objects.tree, (924, 275), 0],
    [objects.tree, (924, 305), 0],
    [objects.tree, (924, 335), 0],
    [objects.fish_box, (265, 575), 0],  # fix box
    # LAKE EDGES
    [objects.lake_right_edge, (374, 310), 0],  # top lake
    [objects.lake_right_edge, (374, 275), 0],
    [objects.lake_left_edge, (250, 310), 0],
    [objects.lake_left_edge, (250, 275), 0],
    [objects.lake_top_edge, (250, 275), 0],
    [objects.lake_top_edge, (290, 275), 0],
    [objects.lake_top_edge, (330, 275), 0],
    [objects.lake_top_edge, (337, 275), 0],
    [objects.lake_right_edge, (374, 485), 0],  # bottom lake
    [objects.lake_right_edge, (374, 450), 0],
    [objects.lake_left_edge, (250, 485), 0],
    [objects.lake_left_edge, (250, 450), 0],
    [objects.lake_bottom_edge, (250, 525), 0],
    [objects.lake_bottom_edge, (290, 525), 0],
    [objects.lake_bottom_edge, (330, 525), 0],
    [objects.lake_bottom_edge, (337, 525), 0],
    [objects.lake_short_bottom_edge, (250, 350), 0],  # middle section
    [objects.lake_short_bottom_edge, (350, 350), 0],
    [objects.lake_short_top_edge, (250, 450), 0],
    [objects.lake_short_top_edge, (350, 450), 0],
    [objects.lake_left_edge, (275, 350), 0],
    [objects.lake_left_edge, (275, 390), 0],
    [objects.lake_left_edge, (275, 413), 0],
    [objects.lake_right_edge, (350, 350), 0],
    [objects.lake_right_edge, (350, 390), 0],
    [objects.lake_right_edge, (350, 413), 0],
    # END OF LAKE EDGES
    [objects.bridge_floor, (260, 370), 0],  # bridge
    [objects.bridge_floor, (293, 370), 0],
    [objects.bridge_floor, (326, 370), 0],
    [objects.top_bridge_railing, (260, 345), 0],
    [objects.single_hedge, (945, 145), 0],  # hedges
    [objects.single_hedge, (1220, 195), 0],
    [objects.up_hedge, (1002, 212), 0],
    [objects.up_hedge, (1002, 247), 0],
    [objects.up_hedge, (1002, 282), 0],
    [objects.up_hedge, (1002, 317), 0],
    [objects.up_hedge, (1100, 212), 0],
    [objects.up_hedge, (1100, 247), 0],
    [objects.up_hedge, (1100, 282), 0],
    [objects.up_hedge, (1100, 317), 0],
    [objects.up_hedge, (1220, 160), 0],
    [objects.up_hedge, (945, 160), 0],
    [objects.single_hedge, (1220, 195), 0],
    [objects.single_hedge, (1002, 352), 0],
    [objects.single_hedge, (1100, 352), 0],
    [objects.single_hedge, (550, 325), 0],  # central single hedges
    [objects.single_hedge, (575, 300), 0],
    [objects.single_hedge, (525, 350), 0],
    [objects.single_hedge, (677, 325), 0],
    [objects.single_hedge, (652, 300), 0],
    [objects.single_hedge, (702, 350), 0],
    [objects.single_hedge, (677, 450), 0],
    [objects.single_hedge, (652, 475), 0],
    [objects.single_hedge, (702, 427), 0],
    [objects.single_hedge, (550, 450), 0],
    [objects.single_hedge, (575, 475), 0],
    [objects.single_hedge, (525, 425), 0],
    [objects.big_tree, (500, 505), 0],  # big trees
    [objects.big_tree, (645, 530), 0],
    # [objects.big_tree, (949, 530), 0], #-
    [objects.big_tree, (1132, 250), 0],
    [objects.big_tree, (263, 150), 0],
    # [objects.big_tree, (400,430), 0], #-
    [objects.left_flag, (80, 200), 0],
    [objects.right_flag, (174, 200), 0],
    [objects.statue, (804, 590), 0],
    [objects.statue, (875, 590), 0],
]