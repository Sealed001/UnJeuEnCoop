# Imports
import yaml
import pygame as py
from routeManager import RouteManager
from Routes import HomeScreen

# Vars
on = True
players = []
windowProperties = {}

# Window Properties
with open("window.yml", 'r') as file:
	windowProperties = yaml.safe_load(file)
screen = py.display.set_mode((windowProperties["width"], windowProperties["height"]))
py.display.set_caption(f"{windowProperties['title']} v{windowProperties['version']}")

# Game
routeManager = RouteManager(routes={"home": HomeScreen}, defaultRoute="home")
py.init()
while on:
	for event in py.event.get():
		if event.type == py.QUIT:
			on = False
	routeManager.update()
	routeManager.draw(screen)
py.quit()