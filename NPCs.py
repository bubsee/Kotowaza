import pygame
import map
import sprites
import random
import entries
import hitboxes

villager_speed = 3


def nearest_path_tile(px, py):
    col, row = (px + 12) // 25, (py + 12) // 25
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
                addition = came_from[inspect][0] * 25 +13, came_from[inspect][1] * 25 +13
                path.append(addition)
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
            tile_rect = pygame.Rect(tile[0] * 25 + 1, tile[1] * 25 + 1, 23, 23)
            if any(tile_rect.colliderect(wall) for wall in hitboxes.walls):
                continue
            came_from[tile] = inspect
            queue.append(tile)

    return None



class Villager:
    def __init__(self, start_building: str):
        self.start_building = start_building
        self.x, self.y = entries.building_entries[start_building]     #fetch the coordinates of th start buidings door
        self.end_point = random.choice(stop_spots)    #choose random stop spot

        #print(map.grid[self.y // 25][self.x // 25])  #debugging start position
        self.route = BFS((self.x, self.y), self.end_point[0])    #find the applicable path
        self.arrived = False
        self.at_home = True

    def walk_to_destination(self, screen, current_image):
        if self.route != []:
            target = self.route[-1]
            relative_positon = target[0] - self.x, target[1] - self.y

            # snap to node on path when close enough (may look weird)
            if self.x > target[0] - villager_speed and self.x < target[0] + villager_speed and self.y > target[1] - villager_speed and self.y < target[1] + villager_speed:
                self.x = target[0]
                self.y = target[1]
                self.route.remove(self.route[-1])

            # adjust x coord
            elif relative_positon[0] > 0:
                self.x += villager_speed
            elif relative_positon[0] < 0:
                self.x -= villager_speed

            # adjust y coord
            if relative_positon[1] > 0:
                self.y += villager_speed
            elif relative_positon[1] < 0:
                self.y -= villager_speed

        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 10, 10))
        #screen.blit(screen, current_image,(self.x, self.y))
        if self.route == []:
            self.arrived = False

    def reset_route(self, screen):
        self.end_point = entries.building_entries[self.start_building][0] + 25, entries.building_entries[self.start_building][1] + 50
        self.route = BFS((self.x, self.y), self.end_point)
        print(self.x, self.y, self.end_point)
        pygame.draw.circle(screen, (0,0,255), (self.x, self.y), 10)
        pygame.draw.circle(screen, (0,0,255), (self.end_point[0],self.end_point[1]), 10)


    def show_path(self):      # for debugging
        print(f'route: {self.start_building} -> {self.end_point[2]}')
        print(self.route)


stop_spots = [  #format: [coords, direction]
    [(286,345),'up', 'bridge'],# on the bridge
    [(103,309),'down', 'gate'],# under the gate
    #[(568,369),'right', 'pond'],# by the pond
    #[(877,252),'down', 'bell tower'],# by the bell tower
    #[(271,573),'up', 'fish box'],# by the fish box
    #[(364,582),'down', 'fish shop'],# by the fish shop
    #[(433,594),'up', 'main shop'],# by the main shop
    #[(1123,444),'down', 'dojo'],# by the dojo
    [(625,576),'right', 'tree']# by the tree
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
