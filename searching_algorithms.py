from utils import *
from collections import deque
from queue import PriorityQueue
from grid import Grid
from spot import Spot
from math import sqrt

def bfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Breadth-First Search (BFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    queue = deque([start])
    visited = {start}
    came_from = {}

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()
        
        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()

            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def dfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Depdth-First Search (DFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    stack = [start]
    visited = {start}
    came_from = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def h_manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Heuristic function for A* algorithm: uses the Manhattan distance between two points.
    Args:
        p1 (tuple[int, int]): The first point (x1, y1).
        p2 (tuple[int, int]): The second point (x2, y2).
    Returns:
        float: The Manhattan distance between p1 and p2.
    """
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def h_euclidian_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Heuristic function for A* algorithm: uses the Euclidian distance between two points.
    Args:
        p1 (tuple[int, int]): The first point (x1, y1).
        p2 (tuple[int, int]): The second point (x2, y2).
    Returns:
        float: The Manhattan distance between p1 and p2.
    """
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def astar(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    A* Pathfinding Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0, count, start))
    came_from = {}

    g_score = {spot : float('inf') for row in grid.grid for spot in row}
    g_score[start] = 0

    f_score = {spot : float('inf') for row in grid.grid for spot in row}
    f_score[start] = h_manhattan_distance(start.get_position(), end.get_position())

    open_set = {start}

    while not open_heap.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_heap.get()[2]  # get the Spot from the heap
        open_set.remove(current)

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue

            tentative_g_score = g_score[current] + 1  # cost = 1 for all moves
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h_manhattan_distance(neighbor.get_position(), end.get_position())
                if neighbor not in open_set:
                    count += 1
                    open_heap.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def dls(draw: callable, grid: Grid, start: Spot, end: Spot, limit: int) -> bool:
    """
    Depth-Limited Search (DLS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
        limit (int): The depth limit for the search.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    stack = [(start, 0)]    
    visited = {start}
    came_from = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current, depth = stack.pop()

        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        if depth < limit:
            for neighbor in current.neighbors:
                if not neighbor.is_barrier() and neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    stack.append((neighbor, depth + 1))
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def ucs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Uninformed Cost Search (UCS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0, count, start))
    came_from = {}

    cost_so_far = {spot : float('inf') for row in grid.grid for spot in row}
    cost_so_far[start] = 0

    open_set = {start}

    while not open_heap.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_heap.get()[2]  # get the Spot from the heap
        open_set.remove(current)

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue

            new_cost = cost_so_far[current] + 1  # cost = 1 for all moves
            if new_cost < cost_so_far[neighbor]:
                came_from[neighbor] = current
                cost_so_far[neighbor] = new_cost
                if neighbor not in open_set:
                    count += 1
                    open_heap.put((cost_so_far[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def dijkstra(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Dijkstra's Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0, count, start))
    came_from = {}
    distance = {spot : float('inf') for row in grid.grid for spot in row}
    distance[start] = 0
    open_set = {start}

    while not open_heap.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_heap.get()[2]  # get the Spot from the heap
        open_set.remove(current)

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue

            new_distance = distance[current] + 1  # cost = 1 for all moves
            if new_distance < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = new_distance
                if neighbor not in open_set:
                    count += 1
                    open_heap.put((distance[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

def ids(draw: callable, grid: Grid, start: Spot, end: Spot, max_depth: int) -> bool:
    """
    Iterative Deepening Search (IDS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
        max_depth (int): The maximum depth to search.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    for depth in range(max_depth):
        if dls(draw, grid, start, end, depth):
            return True
    return False

def ida(draw: callable, grid: Grid, start: Spot, end: Spot, initial_threshold: float) -> bool:
    """
    Iterative Deepening A* (IDA*) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
        initial_threshold (float): The initial threshold for the f-cost.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    def search(current: Spot, g_score: float, threshold: float, came_from: dict, path_set: set):
        f_score = g_score + h_manhattan_distance(current.get_position(), end.get_position())
        if f_score > threshold:
            return False, f_score

        if current == end:
            return True, f_score

        min_threshold = float('inf')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for neighbor in current.neighbors:
            if neighbor.is_barrier() or neighbor in path_set:
                continue

            path_set.add(neighbor)
            came_from[neighbor] = current

            neighbor.make_open()
            draw()

            found, new_threshold = search(neighbor, g_score + 1, threshold, came_from, path_set)
            if found:
                return True, new_threshold

            path_set.remove(neighbor)

            if new_threshold < min_threshold:
                min_threshold = new_threshold

        if current != start:
            current.make_closed()
            draw()

        return False, min_threshold

    threshold = initial_threshold
    came_from = {}
    path_set = {start}

    while True:
        found, new_threshold = search(start, 0, threshold, came_from, path_set)
        if found:
            # Reconstruct path
            current = end
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        if new_threshold == float('inf'):
            return False

        threshold = new_threshold