from utils import *
from grid import Grid
from searching_algorithms import *

if __name__ == "__main__":
    pygame.font.init()
    
    WIN = pygame.display.set_mode((WIDTH, HEIGHT + INTERFACE_HEIGHT))

    pygame.display.set_caption("Path Visualizing Algorithm")

    ROWS = 50
    COLS = 50
    grid = Grid(WIN, ROWS, COLS, WIDTH, HEIGHT)

    start = None
    end = None

    font = pygame.font.SysFont("Times New Roman", 18)

    button_bfs = pygame.Rect(10, HEIGHT + 10, 90, 30)
    button_dfs = pygame.Rect(110, HEIGHT + 10, 90, 30)
    button_astar = pygame.Rect(210, HEIGHT + 10, 90, 30)
    button_dls = pygame.Rect(310, HEIGHT + 10, 90, 30)
    button_ucs = pygame.Rect(410, HEIGHT + 10, 90, 30)
    button_dijkstra = pygame.Rect(510, HEIGHT + 10, 110, 30)
    button_ids = pygame.Rect(630, HEIGHT + 10, 90, 30)
    button_ida = pygame.Rect(730, HEIGHT + 10, 90, 30)
    button_clear = pygame.Rect(10, HEIGHT + 45, 150, 25)

    buttons = [
        (button_bfs, "BFS"),
        (button_dfs, "DFS"),
        (button_astar, "A*"),
        (button_dls, "DLS"),
        (button_ucs, "UCS"),
        (button_dijkstra, "Dijkstra"),
        (button_ids, "IDS"),
        (button_ida, "IDA*"),
        (button_clear, "CLEAR GRID")
    ]

    def draw_interface():
        pygame.draw.rect(WIN, (220, 220, 220), (0, HEIGHT, WIDTH, INTERFACE_HEIGHT))
        
        for rect, text in buttons:
            pygame.draw.rect(WIN, (170, 170, 170), rect)
            WIN.blit(font.render(text, True, (0, 0, 0)),
                     (rect.x + 10, rect.y + 5))

    def draw_grid_only():
        pygame.draw.rect(WIN, COLORS2['UNVISITED'], (0, 0, WIDTH, HEIGHT))
        
        for row in grid.grid:
            for spot in row:
                spot.draw(WIN)
        
        grid.draw_grid_lines()
    
    def draw_algorithm_step():
        draw_grid_only()
        pygame.display.update(pygame.Rect(0, 0, WIDTH, HEIGHT))

    run = True
    started = False

    while run:
        draw_grid_only()  
        draw_interface() 
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                
                if pos[1] < HEIGHT:
                    row, col = grid.get_clicked_pos(pos)

                    if 0 <= row < ROWS and 0 <= col < COLS:
                        spot = grid.grid[row][col]
                        if not start and spot != end:
                            start = spot
                            start.make_start()
                        elif not end and spot != start:
                            end = spot
                            end.make_end()
                        elif spot != end and spot != start:
                            spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  
                pos = pygame.mouse.get_pos()
                
                if pos[1] < HEIGHT:
                    row, col = grid.get_clicked_pos(pos)
                    if 0 <= row < ROWS and 0 <= col < COLS:
                        spot = grid.grid[row][col]
                        spot.reset()

                        if spot == start:
                            start = None
                        elif spot == end:
                            end = None

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                
                if button_bfs.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    bfs(draw_algorithm_step, grid, start, end)
                    started = False
                
                elif button_dfs.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    dfs(draw_algorithm_step, grid, start, end)
                    started = False
                
                elif button_astar.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    astar(draw_algorithm_step, grid, start, end)
                    started = False
                
                elif button_dls.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    dls(draw_algorithm_step, grid, start, end, limit=1000)
                    started = False
                
                elif button_ucs.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    ucs(draw_algorithm_step, grid, start, end)
                    started = False
                
                elif button_dijkstra.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    dijkstra(draw_algorithm_step, grid, start, end)
                    started = False
                
                elif button_ids.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    ids(draw_algorithm_step, grid, start, end, max_depth=1000)
                    started = False
                
                elif button_ida.collidepoint(mouse_pos) and start and end and not started:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    initial_threshold = h_manhattan_distance(start.get_position(), end.get_position())
                    ida(draw_algorithm_step, grid, start, end, initial_threshold)
                    started = False
                
                elif button_clear.collidepoint(mouse_pos):
                    print("Clearing the grid...")
                    start = None
                    end = None
                    grid.reset()

    pygame.quit()