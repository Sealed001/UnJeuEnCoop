import os
import pygame as py

class NewYork:
	_background = None
	_platforms = []
	_players = []

	def __init__(self):
		self._background = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Levels/newyork.png")

	def getSurface(self):
		w, h = py.display.get_surface().get_size()

		surface = py.Surface((w, h), py.SRCALPHA, 32)

		surface.blit(self._background, (0, 0))

		return surface

