import pygame as py
from .player import Player

class Boyfriend:
	_player = None	

	def __init__(self, x, y):
		self._player = Player(x, y, 50, 50, 50, 50)