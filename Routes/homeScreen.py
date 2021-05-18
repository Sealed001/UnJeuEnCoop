import yaml
import pygame as py

class HomeScreen:
	_properties = {}

	def __init__(self):
		with open("homeScreen.yml", 'r') as file:
			self._properties = yaml.safe_load(file)

	def update(self, dt):
		pass

	def draw(self, screen):
		pass