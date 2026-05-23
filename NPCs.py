import pygame
import map
import sprites
import random
import entries

def nearest_path_tile(px, py):
    col, row = px // 25, py // 25
    for dc, dr in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
        nc, nr = col+dc, row+dr
        if map.grid[nr][nc] == 1:
            return (nc, nr)

def BFS(start_coords: tuple, end_coords: tuple):

    # convert pixel coords to nearest path tile
    start = nearest_path_tile(*start_coords)
    end = nearest_path_tile(*end_coords)

    queue = [start]
    came_from = {start: None}  # visited tiles and where they came from

    while queue != []:
        inspect = queue.pop(0)  # take from the front

        if inspect == end:
            # trace back through came_from to build the path
            path = []
            while came_from[inspect] != None:
                path.append(came_from[inspect])
                inspect = came_from[inspect]
            return path

        local_tiles = [(inspect[0] + 1, inspect[1]),
                       (inspect[0] - 1, inspect[1]),
                       (inspect[0], inspect[1]+ 1),
                       (inspect[0], inspect[1] - 1)
                        ]
        for tile in local_tiles:
            if map.grid[tile[1]][tile[0]] != 1 or tile in came_from:
                continue
            came_from[tile] = inspect
            queue.append(tile)

    return None



class Villager:
    def __init__(self, start_building: str):
        self.x, self.y = entries.building_entries[start_building]     #fetch the coordinates of th start buidings door
        self.end_point = random.choice(stop_spots)    #choose random stop spot

        self.route = BFS((self.x, self.y), self.end_point[0])

    def walk_to_destination(self, screen):
        #screen.blit(screen, self,(self.x,self.y))
        ...

    def show_path(self, screen):      # for debugging
        print(self.end_point)
        print(self.route)


stop_spots = [  #format: [coords, direction]
    [(286,345),'up'],# on the bridge
    [(103,309),'down'],# under the gate
    [(568,369),'right'],# by the pond
    [(877,252),'down'],# by the bell tower
    [(271,573),'up'],# by the fish box
    [(364,582),'down'],# by the fish shop
    [(433,594),'up'],# by the main shop
    [(1123,444),'down'],# by the dojo
    [(625,576),'right']# by the tree
]

def show_positions(screen, frame):
    for item in stop_spots:
        if item[1] == 'up':
            current_image = sprites.up_idle[frame]
        elif item[1] == 'down':
            current_image = sprites.down_idle[frame]
        elif item[1] == 'left':
            current_image = sprites.left_idle[frame]
        elif item[1] == 'right':
            current_image = sprites.right_idle[frame]
            
        screen.blit(current_image, (item[0][0], item[0][1]))


#villager instantiations
Arthur = Villager('bell tower')
