import os
import yaml
import pygame as py

class HomeScreen:
	_properties = {}
	_images = {}
	_vars = {
		"background":{
			"offset": 0
		},
		"selectedButton": "solo"
	}

	def __init__(self, parameters):
		with open(f"{os.path.dirname(__file__)}/homeScreen.yml", 'r') as file:
			self._properties = yaml.safe_load(file)
		
		self._images["backgroundTileGreen"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Backgrounds/backgroundTileGreen.png")
		self._images["backgroundTileGreen"].convert()

	def update(self, dt):
		self._vars["background"]["offset"] += dt * self._properties["backgroundSpeed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()

	def draw(self, screen):
		screen.fill((34, 32, 52))
		w, h = py.display.get_surface().get_size()

		# Backgrounds
		for x in range(-self._images["backgroundTileGreen"].get_width(), w + self._images["backgroundTileGreen"].get_width(), self._images["backgroundTileGreen"].get_width()):
			for y in range(-self._images["backgroundTileGreen"].get_height(), h + self._images["backgroundTileGreen"].get_height(), self._images["backgroundTileGreen"].get_height()):
				screen.blit(self._images["backgroundTileGreen"], (x + self._vars["background"]["offset"], y + self._vars["background"]["offset"]))
		
		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, 100))
		alphaClipSurface.set_alpha(180)
		alphaClipSurface.fill((0, 0, 0))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - 100)) # Bottom alpha clip surface


		py.display.flip()