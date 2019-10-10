from graph_helper import *
import collections
import heapq


def get_bfs_route(start_room_id, end_room_id, graph):
    '''
    BFS for route from start_room to end_room
    '''
    current_room = graph[start_room_id]
    q = collections.deque([])
    for exit_dir in current_room["exits"]:
        q.append(([exit_dir], current_room))
    found_end = False
    # cycle protection
    visited = set()
    visited.add(start_room_id)

    while len(q) > 0:
        prev = q.popleft()
        route = prev[0]
        prev_room = prev[1]
        visited.add(prev_room["exits"][route[-1]][0])
        current_room = graph[prev_room["exits"][route[-1]][0]]
        for exit_dir in current_room["exits"]:
            exit_room_id = current_room["exits"][exit_dir][0]
            if exit_room_id == end_room_id:
                # done
                route.append(exit_dir)
                return route
            elif exit_room_id not in visited:
                # new room
                new_route = route[:]
                new_route.append(exit_dir)
                q.append((new_route, current_room))

    return -1


def get_dijk_route(start_room_id, end_room_id, graph):
    '''
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    use djikstra's algorithm to find a route from start_room to end_room
    '''
    # 1 Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    # use a heap for this, start by adding a node for start_room
    # nodes are tuples: (distance from start_room, room_id, route)
    h = []
    # 2 Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.[13]
    heapq.heappush(h, (0, start_room_id, []))
    # cycle protection
    visited = set()
    while len(h) > 0:
        check_data = heapq.heappop(h)
        curr_dist = check_data[0]
        check_room_id = check_data[1]
        check_node = graph[check_room_id]
        curr_route = check_data[2]
        # 3 For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
        for neighbor_dir in check_node["exits"]:
            neighbor_id = check_node["exits"][neighbor_dir][0]
            # done once we get to end_room
            if neighbor_id == end_room_id:
                curr_route.append(neighbor_dir)
                return curr_route
            dist = check_node["exits"][neighbor_dir][1]
            route = curr_route[:]
            route.append(neighbor_dir)
            # add each neighbor node to heap (if not visited before)
            if neighbor_id not in visited:
                heapq.heappush(h, (curr_dist + dist, neighbor_id, route))
        # 4 When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
        visited.add(check_room_id)
    # 5 If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
    # 6 Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.


def get_route_distance(start_id, route, graph):
    '''
    sum up edge weights for a given route
    '''
    distance = 0
    curr_room = graph[start_id]
    for move_dir in route:
        distance += curr_room["exits"][move_dir][1]
        curr_room = graph[curr_room["exits"][move_dir][0]]

    return distance


if __name__ == "__main__":
    graph_existing = load_stored_map("graph.json")
    # print(get_bfs_route("477", "77", graph_existing))
    # print(get_dijk_route("477", "77", graph_existing))
    for round in range(1):
        start = "0"  # str(random.choice(range(0, 500)))
        end = "3"  # str(random.choice(range(0, 500)))
        bfs_route = get_bfs_route(start, end, graph_existing)
        dijk_route = get_dijk_route(start, end, graph_existing)

        print("-" * 20)
        print(f"round {round}")
        print(f"BFS: ")
        print(f"dist: {get_route_distance(start, bfs_route, graph_existing)}")
        print(f"moves: {len(bfs_route)}")
        print(f"DJIKSTRA: ")
        print(f"dist: {get_route_distance(start, dijk_route, graph_existing)}")
        print(f"moves: {len(dijk_route)}")
