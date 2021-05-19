import os
import yaml
import pygame as py
from .ui import BigButton

class HomeScreen:
	_properties = {}
	_images = {}
	_vars = {
		"background":{
			"offset": 0
		},
		"selectedButton": "local"
	}

	def __init__(self, parameters):
		with open(f"{os.path.dirname(__file__)}/homeScreen.yml", 'r') as file:
			self._properties = yaml.safe_load(file)
		
		# Background Tile
		self._images["backgroundTileGreen"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Backgrounds/backgroundTileGreen.png")

		# Buttons Icons
		self._images["optionsIcon"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Icons/options.png")
		self._images["onlineIcon"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Icons/online.png")
		self._images["quitIcon"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Icons/quit.png")
		self._images["localIcon"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Icons/local.png")

		# Buttons Texts
		self._images["optionsText"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Texts/optionsText.png")
		self._images["onlineText"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Texts/onlineText.png")
		self._images["quitText"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Texts/quitText.png")
		self._images["localText"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Texts/localText.png")

	def update(self, dt):
		self._vars["background"]["offset"] += dt * self._properties["background"]["speed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()

	def draw(self, screen):
		w, h = py.display.get_surface().get_size()

		# Background
		screen.fill(tuple(self._properties["background"]["color"]))
		for x in range(-self._images["backgroundTileGreen"].get_width(), w + self._images["backgroundTileGreen"].get_width(), self._images["backgroundTileGreen"].get_width()):
			for y in range(-self._images["backgroundTileGreen"].get_height(), h + self._images["backgroundTileGreen"].get_height(), self._images["backgroundTileGreen"].get_height()):
				screen.blit(self._images["backgroundTileGreen"], (x + self._vars["background"]["offset"], y + self._vars["background"]["offset"]))
		
		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, self._properties["alphaClip"]["height"]))
		alphaClipSurface.set_alpha(self._properties["alphaClip"]["alpha"])
		alphaClipSurface.fill(tuple(self._properties["alphaClip"]["color"]))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - self._properties["alphaClip"]["height"])) # Bottom alpha clip surface

		# Buttons
		buttonWidth = (w / 2) - self._properties["buttons"]["gap"] * 2
		buttonHeight = ((h - self._properties["alphaClip"]["height"] * 2) / 2) - self._properties["buttons"]["gap"] * 2

		# Local Button
		buttonX = self._properties["buttons"]["gap"]
		buttonY = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"]
		screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["local"]["color"]["background"]), tuple(self._properties["buttons"]["local"]["color"]["iconBackground"]), self._images["localIcon"], self._images["localText"]), (buttonX, buttonY))

		# Options Button
		buttonX = (w / 2) + self._properties["buttons"]["gap"]
		buttonY = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"]
		screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["options"]["color"]["background"]), tuple(self._properties["buttons"]["options"]["color"]["iconBackground"]), self._images["optionsIcon"], self._images["optionsText"]), (buttonX, buttonY))

		# Online Button
		buttonX = self._properties["buttons"]["gap"]
		buttonY = self._properties["alphaClip"]["height"] + ((h - self._properties["alphaClip"]["height"] * 2) / 2) + self._properties["buttons"]["gap"]
		screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["online"]["color"]["background"]), tuple(self._properties["buttons"]["online"]["color"]["iconBackground"]), self._images["onlineIcon"], self._images["onlineText"]), (buttonX, buttonY))

		# Quit Button
		buttonX = (w / 2) + self._properties["buttons"]["gap"]
		buttonY = self._properties["alphaClip"]["height"] + ((h - self._properties["alphaClip"]["height"] * 2) / 2) + self._properties["buttons"]["gap"]
		screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["quit"]["color"]["background"]), tuple(self._properties["buttons"]["quit"]["color"]["iconBackground"]), self._images["quitIcon"], self._images["quitText"]), (buttonX, buttonY))

		py.display.flip()