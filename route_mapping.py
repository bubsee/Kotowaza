import pygame
import NPCs
def coordinate_to_matrix(x,y):
    row = y//25
    column = x//25
    return (row,column)

#format: [coords: tuple, mapping connections: tuple
nodes = {
    'A': [(1040, 187), ('X', '1')],
    'B': [(137.5, 415), ('F', '3', 'Q')],
    'C': [(610, 470), ('H','Q', 'P')],
    'D': [(899.5, 415), ('W', 'E','V')],
    'E': [(1040, 415), ('X', 'D', 'I', 'Z')],
    'F': [(137.5, 580), ('B', 'G')],
    'G': [(188.5, 640), ('F', 'H')],
    'H': [(610, 640), ('C', 'G', 'O')],
    'I': [(1040, 500), ('E','2')],
    #'J': [(851,640),('H')],
    'K': [(623.5,310),('S', 'T')],
    'L': [(899.5,305),('W')],
    'M': [(1175.5,500),('I')],
    'N': [(137.5,259),('B')],
    'O': [(640,640),()],
    'P': [(640,470),('O','C')],
    'Q': [(550,415), ('B','C','R')],
    'R': [(550,385),('Q', 'S')],
    'S': [(610,330),('R', 'T', 'K')],
    'T': [(640,330),('S','U', 'K')],
    'U': [(700,385),('T','W')],
    'V': [(700,415),('U','P', 'D')],
    'W': [(899.5, 385),('D','L', 'U','X')],
    'X': [(1040,385),('E','Y', 'A','W')],
    'Y': [(1085,385), ('X', 'Z')],
    'Z': [(1085,415), ('Y','E')],
    '1': [(1085, 187), ('Y', 'A')],
    '2': [(1085, 500), ('I', 'Z')],
    '3': [(137.5, 385), ('N','B','R')],
    '4': [(340, 640), ('G','5')],
    '5': [(480, 640), ('4','H')]
}



def display_nodes(screen):
    for node in nodes:
        pygame.draw.circle(screen, (50, 0, 0), nodes[node][0], 12, 12)
        for item in nodes[node][1]:
            edge(screen,node,item)

        font = pygame.font.SysFont(None, 24)
        text = font.render(node, True, (255, 255, 255))
        coords = (nodes[node][0][0] - 5, nodes[node][0][1] - 7)
        screen.blit(text, coords)


def edge(screen,node_1,node_2):
    pygame.draw.line(screen, (50, 0, 0), nodes[node_1][0], nodes[node_2][0], width=3)



def find_route(start:tuple,end:tuple):
    #print(f'unsnapped start: {start}')
    #print(f'unsnapped end: {end}')
    #find node which is closest to starting coordinate
    total = 1000000000000
    for node in nodes:
        distance = ((start[0]-nodes[node][0][0])**2 + (start[1]-nodes[node][0][1])**2)
        if distance < total:
            total = distance
            start_node = node

    #find node which is closest to end coordinate
    total = 1000000000000
    for node in nodes:
        distance = ((end[0] - nodes[node][0][0]) ** 2 + (end[1] - nodes[node][0][1]) ** 2)
        if distance < total:
            total = distance
            end_node = node

    start = nodes[start_node][0]
    end = nodes[end_node][0]

    #print(f'snapped start: {start}')
    #print(f'snapped end: {end}')

    #A* algorithm
    #A* algorithm
    came_from = {}
    open_nodes = [start_node]
    g_score = {start_node: 0}
    visited = []

    while open_nodes:
        #select next open node to visit
        total = 10000000000
        for node in open_nodes:
            heuristic = ((end[0]-nodes[node][0][0])**2 + (end[1]-nodes[node][0][1])**2)**(1/2)
            f_score = g_score[node] + heuristic
            if f_score < total:
                total = f_score
                next_visited = node

        #check if destination has been reached
        if next_visited == end_node:
            route = [end_node]
            while route[-1] in came_from:
                route.append(came_from[route[-1]])
            route.reverse()
            #print()
            #for node in route:
                #print(node)

            return [nodes[node][0] for node in route]

        #move it into visited, and remove it from open
        open_nodes.remove(next_visited)
        visited.append(next_visited)

        #add its neighbours to open
        for neighbour in nodes[next_visited][1]:
            if neighbour in visited:
                continue
            tentative_g_score = g_score[next_visited] + (((nodes[next_visited][0][0]-nodes[neighbour][0][0])**2 + (nodes[next_visited][0][1]-nodes[neighbour][0][1])**2)**(1/2))
            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = next_visited
                g_score[neighbour] = tentative_g_score
                if neighbour not in open_nodes:
                    open_nodes.append(neighbour)

def display_route(screen,route:list, NPC_coords:tuple):
    for i in range(len(route)):
        pygame.draw.circle(screen, (255, 0, 0), route[i], 12, 12)
        if i < len(route)-1:
            pygame.draw.line(screen, (255, 0, 0), route[i], route[i+1], width=3)
    if route:
        pygame.draw.line(screen, (255, 0, 0), route[0],NPC_coords, width=3)

    font = pygame.font.SysFont(None, 24)
    for node in nodes:
        text = font.render(node, True, (255, 255, 255))
        coords = (nodes[node][0][0] - 5, nodes[node][0][1] - 7)
        screen.blit(text, coords)