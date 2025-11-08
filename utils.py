import pygame

WIDTH = 800
HEIGHT = 800

INTERFACE_HEIGHT = 80

# colors as hex values
COLORS2 = {
    'CLOSED': 0xF4442E,           # closed nodes
    'OPEN': 0x982649,             # open nodes
    'START': 0x06BCC1,            # start node
    'END': 0xFF579F,              # end node
    'UNVISITED': 0x444554,        # unvisited nodes
    'BARRIER': 0x031926,          # barrier
    'PATH': 0x84DCC6,             # path
    'GRID_LINES': 0x595358,       # grid lines
}