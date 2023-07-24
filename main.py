from ursina import *
from ursina.shaders import *
from ursina.prefabs.first_person_controller import FirstPersonController
import tkinter
Game = Ursina()
window.borderless = False
window.cog_button.disable()
window.fps_counter.disable()
window.exit_button.disable()
Sky()
def input(key):
    if key == "tab":
        EditorCamera()
    if key == "escape":
        mouse.locked = not mouse.locked
        
Floor = Entity(model="plane", collider="mesh", texture="white_cube",scale=(50,1,50),texture_scale=(50,50))
stuff = Entity(model="cube", color=color.black, scale=(1,1,3),position=(1,1,3),collider="box")
stuff = Entity(model="cube", color=color.black, scale=(1,4,1),position=(1,3,3),collider="box")
Player = FirstPersonController()
destroy(Player.cursor)
Game.run()
