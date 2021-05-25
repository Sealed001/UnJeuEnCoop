import os
import yaml
import pygame as py
import pygame.freetype as ft
from Libs import ui
from Characters import characters
from Levels import levels

class LocalCharacterSelection:
	_properties = {}
	_images = {}
	_font = None
	_vars = {
		"background":{
			"offset": 0
		},
		"scrollY": 0,
		"message": "",
		"targetScrollY": 0,
		"characters": characters,
		"players": [None, None],
		"characterSelector": {
			"timer": 0,
			"selectedCharacter": 0,
			"charactersPerLine": 0,
			"characterContainerSize": 0
		}
	}

	def __init__(self, parameters):
		with open(f"{os.path.dirname(__file__)}/localCharacterSelection.yml", 'r') as file:
			self._properties = yaml.safe_load(file)
		
		# Background Tile
		self._images["backgroundTileGreen"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Backgrounds/backgroundTileGreen.png")
		self._font = ft.Font(f"{os.path.dirname(__file__)}/../Assets/Texts/dpcomic.ttf", 24)

	def update(self, dt, game):
		self._vars["background"]["offset"] += dt * self._properties["background"]["speed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()
		
		if (None in self._vars["players"]):
			self._vars["message"] = f"Player {self._vars['players'].index(None) + 1}, please select a character with enter"
		else:
			self._vars["message"] = "Press enter to launch the game"

		w, h = py.display.get_surface().get_size()
		self._vars["characterSelector"]["charactersPerLine"] = int(w / (self._properties["characterContainerList"]["minSize"] + self._properties["characterContainerList"]["space"] * 2))
		self._vars["characterSelector"]["characterContainerSize"] = int(min((w - (self._properties["characterContainerList"]["space"] * 2 * self._vars["characterSelector"]["charactersPerLine"])) / self._vars["characterSelector"]["charactersPerLine"], self._properties["characterContainerList"]["maxSize"]))

		keysPressed = py.key.get_pressed()
		
		if (self._vars["characterSelector"]["timer"] > 0.20):
			if (keysPressed[py.K_RIGHT]):
				if ((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) < (self._vars["characterSelector"]["charactersPerLine"] - 1)):
					if ((self._vars["characterSelector"]["selectedCharacter"] + 1) < len(self._vars["characters"])):
						self._vars["characterSelector"]["selectedCharacter"] += 1
						self._vars["characterSelector"]["timer"] = 0
			if (keysPressed[py.K_LEFT]):
				if ((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) > 0):
					self._vars["characterSelector"]["selectedCharacter"] -= 1
					self._vars["characterSelector"]["timer"] = 0
			if (keysPressed[py.K_DOWN]):
				if ((self._vars["characterSelector"]["selectedCharacter"] + self._vars["characterSelector"]["charactersPerLine"]) < len(self._vars["characters"])):
					self._vars["characterSelector"]["selectedCharacter"] += self._vars["characterSelector"]["charactersPerLine"]
					self._vars["characterSelector"]["timer"] = 0
			if (keysPressed[py.K_UP]):
				if ((self._vars["characterSelector"]["selectedCharacter"] - self._vars["characterSelector"]["charactersPerLine"]) >= 0):
					self._vars["characterSelector"]["selectedCharacter"] -= self._vars["characterSelector"]["charactersPerLine"]
					self._vars["characterSelector"]["timer"] = 0
			if (keysPressed[py.K_RETURN]):
				if (None in self._vars['players']):
					self._vars['players'][self._vars['players'].index(None)] = self._vars["characters"][self._vars["characterSelector"]["selectedCharacter"]]
				else:
					game.routeManager.go("localPlay", parameters={"players": self._vars['players'], "level": levels[0]})
				self._vars["characterSelector"]["timer"] = 0
			if (keysPressed[py.K_BACKSPACE]):
				if (self._vars['players'][0] != None):
					if (not(None in self._vars['players'])):
						self._vars['players'][len(self._vars['players']) - 1] = None
					else:
						self._vars['players'][self._vars['players'].index(None) - 1] = None
					self._vars["characterSelector"]["timer"] = 0
				else:
					game.routeManager.go("homeScreen")


		self._vars["targetScrollY"] = -(self._properties["alphaClip"]["height"] + self._properties["characterContainerList"]["space"] + self._vars["characterSelector"]["characterContainerSize"] / 2 + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (self._vars["characterSelector"]["selectedCharacter"] // self._vars["characterSelector"]["charactersPerLine"])) + h / 2
		if (self._vars["targetScrollY"] < self._vars["scrollY"]):
			self._vars["scrollY"] -= int((self._vars["scrollY"] - self._vars["targetScrollY"]) * dt * 1.1)
		elif (self._vars["targetScrollY"] > self._vars["scrollY"]):
			self._vars["scrollY"] += int((self._vars["targetScrollY"] - self._vars["scrollY"]) * dt * 1.1)

		self._vars["characterSelector"]["timer"] += dt

	def draw(self, screen, transition, inTransition, timeTransition):
		w, h = py.display.get_surface().get_size()

		# Background
		screen.fill(tuple(self._properties["background"]["color"]))
		for x in range(-self._images["backgroundTileGreen"].get_width(), w + self._images["backgroundTileGreen"].get_width(), self._images["backgroundTileGreen"].get_width()):
			for y in range(-self._images["backgroundTileGreen"].get_height(), h + self._images["backgroundTileGreen"].get_height(), self._images["backgroundTileGreen"].get_height()):
				screen.blit(self._images["backgroundTileGreen"], (x - self._vars["background"]["offset"], y + self._vars["background"]["offset"]))
		
		# List Characters
		for elI in range(len(self._vars["characters"])):
			el = self._vars["characters"][elI]
			screen.blit(ui.CharacterContainer(self._vars["characterSelector"]["characterContainerSize"], self._vars["characterSelector"]["characterContainerSize"]), ((elI % self._vars["characterSelector"]["charactersPerLine"]) * (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) + self._properties["characterContainerList"]["space"], self._properties["alphaClip"]["height"] + self._vars["scrollY"] + self._properties["characterContainerList"]["space"] + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (elI//self._vars["characterSelector"]["charactersPerLine"])))
			if ("preview" in el):
				screen.blit(py.transform.scale(el["preview"], (self._vars["characterSelector"]["characterContainerSize"] - self._properties["characterContainerList"]["previewSpace"] * 2, self._vars["characterSelector"]["characterContainerSize"] - self._properties["characterContainerList"]["previewSpace"] * 2)), (self._properties["characterContainerList"]["previewSpace"] + (elI % self._vars["characterSelector"]["charactersPerLine"]) * (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) + self._properties["characterContainerList"]["space"], self._properties["characterContainerList"]["previewSpace"] + self._properties["alphaClip"]["height"] + self._vars["scrollY"] + self._properties["characterContainerList"]["space"] + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (elI//self._vars["characterSelector"]["charactersPerLine"])))

		# Character Selector
		screen.blit(ui.CharacterContainerSelector(self._vars["characterSelector"]["characterContainerSize"], self._vars["characterSelector"]["characterContainerSize"]), ((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) * (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) + self._properties["characterContainerList"]["space"], self._properties["alphaClip"]["height"] + self._vars["scrollY"] + self._properties["characterContainerList"]["space"] + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (self._vars["characterSelector"]["selectedCharacter"]//self._vars["characterSelector"]["charactersPerLine"])))

		textSurface, textRect = self._font.render(self._vars["characters"][self._vars["characterSelector"]["selectedCharacter"]]["name"], (255, 255, 255))
		screen.blit(textSurface, ( int((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) * (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) + self._properties["characterContainerList"]["space"] + self._vars["characterSelector"]["characterContainerSize"] / 2 - textRect.width / 2), int(self._properties["alphaClip"]["height"] + self._vars["scrollY"] + self._properties["characterContainerList"]["space"] + self._vars["characterSelector"]["characterContainerSize"] + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (self._vars["characterSelector"]["selectedCharacter"]//self._vars["characterSelector"]["charactersPerLine"]) + self._properties["characterContainerList"]["textSpace"])))

		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, self._properties["alphaClip"]["height"]))
		alphaClipSurface.set_alpha(self._properties["alphaClip"]["alpha"])
		alphaClipSurface.fill(tuple(self._properties["alphaClip"]["color"]))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - self._properties["alphaClip"]["height"])) # Bottom alpha clip surface

		# Message
		textSurface, textRect = self._font.render(self._vars["message"], (255, 255, 255))
		screen.blit(textSurface, (int(w / 2 - textRect.width / 2), int(self._properties["alphaClip"]["height"] / 2 - textRect.height / 2))) 

		# Transition
		if (inTransition):
			screen.blit(transition.getSurface(w, h, timeTransition), (0, 0))

		py.display.flip()