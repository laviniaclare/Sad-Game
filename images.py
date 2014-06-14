IMAGES = {}

import pyglet
def setup_images():
    filenames = {
            "Wall": "Wall Block.png",
            "Block": "Plain Block.png",
            "GrassBlock": "Grass Block.png",
            "StoneBlock": "Stone Block.png",
            "RainbowBlock": "Rainbow_block.png",
            "DarkDirt": "Dark_Dirt_Block.png",
            "ShortTree": "Tree Short.png",
            "TallTree": "Tree Tall.png",
            "BestTree": "Tree Cute.png",
            "DeadShrub": "Dead_Shrub.png",
            "RainbowTree": "RainbowTree.png",
            "MCTree": "Monochrome_Tree.png",
            "Lava": "Lava_block.png",
            "Water": "Water Block.png",
            "Rock": "Rock.png",
            "Rock2": "Rock2.png",
            "BlackRock": "Black_rock.png",
            "LavaRock": "Lava_Rock.png",
            "RainbowRock": "RainbowRock.png",
            "MCRock": "Monochrome_Rock.png",
            "Chest": "Chest Closed.png",
            "DoorClosed": "Door Tall Closed.png",
            "DoorOpen": "Door Tall Open.png",
            "BlueGem": "Gem Blue.png",
            "GreenGem": "Gem Green.png",
            "OrangeGem": "Gem Orange.png",
            "Star": "Star.png",
            "RainbowStar": "RainbowStar.png",
            "Selector": "Selector.png",
            "Heart": "Heart.png",
            "Key": "Key.png",
            "Boy": "Character Boy.png",
            "Boy2": "boy2.png",
            "RainbowBoy2": "RainbowBoy2.png",
            "MCBoy": "Monochrome Boy.png",
            "MCBoy2": "Monochrome_Boy.png",
            "Cat" : "Character Cat Girl.png",
            "RainbowCat": "RainbowCatGirl.png",
            "Horns": "Character Horn Girl.png",
            "Girl": "Character Pink Girl.png",
            "RainbowGirl1": "RainbowGirl1.png",
            "Girl2": "Character Purple Girl.png",
            "RainbowGirl2": "RainbowGirl2.png",
            "MCGirl": "Monochrome Girl.png",
            "Princess": "Character Princess Girl.png",
            "SadBoy": "SadChild.png",
            "SouthRamp": "Ramp South.png",
            "NorthRamp": "Ramp South.png",
            "WestRamp": "Ramp West.png",
            "EastRamp": "Ramp East.png"
            }

    for k,v in filenames.items():
        i = pyglet.resource.image(v)
#        i.anchor_x = i.width/2
        i.anchor_y = i.height
        IMAGES[k] = i

    # global TILE_WIDTH, TILE_HEIGHT
    TILE_WIDTH = i.width
    TILE_HEIGHT = i.height
    return (i.width, i.height)
