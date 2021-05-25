import os
import yaml
import pygame as py
from Libs import ui

class LocalCharacterSelection:
	_properties = {}
	_images = {}
	_vars = {
		"background":{
			"offset": 0
		},
		"scrollY": 0,
		"targetScrollY": 0,
		"characters": [i for i in range( 30 )],
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

	def update(self, dt, game):
		self._vars["background"]["offset"] += dt * self._properties["background"]["speed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()
		
		w, h = py.display.get_surface().get_size()
		self._vars["characterSelector"]["charactersPerLine"] = int(w / (self._properties["characterContainerList"]["minSize"] + self._properties["characterContainerList"]["space"] * 2))
		self._vars["characterSelector"]["characterContainerSize"] = int(min((w - (self._properties["characterContainerList"]["space"] * 2 * self._vars["characterSelector"]["charactersPerLine"])) / self._vars["characterSelector"]["charactersPerLine"], self._properties["characterContainerList"]["maxSize"]))

		keysPressed = py.key.get_pressed()
		
		if (self._vars["characterSelector"]["timer"] > 0.20):
			if (keysPressed[py.K_RIGHT]):
				if ((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) < (self._vars["characterSelector"]["charactersPerLine"] - 1)):
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

		# Character Selector
		screen.blit(ui.CharacterContainerSelector(self._vars["characterSelector"]["characterContainerSize"], self._vars["characterSelector"]["characterContainerSize"]), ((self._vars["characterSelector"]["selectedCharacter"] % self._vars["characterSelector"]["charactersPerLine"]) * (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) + self._properties["characterContainerList"]["space"], self._properties["alphaClip"]["height"] + self._vars["scrollY"] + self._properties["characterContainerList"]["space"] + (self._vars["characterSelector"]["characterContainerSize"] + self._properties["characterContainerList"]["space"] * 2) * (self._vars["characterSelector"]["selectedCharacter"]//self._vars["characterSelector"]["charactersPerLine"])))

		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, self._properties["alphaClip"]["height"]))
		alphaClipSurface.set_alpha(self._properties["alphaClip"]["alpha"])
		alphaClipSurface.fill(tuple(self._properties["alphaClip"]["color"]))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - self._properties["alphaClip"]["height"])) # Bottom alpha clip surface

		# Transition
		if (inTransition):
			screen.blit(transition.getSurface(w, h, timeTransition), (0, 0))

		py.display.flip()