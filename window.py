import pyglet

SCREEN_X = 1100
SCREEN_Y = 1000

draw_list = []
update_list = []

# game_window = None
game_window = pyglet.window.Window(SCREEN_X, SCREEN_Y)

def initialize():
    """Put game initialization code here"""

#    load_board_1()


    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(1, 4, PLAYER)

    print PLAYER
