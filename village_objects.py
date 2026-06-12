import objects
def show_everything_under_sprite(screen):
    screen.blit(objects.gate, (72, 280))  # gate
    screen.blit(objects.bottom_bridge_railing, (260, 391))
    screen.blit(objects.side_hedge, (985, 195))
    screen.blit(objects.side_hedge, (1101, 195))
    screen.blit(objects.side_hedge, (1141, 195))
    screen.blit(objects.side_hedge, (1181, 195))
    screen.blit(objects.side_hedge, (945, 195))

def show_everything_over_sprite(screen):
    # ---------------BUILDINGS------------------
    screen.blit(objects.big_house, (750, 435))
    screen.blit(objects.main_palace, (474, 0))
    screen.blit(objects.food_shop, (328, 530))
    screen.blit(objects.shop, (418, 531))
    screen.blit(objects.tall_palace, (46, 0))
    screen.blit(objects.tall_building, (864, 120))
    screen.blit(objects.wide_house, (1040, 62))
    screen.blit(objects.tall_house, (960, 43))
    screen.blit(objects.regular_house, (1150, 63))
    screen.blit(objects.dojo, (1100, 375))

    # ----------------DETAILS-------------------
    screen.blit(objects.lake_tile, (275, 400))
    screen.blit(objects.lake_tile, (300, 400))
    screen.blit(objects.lake_tile, (315, 400))
    screen.blit(objects.sakura, (775, 90))  # right side sakura
    screen.blit(objects.sakura, (775, 140))
    screen.blit(objects.sakura, (775, 190))
    screen.blit(objects.sakura, (775, 240))
    screen.blit(objects.sakura, (432, 90))  # left side sakura
    screen.blit(objects.sakura, (432, 140))
    screen.blit(objects.sakura, (432, 190))
    screen.blit(objects.sakura, (432, 240))
    screen.blit(objects.pond, (591, 360))  # pond
    screen.blit(objects.tree, (854, 245))  # left side trees
    screen.blit(objects.tree, (854, 275))
    screen.blit(objects.tree, (854, 305))
    screen.blit(objects.tree, (854, 335))
    screen.blit(objects.tree, (924, 245))  # right side trees
    screen.blit(objects.tree, (924, 275))
    screen.blit(objects.tree, (924, 305))
    screen.blit(objects.tree, (924, 335))
    screen.blit(objects.fish_box, (265, 575))  # fix box
    # LAKE EDGES
    screen.blit(objects.lake_right_edge, (374, 310))  # top lake
    screen.blit(objects.lake_right_edge, (374, 275))
    screen.blit(objects.lake_left_edge, (250, 310))
    screen.blit(objects.lake_left_edge, (250, 275))
    screen.blit(objects.lake_top_edge, (250, 275))
    screen.blit(objects.lake_top_edge, (290, 275))
    screen.blit(objects.lake_top_edge, (330, 275))
    screen.blit(objects.lake_top_edge, (337, 275))
    screen.blit(objects.lake_right_edge, (374, 485))  # bottom lake
    screen.blit(objects.lake_right_edge, (374, 450))
    screen.blit(objects.lake_left_edge, (250, 485))
    screen.blit(objects.lake_left_edge, (250, 450))
    screen.blit(objects.lake_bottom_edge, (250, 525))
    screen.blit(objects.lake_bottom_edge, (290, 525))
    screen.blit(objects.lake_bottom_edge, (330, 525))
    screen.blit(objects.lake_bottom_edge, (337, 525))
    screen.blit(objects.lake_short_bottom_edge, (250, 350))  # middle section
    screen.blit(objects.lake_short_bottom_edge, (350, 350))
    screen.blit(objects.lake_short_top_edge, (250, 450))
    screen.blit(objects.lake_short_top_edge, (350, 450))
    screen.blit(objects.lake_left_edge, (275, 350))
    screen.blit(objects.lake_left_edge, (275, 390))
    screen.blit(objects.lake_left_edge, (275, 413))
    screen.blit(objects.lake_right_edge, (350, 350))
    screen.blit(objects.lake_right_edge, (350, 390))
    screen.blit(objects.lake_right_edge, (350, 413))
    # END OF LAKE EDGES
    screen.blit(objects.bridge_floor, (260, 370))  # bridge
    screen.blit(objects.bridge_floor, (293, 370))
    screen.blit(objects.bridge_floor, (326, 370))
    screen.blit(objects.top_bridge_railing, (260, 345))
    screen.blit(objects.single_hedge, (945, 145))  # hedges
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.up_hedge, (1002, 212))
    screen.blit(objects.up_hedge, (1002, 247))
    screen.blit(objects.up_hedge, (1002, 282))
    screen.blit(objects.up_hedge, (1002, 317))
    screen.blit(objects.up_hedge, (1100, 212))
    screen.blit(objects.up_hedge, (1100, 247))
    screen.blit(objects.up_hedge, (1100, 282))
    screen.blit(objects.up_hedge, (1100, 317))
    screen.blit(objects.up_hedge, (1220, 160))
    screen.blit(objects.up_hedge, (945, 160))
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.single_hedge, (1002, 352))
    screen.blit(objects.single_hedge, (1100, 352))
    screen.blit(objects.single_hedge, (550, 325))  # central single hedges
    screen.blit(objects.single_hedge, (575, 300))
    screen.blit(objects.single_hedge, (525, 350))
    screen.blit(objects.single_hedge, (677, 325))
    screen.blit(objects.single_hedge, (652, 300))
    screen.blit(objects.single_hedge, (702, 350))
    screen.blit(objects.single_hedge, (677, 450))
    screen.blit(objects.single_hedge, (652, 475))
    screen.blit(objects.single_hedge, (702, 427))
    screen.blit(objects.single_hedge, (550, 450))
    screen.blit(objects.single_hedge, (575, 475))
    screen.blit(objects.single_hedge, (525, 425))
    screen.blit(objects.big_tree, (500, 505))  # big trees
    screen.blit(objects.big_tree, (645, 530))
    # screen.blit(objects.big_tree, (949, 530)) #-
    screen.blit(objects.big_tree, (1132, 250))
    screen.blit(objects.big_tree, (263, 150))
    # screen.blit(objects.big_tree, (400,430)) #-
    screen.blit(objects.left_flag, (80, 200))
    screen.blit(objects.right_flag, (174, 200))
    screen.blit(objects.statue, (804, 590))
    screen.blit(objects.statue, (875, 590))

object_coord = {
    #in front
    objects.gate : (72, 280) # gate
    objects.bottom_bridge_railing, (260, 391)
    objects.side_hedge, (985, 195)
    objects.side_hedge, (1101, 195)
    objects.side_hedge, (1141, 195)
    objects.side_hedge, (1181, 195)
    objects.side_hedge, (945, 195)

    #behind
# ---------------BUILDINGS------------------
    screen.blit(objects.big_house, (750, 435))
    screen.blit(objects.main_palace, (474, 0))
    screen.blit(objects.food_shop, (328, 530))
    screen.blit(objects.shop, (418, 531))
    screen.blit(objects.tall_palace, (46, 0))
    screen.blit(objects.tall_building, (864, 120))
    screen.blit(objects.wide_house, (1040, 62))
    screen.blit(objects.tall_house, (960, 43))
    screen.blit(objects.regular_house, (1150, 63))
    screen.blit(objects.dojo, (1100, 375))

    # ----------------DETAILS-------------------
    screen.blit(objects.lake_tile, (275, 400))
    screen.blit(objects.lake_tile, (300, 400))
    screen.blit(objects.lake_tile, (315, 400))
    screen.blit(objects.sakura, (775, 90))  # right side sakura
    screen.blit(objects.sakura, (775, 140))
    screen.blit(objects.sakura, (775, 190))
    screen.blit(objects.sakura, (775, 240))
    screen.blit(objects.sakura, (432, 90))  # left side sakura
    screen.blit(objects.sakura, (432, 140))
    screen.blit(objects.sakura, (432, 190))
    screen.blit(objects.sakura, (432, 240))
    screen.blit(objects.pond, (591, 360))  # pond
    screen.blit(objects.tree, (854, 245))  # left side trees
    screen.blit(objects.tree, (854, 275))
    screen.blit(objects.tree, (854, 305))
    screen.blit(objects.tree, (854, 335))
    screen.blit(objects.tree, (924, 245))  # right side trees
    screen.blit(objects.tree, (924, 275))
    screen.blit(objects.tree, (924, 305))
    screen.blit(objects.tree, (924, 335))
    screen.blit(objects.fish_box, (265, 575))  # fix box
    # LAKE EDGES
    screen.blit(objects.lake_right_edge, (374, 310))  # top lake
    screen.blit(objects.lake_right_edge, (374, 275))
    screen.blit(objects.lake_left_edge, (250, 310))
    screen.blit(objects.lake_left_edge, (250, 275))
    screen.blit(objects.lake_top_edge, (250, 275))
    screen.blit(objects.lake_top_edge, (290, 275))
    screen.blit(objects.lake_top_edge, (330, 275))
    screen.blit(objects.lake_top_edge, (337, 275))
    screen.blit(objects.lake_right_edge, (374, 485))  # bottom lake
    screen.blit(objects.lake_right_edge, (374, 450))
    screen.blit(objects.lake_left_edge, (250, 485))
    screen.blit(objects.lake_left_edge, (250, 450))
    screen.blit(objects.lake_bottom_edge, (250, 525))
    screen.blit(objects.lake_bottom_edge, (290, 525))
    screen.blit(objects.lake_bottom_edge, (330, 525))
    screen.blit(objects.lake_bottom_edge, (337, 525))
    screen.blit(objects.lake_short_bottom_edge, (250, 350))  # middle section
    screen.blit(objects.lake_short_bottom_edge, (350, 350))
    screen.blit(objects.lake_short_top_edge, (250, 450))
    screen.blit(objects.lake_short_top_edge, (350, 450))
    screen.blit(objects.lake_left_edge, (275, 350))
    screen.blit(objects.lake_left_edge, (275, 390))
    screen.blit(objects.lake_left_edge, (275, 413))
    screen.blit(objects.lake_right_edge, (350, 350))
    screen.blit(objects.lake_right_edge, (350, 390))
    screen.blit(objects.lake_right_edge, (350, 413))
    # END OF LAKE EDGES
    screen.blit(objects.bridge_floor, (260, 370))  # bridge
    screen.blit(objects.bridge_floor, (293, 370))
    screen.blit(objects.bridge_floor, (326, 370))
    screen.blit(objects.top_bridge_railing, (260, 345))
    screen.blit(objects.single_hedge, (945, 145))  # hedges
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.up_hedge, (1002, 212))
    screen.blit(objects.up_hedge, (1002, 247))
    screen.blit(objects.up_hedge, (1002, 282))
    screen.blit(objects.up_hedge, (1002, 317))
    screen.blit(objects.up_hedge, (1100, 212))
    screen.blit(objects.up_hedge, (1100, 247))
    screen.blit(objects.up_hedge, (1100, 282))
    screen.blit(objects.up_hedge, (1100, 317))
    screen.blit(objects.up_hedge, (1220, 160))
    screen.blit(objects.up_hedge, (945, 160))
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.single_hedge, (1002, 352))
    screen.blit(objects.single_hedge, (1100, 352))
    screen.blit(objects.single_hedge, (550, 325))  # central single hedges
    screen.blit(objects.single_hedge, (575, 300))
    screen.blit(objects.single_hedge, (525, 350))
    screen.blit(objects.single_hedge, (677, 325))
    screen.blit(objects.single_hedge, (652, 300))
    screen.blit(objects.single_hedge, (702, 350))
    screen.blit(objects.single_hedge, (677, 450))
    screen.blit(objects.single_hedge, (652, 475))
    screen.blit(objects.single_hedge, (702, 427))
    screen.blit(objects.single_hedge, (550, 450))
    screen.blit(objects.single_hedge, (575, 475))
    screen.blit(objects.single_hedge, (525, 425))
    screen.blit(objects.big_tree, (500, 505))  # big trees
    screen.blit(objects.big_tree, (645, 530))
    # screen.blit(objects.big_tree, (949, 530)) #-
    screen.blit(objects.big_tree, (1132, 250))
    screen.blit(objects.big_tree, (263, 150))
    # screen.blit(objects.big_tree, (400,430)) #-
    screen.blit(objects.left_flag, (80, 200))
    screen.blit(objects.right_flag, (174, 200))
    screen.blit(objects.statue, (804, 590))
    screen.blit(objects.statue, (875, 590))
}