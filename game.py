# Imports
import yaml
import pygame as py
from routeManager import RouteManager
from Routes import HomeScreen

class Game():
	on = True
	windowProperties = {}
	screen = None
	routeManager = None

	def __init__(self):
		# Window Properties
		with open("window.yml", 'r') as file:
			self.windowProperties = yaml.safe_load(file)
		self.screen = py.display.set_mode((self.windowProperties["width"], self.windowProperties["height"]))
		py.display.set_caption(f"{self.windowProperties['title']} v{self.windowProperties['version']}")

		# Game
		self.routeManager = RouteManager(routes={"home": HomeScreen}, defaultRoute="home")
		py.init()

game = Game()

while game.on:
	for event in py.event.get():
		if event.type == py.QUIT:
			game.on = False
	game.routeManager.update(game)
	game.routeManager.draw(game.screen)

py.quit()