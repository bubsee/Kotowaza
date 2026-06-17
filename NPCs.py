import pygame
import map
import sprites
import random
import entries
import hitboxes

villager_speed = 1
villagers = []

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
        self.x, self.y = entries.building_entries[start_building]     #fetch the coordinates of the start buiding's door
        self.end_point = random.choice(stop_spots)    #choose random stop spot

        #print(map.grid[self.y // 25][self.x // 25])  #debugging start position
        self.at_home = True
        self.arrived = False
        self.is_tapping_foot = False
        self.wait_timer = None
        self.wait_length = 200

        self.find_route()

        villagers.append(self)

    def find_route(self):
        if self.arrived:
            x = self.end_point
            self.end_point = random.choice(stop_spots)
            stop_spots.append(x)
        else:
            self.end_point = random.choice(stop_spots)
        stop_spots.remove(self.end_point)

        self.route = BFS((self.x, self.y), self.end_point[0])  # find the applicable path
        self.arrived = False

    def walk_to_destination(self, screen, current_image):
        if self.is_tapping_foot:
          self.wait_timer += 1
          if self.wait_timer > self.wait_length:
              self.wait_timer = None
              self.is_tapping_foot = False

        elif self.route != []:
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
            self.arrived = True
            self.wait_timer = 0
            self.is_tapping_foot = True

    def show_path(self):      # for debugging
        print(f'route: {self.start_building} -> {self.end_point[2]}')
        print(self.route)


stop_spots = [  #format: [coords, direction]
    [(286,345),'up', 'bridge'],# on the bridge
    [(103,309),'down', 'gate'],# under the gate
    [(560,369),'right', 'pond'],# by the pond
    [(885,300),'down', 'bell tower'],# by the bell tower
    #[(283,594),'up', 'fish box'],# by the fish box
    #[(364,582),'down', 'fish shop'],# by the fish shop
    #[(481,591),'up', 'main shop'],# by the main shop
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

def update(screen, current_image):
    for character in villagers:
        if character.route == []:
            character.find_route()
        else:
            character.walk_to_destination(screen, current_image)


#villager instantiations
Arthur = Villager('bell tower')
Dean = Villager('dojo')
James = Villager('tall palace')
Rowan = Villager('tall house')
#Matti = Villager('big house')