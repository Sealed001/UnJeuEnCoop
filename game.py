# Imports
from Routes.localCharacterSelection import LocalCharacterSelection
import yaml
import pygame as py
from routeManager import RouteManager
from Libs import transition
from Routes import HomeScreen, LocalCharacterSelection, LocalLevelSelection, Options, LocalPlay

class Game():
	on = True
	gameProperties = {}
	screen = None
	routeManager = None

	def __init__(self):
		# Window Properties
		with open("game.yml", 'r') as file:
			self.gameProperties = yaml.safe_load(file)
		self.screen = py.display.set_mode((self.gameProperties["width"], self.gameProperties["height"]), py.RESIZABLE)
		py.display.set_caption(f"{self.gameProperties['title']} v{self.gameProperties['version']}")

		# Game
		self.routeManager = RouteManager(transition.GrowingDotsTransition(easingFunc=transition.EASEINOUTCUBIC), self.gameProperties["transitionDuration"], routes={"homeScreen": HomeScreen, "localCharacterSelection": LocalCharacterSelection, "localLevelSelection": LocalLevelSelection, "options": Options, "localPlay": LocalPlay}, defaultRoute="homeScreen")
		py.init()

game = Game()

while game.on:
	for event in py.event.get():
		if event.type == py.QUIT:
			game.on = False
	
	game.routeManager.update(game)
	game.routeManager.draw(game.screen)

py.quit()