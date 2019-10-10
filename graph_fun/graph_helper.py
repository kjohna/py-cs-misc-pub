from pathlib import Path  # python3 only
import json
import os
import random


def load_stored_map(filename):
    '''
    load map graph data from file
    '''
    working_dir = os.path.dirname(os.path.abspath(__file__))

    with open(working_dir + f'/{filename}', 'r+') as f:
        graph_existing = json.loads(f.read().strip().rstrip())

    return graph_existing


def update_stored_map(map_graph):
    '''
    dump map graph data to file
    '''
    working_dir = os.path.dirname(os.path.abspath(__file__))
    with open(working_dir + '/graph.json', 'w+') as f:
        json.dump(map_graph, f, sort_keys=True, indent=4)


def opposite(direction):
    '''
    return opposite direction
    '''
    opposites = {
        "n": "s",
        "e": "w",
        "s": "n",
        "w": "e"
    }
    return opposites[direction]


def convert_to_weighted(graph_existing):
    '''
    add edge weights to graph
    '''
    for room_id in graph_existing:
        for exit_id in graph_existing[room_id]["exits"]:
            # only update if exit is string type (not converted to weighted yet)
            if type(graph_existing[room_id]["exits"][exit_id]) == str:
                edge_weight = random.choice(range(1, 6))
                exit_room = graph_existing[room_id]["exits"][exit_id]
                new_exit = (exit_room, edge_weight)
                graph_existing[room_id]["exits"][exit_id] = new_exit
                # also update exit room so edge weights match
                opp_exit = (room_id, edge_weight)
                graph_existing[exit_room]["exits"][opposite(
                    exit_id)] = opp_exit
    return 0


if __name__ == "__main__":

    graph_existing = load_stored_map()
    # updates unweighted graph to weighted
    convert_to_weighted(graph_existing)
    update_stored_map(graph_existing)
