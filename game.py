import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 9
GAME_HEIGHT = 9

#### Put class definitions here ####
class Portal1(GameElement):
    IMAGE="Selector"
    SOLID=True
    def interact(self, player):
        if len(player.inventory)> 0 :
            GAME_BOARD.draw_msg("Good job! Next dimension!")
            level2()
            load_board_2()
            print GAME_BOARD
        else:
            GAME_BOARD.draw_msg("You probably want to explore some more before leaving...")

class Yellow_Star(GameElement):
    IMAGE="Star"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a yellow star! You have %d items!" %(len(player.inventory)))


class Best_Tree(GameElement):
    IMAGE="BestTree"
    SOLID=True

class Dead_Shrub(GameElement):
    IMAGE="DeadShrub"
    SOLID=True

class Rock(GameElement):
    IMAGE="Rock"
    SOLID = True

class Blue_Rock(GameElement):
    IMAGE="Rock2"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a BLUE ROCK! You have %d items!" %(len(player.inventory)))

class Heart(GameElement):
    IMAGE = "Heart"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a heart! You have %d items!" %(len(player.inventory)))


class Rainbow_Rock(GameElement):
    IMAGE = "RainbowRock"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a Rainbow Rock! Weird.  Do those even exists? Maybe it will be useful later. You have %d items!" %(len(player.inventory)))

class Rainbow_Girl1(GameElement):
    IMAGE="RainbowGirl1"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("That rock you're holding...I've never seen such a boring rock. I'm kind of a collector of really boring kitsch. I have my own museum. It has a...okay, there's nothing really in besides this seed, but that rock is totally more boring. Will you trade?")

    #Interactive text choices here

class Rainbow_Girl2(GameElement):
    IMAGE="RainbowGirl2"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Living here kind of makes my eyes hurt. I wonder why that is?")

class Rainbow_Boy2(GameElement):
    IMAGE="RainbowBoy2"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("I tHiNk I aM gOiNg InSaNe..............haha, just kidding. This place is pretty cool.")

class Rainbow_Cat(GameElement):
    IMAGE="RainbowCat"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Can you imagine how difficult it is to choose an outfit in the morning? Nothing matches here!")

class Rainbow_Star(GameElement):
    IMAGE="RainbowStar"
    SOLID=True

class Rainbow_Tree(GameElement):
    IMAGE="RainbowTree"
    SOLID=True


class Rainbok_Block(GameElement):
    IMAGE="RainbowBlock"
    SOLID=True


class Grass_Block(GameElement):
    IMAGE="GrassBlock"
    SOLID=True

class Lava_Rock(GameElement):
    IMAGE="LavaRock"
    SOLID=True

class SBlack_Rock(GameElement):
    IMAGE="BlackRock"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a BLACK ROCK! Maybe this will be useful later. You have %d items!" %(len(player.inventory)))

class Black_Rock(GameElement):
    IMAGE="BlackRock"
    SOLID=True

class SadChild(GameElement):
    IMAGE="SadBoy"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Hello, Traveler. If you were planning on having a nice time here, you came at the wrong time. *sniffle* All of our plants are dead.  We have no food. Soon we will all be dead, too. *tear runs down cheek* If only someone would bring us Best Tree seeds, we could plant them in the lava to turn it to water and revive our crops. Alas! No one here has the strength to go. *can no longer control his desperate sobbing*  If you got some for us, we would be so happy.  We might even have a happy party for once. My parents died at the last party. It was not happy.")

class Boy2(GameElement):
    IMAGE="Boy2"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Don't talk to the sad kid down there--he's such a downer. I, on the other hand, have come to peace with my inevitable starvation.")

class Cat(GameElement):
    IMAGE="Cat"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Best Trees are the eighth wonder of the world! They will save us all! ...if you get going soon.")

class Girl(GameElement):
    IMAGE="Girl"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Before this, I was known for my prized orchids. ...now I have no identity. How will people remember me now? What will they say at my eulogy?")
       

class Girl2(GameElement):
    IMAGE="Girl2"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("When the volcano first erupted, I thought the new color scheme was cool, but now black and red seems so last year. Oh well...I heard that fasting is a good detox...I bet my colon's really clean now.")
       

class MC_Girl(GameElement):
    IMAGE="MCGirl"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Whoa! What are all of those weird colors on your clothes? I've never seen such vibrant colors before! Are you....from someplace else?")

class MC_Boy2(GameElement):
    IMAGE="MCBoy2"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Wow! That rock you've got---it has more colors than I could ever imagine! Can I have it?")
        GAME_BOARD.check_status("Waiting...")
        # if status=="Waiting...":
#Interactive text here. 

class MC_Boy(GameElement):
    IMAGE="MCBoy"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("I never have to worry about getting dressed for special occasions! This is the same outfit I wore to Bob's wedding! My aunt's funeral! My own bar mitzvah!")

class MC_Rock(GameElement):
    IMAGE="MCRock"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a MONOCHROME ROCK (Basically a normal rock, but lighter)! Maybe this will be useful later. You have %d items!" %(len(player.inventory)))

class MC_Tree(GameElement):
    IMAGE="MCTree"
    SOLID=True

class MC_Block(GameElement):
    IMAGE="Block"
    SOLID=True

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

class Character(GameElement):
    IMAGE="Horns"
    SOLID=True        


    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None
#THIS SYNTAX IS USEFUL FOR BORDERS ^^^^^^^

        
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

    load_board_1()
    level1()
    print GAME_BOARD


    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(1, 4, PLAYER)

    print PLAYER


####Levels here.  Do not delete.#####
def level1():
    black_rock_positions=[
                        (5,4),
                        (2,3),
                        (6,6)
                        ]
    brocks=[]

    for pos in black_rock_positions:
        black_rock=Black_Rock()
        GAME_BOARD.register(black_rock)
        GAME_BOARD.set_el(pos[1], pos[0], black_rock)
        brocks.append(black_rock)

    for black_rock in brocks:
        print black_rock

    special_black_rock = SBlack_Rock()
    GAME_BOARD.register(special_black_rock)
    GAME_BOARD.set_el(1, 1, special_black_rock)


    lava_rock = Lava_Rock()
    GAME_BOARD.register(lava_rock)
    GAME_BOARD.set_el(1, 7, lava_rock)

    lava_rock = Lava_Rock()
    GAME_BOARD.register(lava_rock)
    GAME_BOARD.set_el(1, 2, lava_rock)


    dead_shrub_positions=[
            (7,1),
            (7,2),
            (7,3),
            (7,4),
            (1,5)
            ]
    shrubs=[]
    
    for pos in dead_shrub_positions:
        shrub=Dead_Shrub()
        GAME_BOARD.register(shrub)
        GAME_BOARD.set_el(pos[0], pos[1], shrub)
        shrubs.append(shrub)

    for shrub in shrubs:
      print shrub

    cat_girl = Cat()
    GAME_BOARD.register(cat_girl)
    GAME_BOARD.set_el(7, 5, cat_girl)

    boy2 = Boy2()
    GAME_BOARD.register(boy2)
    GAME_BOARD.set_el(6, 3, boy2)

    sad_child = SadChild()
    GAME_BOARD.register(sad_child)
    GAME_BOARD.set_el(4, 7, sad_child)

    # if not :
    portal = Portal1()
    GAME_BOARD.register(portal)
    GAME_BOARD.set_el(7, 7, portal)


    GAME_BOARD.draw_msg("This game, it is the saddest. :( :( :*( ")

def level2():
    rainbow_rock_positions=[
                        (5,4),
                        (2,3),
                        (6,6)
                        ]
    rainbow_rocks=[]

    for pos in rainbow_rock_positions:
        rainbow_rock=Rainbow_Rock()
        GAME_BOARD.register(rainbow_rock)
        GAME_BOARD.set_el(pos[1], pos[0], rainbow_rock)
        rainbow_rocks.append(rainbow_rock)

    for rainbow_rock in rainbow_rocks:
        print rainbow_rock

    rainbow_star = Rainbow_Star()
    GAME_BOARD.register(rainbow_star)
    GAME_BOARD.set_el(1, 7, rainbow_star)

    rainbow_star = Rainbow_Star()
    GAME_BOARD.register(rainbow_star)
    GAME_BOARD.set_el(1, 2, rainbow_star)


    rainbow_tree_positions=[
            (7,1),
            (7,2),
            (7,3),
            (7,4),
            (1,5)
            ]
    trees=[]
    
    for pos in rainbow_tree_positions:
        tree=Rainbow_Tree()
        GAME_BOARD.register(tree)
        GAME_BOARD.set_el(pos[0], pos[1], tree)
        trees.append(tree)

    for tree in trees:
      print tree

    rainbow_cat_girl = Rainbow_Cat()
    GAME_BOARD.register(rainbow_cat_girl)
    GAME_BOARD.set_el(7, 5, rainbow_cat_girl)

    rainbow_boy2 = Rainbow_Boy2()
    GAME_BOARD.register(rainbow_boy2)
    GAME_BOARD.set_el(6, 3, rainbow_boy2)

    rainbow_girl = Rainbow_Girl2()
    GAME_BOARD.register(rainbow_girl)
    GAME_BOARD.set_el(4, 7, rainbow_girl)

    # portal = Portal2()
    # GAME_BOARD.register(portal)
    # GAME_BOARD.set_el(8, 4, portal)

def level3():
    mc_rock_positions=[
                        (5,4),
                        (2,3),
                        (6,6)
                        ]
    mc_rocks=[]

    for pos in mc_rock_positions:
        mc_rock=MC_Rock()
        GAME_BOARD.register(mc_rock)
        GAME_BOARD.set_el(pos[1], pos[0], mc_rock)
        mc_rocks.append(mc_rock)

    for mc_rock in mc_rocks:
        print mc_rock

    mc_block = MC_Block()
    GAME_BOARD.register(mc_block)
    GAME_BOARD.set_el(1, 7, mc_block)

    mc_block = MC_Block()
    GAME_BOARD.register(mc_block)
    GAME_BOARD.set_el(1, 2, mc_block)


    mc_tree_positions=[
            (7,1),
            (7,2),
            (7,3),
            (7,4),
            (1,5)
            ]
    trees=[]
    
    for pos in mc_tree_positions:
        tree=MC_Tree()
        GAME_BOARD.register(tree)
        GAME_BOARD.set_el(pos[0], pos[1], tree)
        trees.append(tree)

    for tree in trees:
      print tree

    mc_boy = MC_Boy()
    GAME_BOARD.register(mc_boy)
    GAME_BOARD.set_el(7, 5, mc_boy)

    mc_boy2 = MC_Boy2()
    GAME_BOARD.register(mc_boy2)
    GAME_BOARD.set_el(6, 3, mc_boy2)

    mc_girl = MC_Girl()
    GAME_BOARD.register(mc_girl)
    GAME_BOARD.set_el(4, 7, mc_girl)

    # portal = Portal()
    # GAME_BOARD.register(portal)
    # GAME_BOARD.set_el(8, 4, portal)




    GAME_BOARD.draw_msg("Wow, it's like and old movie.")

####End levels section###


def keyboard_handler():
    direction = None
     # GAME_BOARD.check_status()
     #    if status=="Waiting...":
     #        if KEYBOARD[key.ENTER]:
     #        #Do stuff
     #        #next() <---what to do if enter is hit.
     #        pass

    if KEYBOARD[key.UP]:
        direction = "up"
        print "key is up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

               
    
    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)
            # player.inventory.append(heart)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)


import engine


def load_board_1():
    b = engine.load_board_1()
    global GAME_BOARD
    GAME_BOARD = b
    print 1, GAME_BOARD
    engine.draw_list.append(b)

def load_board_2():
    b = engine.load_board_2()
    global GAME_BOARD
    GAME_BOARD = b
    print 1, GAME_BOARD
    engine.draw_list.append(b)

