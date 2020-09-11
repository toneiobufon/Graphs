from room import Room
from player import Player
from world import World
from util import Queue
import sys
import os
import random
from ast import literal_eval
from typing import List

# Uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary

with open(os.path.join(sys.path[0], map_file), 'r') as f:
    room_graph = literal_eval(f.read())
# print(room_graph)

# Initialize the variables needed
world = World()
world.load_graph(room_graph)
world.print_rooms()

player = Player(world.starting_room)

moves_queue = Queue()

# traversal path to be created:
path = []

# traversal graph to be created:
graph = {}
'''
Sample graph:
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
'''
inverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

#to backtrack when reaching dead end or no more unexplored exits. returns to an unexplored room and direction
def backtrack_to_unexplored() -> List[int]:
   
    backtracking_queue = Queue()
    visited = set()
    backtracking_queue.enqueue([player.current_room.id])
    while backtracking_queue.size() > 0:
        current_path = backtracking_queue.dequeue()
        prev_room = current_path[-1]
        if prev_room not in visited:
            visited.add(prev_room)
            for direction in graph[prev_room]:
                if graph[prev_room][direction] == '?':
                    # found the way out
                    # print('path to backtrack: ', current_path)
                    return current_path
                else:
                    # make a copy of the current_path
                    current_path_copy = list(current_path)
                    current_path_copy.append(graph[prev_room][direction])
                    backtracking_queue.enqueue(current_path_copy)

    # If no valid backtracking path is found
    return []

#adds a possible choice of unexplored random rooms or exits  
def enqueue_moves():
  
    current_room_exits = graph[player.current_room.id]
   
    unexplored_exits = []
    for direction in current_room_exits:
        if current_room_exits[direction] == '?':
            unexplored_exits.append(direction)
    if len(unexplored_exits) > 0:
        # Go to a random choice of the unexplored exits
        moves_queue.enqueue(
            unexplored_exits[random.randint(0, len(unexplored_exits)-1)])
    else:
        # Backtrack to a room that has unexplored exits
        path_to_unexplored = backtrack_to_unexplored()
        current_room_id = player.current_room.id
        for room_id in path_to_unexplored:
            for direction in graph[current_room_id]:
                if room_id == graph[current_room_id][direction]:

                    moves_queue.enqueue(direction)
                    current_room_id = room_id
                    # Go on to next room in path_to_unexplored
                    break


def create_path():
    new_room = {}
    for direction in player.current_room.get_exits():
        new_room[direction] = '?'
    graph[player.current_room.id] = new_room
    enqueue_moves()

    while moves_queue.size() > 0:
        # print('current moves_queue: ', moves_queue)
        starting_room_id = player.current_room.id
        next_direction = moves_queue.dequeue()
        player.travel(next_direction)
        path.append(next_direction)
        current_room_id = player.current_room.id
        graph[starting_room_id][next_direction] = current_room_id

        if current_room_id not in graph:
            # Create a new entry
            graph[current_room_id] = {}
            current_room_exits = player.current_room.get_exits()
            for direction in current_room_exits:
                graph[current_room_id][direction] = '?'

        # Link the current room to the starting room
        graph[current_room_id][inverse_directions[next_direction]] = starting_room_id
        
        
        # Get the next move if the moves_queue is empty.
        if moves_queue.size() <= 0:
            enqueue_moves()


def move_player_along_path():
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)
    for direction in path:
        player.travel(direction)
        visited_rooms.add(player.current_room)

    print("Rooms visited: ", len(visited_rooms))
    print("Path Length: ", len(path))

#information to display
create_path()
move_player_along_path()