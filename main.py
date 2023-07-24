from ursina import *
from ursina.shaders import *
from ursina.prefabs.first_person_controller import FirstPersonController
import tkinter
#
#
Game = Ursina()
window.borderless = False
window.cog_button.disable()
window.fps_counter.disable()
window.exit_button.disable()
Sky()
def input():
    if key == "tab":
        EditorCamera()
    if key == "escape":
        mouse.locked = not mouse.locked
        
Floor = Entity(model="plane", collider="mesh", texture="brown_cube",scale=(50,1,50),texture_scale=(51,49))
Player = FirstPersonController()
Game.run()
