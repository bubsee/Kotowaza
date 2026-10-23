import pygame
def coordinate_to_matrix(x,y):
    row = y//25
    column = x//25
    return (row,column)

#format: [coords: tuple, mapping connections: tuple
nodes = {
    'A': [(1058.5, 187), ('E',)],
    'B': [(137.5, 406), ('C', 'F')],
    'C': [(623.5, 406), ('B', 'D', 'H')],
    'D': [(899.5, 406), ('C', 'E')],
    'E': [(1058.5, 406), ('A', 'D', 'E')],
    'F': [(137.5, 580), ('B', 'G')],
    'G': [(188.5, 640), ('F', 'H')],
    'H': [(623.5, 640), ('C', 'G')],
    'I': [(1058.5, 500), ('E',)]
}

def display_nodes(screen):
    for node in nodes:
        pygame.draw.circle(screen, (100, 0, 0), nodes[node][0], 12, 12)
        for item in nodes[node][1]:
            edge(screen,node,item)

def edge(screen,node_1,node_2):
    pygame.draw.line(screen, (100, 0, 0), nodes[node_1][0], nodes[node_2][0], width=3)



def find_route(start:tuple,end:tuple):
    print(f'unsnapped start: {start}')
    print(f'unsnapped end: {end}')
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

    print(f'snapped start: {start}')
    print(f'snapped end: {end}')

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
            print()
            for node in route:
                print(node)

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

def display_route()