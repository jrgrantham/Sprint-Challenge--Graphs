from room import Room
from player import Player
from world import World
import copy
import random
from ast import literal_eval
from utils import Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = {}

def set_exits(room):
    if graph.get(room):
        return
    else:
        graph[room] = {}
    for exit in player.current_room.get_exits():
        graph[room][exit] = '?'

def connect_rooms(previous, current, direction):
    set_exits(current)
    pairs = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    graph[previous][direction] = current 
    graph[current][pairs[direction]] = previous

def unexplored_exits(room):
    results = []
    for exit in player.current_room.get_exits():
        if graph[room][exit] == '?':
            results.append(exit)
    return results

set_exits(player.current_room.id)
previous_room = player.current_room.id

room_queue = Queue()
room_queue.enqueue(player.current_room)

print('-' * 20)
print(f'you are in room {player.current_room.id}')
print(f'your options are {player.current_room.get_exits()}')
print('-' * 20)

while len(graph) < len(world.rooms):
    move = random.choice(unexplored_exits(player.current_room.id))
    player.travel(move)
    traversal_path.append(move)
    connect_rooms(previous_room, player.current_room.id, move)
    print('-' * 20)
    print(f'you were in room {previous_room}')
    print(f'you are now in room {player.current_room.id}')
    print(f'your options are {player.current_room.get_exits()}')
    print(f'rooms visited {graph[player.current_room.id]}')
    print(f'unvisited {unexplored_exits(player.current_room.id)}')
    print('-' * 20)
    previous_room = player.current_room.id

print(graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
