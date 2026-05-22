import map
import sprites

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