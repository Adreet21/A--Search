from heapq import heappush, heappop
import time

class Zombie_problem(object):

    def __init__(self):
        self.start_state = ('Left ', 'Left ', 'Left ', 'Left ', 'Left ')
        self.crossing_times = [1, 2, 5, 10]

    def start_node(self):
        """Returns the start state"""
        return self.start_state

    def is_goal(self, node):
        """Returns True if node is a goal state"""
        for i in range(len(node) - 1):
            position = node[i]
            if position != 'Right':
                return False
        return True

    def neighbors(self, node):
        """Returns a list of neighbors of node"""
        neighbors = []
        LEFT = 'Left '
        RIGHT = 'Right'
        flightPosition = node[-1]
        all_moves = [(0,), (1,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        for move in all_moves:
            valid_move = True
            for character_index in move:
                if node[character_index] != flightPosition:
                    valid_move = False
                    break
            if valid_move:
                new_state = list(node)
                for character_index in move:
                    if new_state[character_index] == LEFT:
                        new_state[character_index] = RIGHT
                    else:
                        new_state[character_index] = LEFT
                if flightPosition == LEFT:
                    new_state[-1] = RIGHT
                else:
                    new_state[-1] = LEFT
                move_cost = 0
                if move:
                    slowest_time = 0
                    for character_index in move:
                        character_time = self.crossing_times[character_index]
                        if character_time > slowest_time:
                            slowest_time = character_time
                    move_cost = slowest_time
                neighbors.append((tuple(new_state), move_cost))
        return neighbors

    def arc_cost(self, arc):
        """Returns the cost of arc"""
        return arc[1]

    def cost(self, path):
        """Returns the cost of path"""
        return sum(self.arc_cost(arc) for arc in path)

    def heuristic(self, node):
        """Returns the heuristic value of node"""
        l_side = []
        for i in range(len(node) - 1):
            position = node[i]
            if position == 'Left ':
                crossing_time = self.crossing_times[i]
                l_side.append(crossing_time)
        if len(l_side) > 0:
            max_time = 0
            for time in l_side:
                if time > max_time:
                    max_time = time
            return max_time
        else:
            return 0

    def search(self):
        """A* search"""
        frontier = []
        initial_heuristic = self.heuristic(self.start_node())
        initial_cost = (self.start_node(), 0)
        heappush(frontier, (initial_heuristic, [initial_cost]))
        while len(frontier) > 0:
            current_cost, current_path = heappop(frontier)
            current_node = current_path[-1][0]
            if self.is_goal(current_node):
                return current_path
            neighbors = self.neighbors(current_node)
            for neighbor in neighbors:
                next_state, step_cost = neighbor
                new_path = list(current_path)
                new_path.append((next_state, step_cost))
                new_cost = self.cost(new_path) + self.heuristic(next_state)
                heappush(frontier, (new_cost, new_path))
        return None

def format_solution(solution, crossing_times):
    """Format the solution path for better readability"""
    result = []
    for state, cost in solution:
        formatted_state = ', '.join(state[:-1]) + ' | Flashlight: ' + state[-1]
        result.append(f"State: [{formatted_state}] - Cost: {cost}")
    total_cost = sum(cost for _, cost in solution)
    result.append(f"\nTotal cost: {total_cost}")
    return '\n'.join(result)

def unit_tests():
    """
    Some trivial tests to check that the implementation even runs.
    Feel free to add additional tests.
    """
    print("testing...")
    time.sleep(2)

    p = Zombie_problem()
    assert p.start_node() is not None
    assert not p.is_goal(p.start_node())
    assert p.heuristic(p.start_node()) >= 0

    ns = p.neighbors(p.start_node())
    assert len(ns) > 0

    soln = p.search()
    assert p.cost(soln) > 0
    print("tests ok")

def main():
    unit_tests()
    p = Zombie_problem()
    soln = p.search()
    if soln:
        print("Solution found:")
        print("State: [Position A , Position B , Position C , Position D  | Position Flashlight ] - Cost of that move.")
        print(format_solution(soln, p.crossing_times))
    else:
        raise RuntimeError("Empty solution")

if __name__ == '__main__':
    main()