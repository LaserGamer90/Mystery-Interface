from ursina import *
from ursina.shaders import *
from ursina.prefabs.first_person_controller import FirstPersonController
Game = Ursina()
window.borderless = False
window.cog_button.disable()
window.fps_counter.disable()
window.exit_button.disable()
Sky()
Floor = Entity(model="plane", collider="mesh", texture="white_cube",scale=(50,50))
Player = FirstPersonController()
Game.run()
