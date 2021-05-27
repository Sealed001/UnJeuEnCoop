import os
import yaml
import pygame as py
import pygame.freetype as ft
from Libs import ui
from Levels import levels

class LocalLevelSelection:
	_properties = {}
	_images = {}
	_font = None
	_vars = {
		"background":{
			"offset": 0
		},
		"message": "",
		"scrollX": 0,
		"targetScrollX": 0,
		"levels": [levels[0] for i in range(8)],
		"level": None,
		"players": None,
		"levelSelector": {
			"timer": 0,
			"selectedLevel": 0,
		}
	}

	def __init__(self, parameters):
		self._vars["players"] = parameters["players"]
		with open(f"{os.path.dirname(__file__)}/localLevelSelection.yml", 'r') as file:
			self._properties = yaml.safe_load(file)
		
		# Background Tile
		self._images["backgroundTileGreen"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Backgrounds/backgroundTileGreen.png")
		self._font = ft.Font(f"{os.path.dirname(__file__)}/../Assets/Texts/dpcomic.ttf", 24)

	def update(self, dt, game):
		self._vars["background"]["offset"] += dt * self._properties["background"]["speed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()
		
		if (self._vars["level"] == None):
			self._vars["message"] = "Please select a level with enter"
		else:
			self._vars["message"] = "Press enter to launch the game"

		keysPressed = py.key.get_pressed()
		
		if (self._vars["levelSelector"]["timer"] > 0.20):
			if (keysPressed[py.K_RIGHT]):
				if ((self._vars["levelSelector"]["selectedLevel"] + 1) < len(self._vars["levels"])):
					self._vars["levelSelector"]["selectedLevel"] += 1
					self._vars["levelSelector"]["timer"] = 0
			if (keysPressed[py.K_LEFT]):
				if ((self._vars["levelSelector"]["selectedLevel"] - 1) >= 0):
					self._vars["levelSelector"]["selectedLevel"] -= 1
					self._vars["levelSelector"]["timer"] = 0
			if (keysPressed[py.K_RETURN]):
				if (self._vars['level'] == None):
					self._vars['level'] = self._vars['levels'][self._vars["levelSelector"]["selectedLevel"]]
					self._vars["levelSelector"]["timer"] = 0
				else:
					game.routeManager.go("localPlay", parameters={"players": self._vars['players'], "level": self._vars['level']})
			if (keysPressed[py.K_BACKSPACE]):
				if (self._vars['level'] != None):
					self._vars['level'] = None
				else:
					game.routeManager.go("localCharacterSelection", parameters={"players": self._vars['players']})

		w, h = py.display.get_surface().get_size()

		self._vars["targetScrollX"] = 0
		for elI in range(len(self._vars["levels"])):
			if (elI != self._vars["levelSelector"]["selectedLevel"]):
				el = self._vars["levels"][elI]
				elSurface = ui.LevelContainer(h - 2 * (self._properties["alphaClip"]["height"] + self._properties["levelContainerList"]["space"]), elI == self._vars["levelSelector"]["selectedLevel"], el["preview"])
				self._vars["targetScrollX"] += elSurface.get_width() + self._properties["levelContainerList"]["space"]
			else:
				break
		
		if (self._vars["targetScrollX"] > self._vars["scrollX"]):
			self._vars["scrollX"] += int((self._vars["targetScrollX"] - self._vars["scrollX"]) * dt * 1.1)
		if (self._vars["targetScrollX"] < self._vars["scrollX"]):
			self._vars["scrollX"] -= int((self._vars["scrollX"] - self._vars["targetScrollX"]) * dt * 1.1)

		self._vars["levelSelector"]["timer"] += dt

	def draw(self, screen, transition, inTransition, timeTransition):
		w, h = py.display.get_surface().get_size()

		# Background
		screen.fill(tuple(self._properties["background"]["color"]))
		for x in range(-self._images["backgroundTileGreen"].get_width(), w + self._images["backgroundTileGreen"].get_width(), self._images["backgroundTileGreen"].get_width()):
			for y in range(-self._images["backgroundTileGreen"].get_height(), h + self._images["backgroundTileGreen"].get_height(), self._images["backgroundTileGreen"].get_height()):
				screen.blit(self._images["backgroundTileGreen"], (x - self._vars["background"]["offset"], y + self._vars["background"]["offset"]))
		
		# List Levels
		xOffset = (w / 2)
		for elI in range(len(self._vars["levels"])):
			el = self._vars["levels"][elI]
			elSurface = ui.LevelContainer(h - 2 * (self._properties["alphaClip"]["height"] + self._properties["levelContainerList"]["space"]), elI == self._vars["levelSelector"]["selectedLevel"], el["preview"])
			if (elI != 0):
				xOffset += elSurface.get_width() / 2
			screen.blit(elSurface, (- self._vars['scrollX'] + xOffset - elSurface.get_width() / 2, self._properties["levelContainerList"]["space"] + self._properties["alphaClip"]["height"]))
			xOffset += (elSurface.get_width() / 2 + self._properties["levelContainerList"]["space"])

		# previousLevel = None
		# previousLevelSurface = None
		# nextLevel = None
		# nextLevelSurface = None

		# if ((self._vars["levelSelector"]["selectedLevel"] - 1) >= 0):
		# 	previousLevel = self._vars["levels"][self._vars["levelSelector"]["selectedLevel"] - 1]
		# 	previousLevelSurface = ui.LevelContainer(h - 2 * (self._properties["alphaClip"]["height"] + self._properties["levelContainerList"]["space"]), False, previousLevel["preview"])

		# selectedLevel = self._vars["levels"][self._vars["levelSelector"]["selectedLevel"]]
		# selectedLevelSurface = ui.LevelContainer(h - 2 * (self._properties["alphaClip"]["height"] + self._properties["levelContainerList"]["space"]), True, selectedLevel["preview"])

		# if ((self._vars["levelSelector"]["selectedLevel"] + 1) < len(self._vars["levels"])):
		# 	nextLevel = self._vars["levels"][self._vars["levelSelector"]["selectedLevel"] + 1]
		# 	nextLevelSurface = ui.LevelContainer(h - 2 * (self._properties["alphaClip"]["height"] + self._properties["levelContainerList"]["space"]), False, nextLevel["preview"])

		# if (previousLevel != None):
		# 	screen.blit(previousLevelSurface, ((w - selectedLevelSurface.get_width()) / 2 - self._properties["levelContainerList"]["space"] - previousLevelSurface.get_width(), self._properties["levelContainerList"]["space"] + self._properties["alphaClip"]["height"]))
		
		# screen.blit(selectedLevelSurface, ((w - selectedLevelSurface.get_width()) / 2, self._properties["levelContainerList"]["space"] + self._properties["alphaClip"]["height"]))
		
		# if (nextLevel != None):
		# 	screen.blit(nextLevelSurface, ((w + selectedLevelSurface.get_width()) / 2 + self._properties["levelContainerList"]["space"], self._properties["levelContainerList"]["space"] + self._properties["alphaClip"]["height"]))
		
		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, self._properties["alphaClip"]["height"]))
		alphaClipSurface.set_alpha(self._properties["alphaClip"]["alpha"])
		alphaClipSurface.fill(tuple(self._properties["alphaClip"]["color"]))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - self._properties["alphaClip"]["height"])) # Bottom alpha clip surface

		# Message
		textSurface, textRect = self._font.render(self._vars["message"], (255, 255, 255))
		screen.blit(textSurface, (int((w - textRect.width) / 2), int(self._properties["alphaClip"]["height"] / 2 - textRect.height / 2))) 

		# Level name
		textSurface, textRect = self._font.render(self._vars["levels"][self._vars["levelSelector"]["selectedLevel"]]["name"], (255, 255, 255))
		screen.blit(textSurface, (int((w - textRect.width) / 2), int(h - (self._properties["alphaClip"]["height"] + textRect.height) / 2)))

		# Transition
		if (inTransition):
			screen.blit(transition.getSurface(w, h, timeTransition), (0, 0))

		py.display.flip()