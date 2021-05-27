import os
import yaml
import pygame as py
from Levels import levels

class LocalPlay:
	_parameters = {}
	_vars = {
		"level": None
	}

	def __init__(self, parameters):
		self._parameters = parameters
		self._vars["level"] = self._parameters["level"]["level"](players=parameters["players"])

	def update(self, dt, game):
		pass

	def draw(self, screen, transition, inTransition, timeTransition):
		w, h = py.display.get_surface().get_size()

		screen.blit(self._vars["level"].getSurface(w, h), (0, 0))

		if (inTransition):
			screen.blit(transition.getSurface(w, h, timeTransition), (0, 0))

		py.display.flip()