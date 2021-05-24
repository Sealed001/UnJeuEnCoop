import os
import yaml
import pygame as py
#from .ui import BigButton

class Options:
	_properties = {}
	_images = {}
	_vars = {
		"background":{
			"offset": 0
		},
		"buttons": {
			"selected": "local",
			"selector": {
				"isMoving": True,
				"position": {
					"x": 0,
					"y": 0
				},
				"targetPosition": {
					"x": 0,
					"y": 0
				},
				"size": {
					"width": 0,
					"height": 0
				},
				"targetSize": {
					"width": 0,
					"height": 0
				}
			}
		}
	}

	def __init__(self, parameters):
		with open(f"{os.path.dirname(__file__)}/options.yml", 'r') as file:
			self._properties = yaml.safe_load(file)
		
		# Background Tile
		self._images["backgroundTileGreen"] = py.image.load(f"{os.path.dirname(__file__)}/../Assets/Backgrounds/backgroundTileGreen.png")

		# Selector
		#w, h = py.display.get_surface().get_size()
		#self._vars["buttons"]["selector"]["size"]["width"] = w - self._properties["buttons"]["selector"]["width"] * 2 - self._properties["buttons"]["selector"]["buttonGap"] * 2
		#self._vars["buttons"]["selector"]["size"]["height"] = h - self._properties["alphaClip"]["height"] * 2 - self._properties["buttons"]["selector"]["width"] * 2 - self._properties["buttons"]["selector"]["buttonGap"] * 2
		#self._vars["buttons"]["selector"]["position"]["x"] = (w - self._vars["buttons"]["selector"]["size"]["width"]) / 2
		#self._vars["buttons"]["selector"]["position"]["y"] = (h - self._vars["buttons"]["selector"]["size"]["height"]) / 2

	def update(self, dt, game):
		self._vars["background"]["offset"] += dt * self._properties["background"]["speed"]
		if (self._vars["background"]["offset"] >= self._images["backgroundTileGreen"].get_width()):
			self._vars["background"]["offset"] -= self._images["backgroundTileGreen"].get_width()
		
		#keysPressed = py.key.get_pressed()
		#if (not(self._vars["buttons"]["selector"]["isMoving"])):
		#	if (keysPressed[py.K_RIGHT]):
		#		if (self._vars["buttons"]["selected"] == "local"):
		#			self._vars["buttons"]["selected"] = "options"
		#		elif (self._vars["buttons"]["selected"] == "online"):
		#			self._vars["buttons"]["selected"] = "quit"
		#	if (keysPressed[py.K_LEFT]):
		#		if (self._vars["buttons"]["selected"] == "options"):
		#			self._vars["buttons"]["selected"] = "local"
		#		elif (self._vars["buttons"]["selected"] == "quit"):
		#			self._vars["buttons"]["selected"] = "online"
		#	if (keysPressed[py.K_DOWN]):
		#		if (self._vars["buttons"]["selected"] == "local"):
		#			self._vars["buttons"]["selected"] = "online"
		#		elif (self._vars["buttons"]["selected"] == "options"):
		#			self._vars["buttons"]["selected"] = "quit"
		#	if (keysPressed[py.K_UP]):
		#		if (self._vars["buttons"]["selected"] == "online"):
		#			self._vars["buttons"]["selected"] = "local"
		#		elif (self._vars["buttons"]["selected"] == "quit"):
		#			self._vars["buttons"]["selected"] = "options"
		#if (keysPressed[py.K_RETURN]):
		#	if (self._vars["buttons"]["selected"] == "quit"):
		#		game.on = False

		# Selector Target Size & Position
		# w, h = py.display.get_surface().get_size()
		# self._vars["buttons"]["selector"]["targetSize"]["width"] = (w / 2) - self._properties["buttons"]["gap"] * 2 + (self._properties["buttons"]["selector"]["width"] + self._properties["buttons"]["selector"]["buttonGap"]) * 2
		# self._vars["buttons"]["selector"]["targetSize"]["height"] = ((h - self._properties["alphaClip"]["height"] * 2) / 2) - self._properties["buttons"]["gap"] * 2 + (self._properties["buttons"]["selector"]["width"] + self._properties["buttons"]["selector"]["buttonGap"]) * 2
		# if (self._vars["buttons"]["selected"] == "local"):
		# 	self._vars["buttons"]["selector"]["targetPosition"]["x"] = self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# 	self._vars["buttons"]["selector"]["targetPosition"]["y"] = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# elif (self._vars["buttons"]["selected"] == "online"):
		# 	self._vars["buttons"]["selector"]["targetPosition"]["x"] = self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# 	self._vars["buttons"]["selector"]["targetPosition"]["y"] = (h / 2) + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# elif (self._vars["buttons"]["selected"] == "quit"):
		# 	self._vars["buttons"]["selector"]["targetPosition"]["x"] = (w / 2) + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# 	self._vars["buttons"]["selector"]["targetPosition"]["y"] = (h / 2) + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# elif (self._vars["buttons"]["selected"] == "options"):
		# 	self._vars["buttons"]["selector"]["targetPosition"]["x"] = (w / 2) + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]
		# 	self._vars["buttons"]["selector"]["targetPosition"]["y"] = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"] - self._properties["buttons"]["selector"]["width"] - self._properties["buttons"]["selector"]["buttonGap"]

		# Selector Size & Position
		# hasMoved = False
		# if (self._vars["buttons"]["selector"]["position"]["x"] > self._vars["buttons"]["selector"]["targetPosition"]["x"]):
		# 	self._vars["buttons"]["selector"]["position"]["x"] = max(self._vars["buttons"]["selector"]["position"]["x"] - self._properties["buttons"]["selector"]["positionSpeed"] * dt, self._vars["buttons"]["selector"]["targetPosition"]["x"])
		# 	hasMoved = True
		# elif (self._vars["buttons"]["selector"]["position"]["x"] < self._vars["buttons"]["selector"]["targetPosition"]["x"]):
		# 	self._vars["buttons"]["selector"]["position"]["x"] = min(self._vars["buttons"]["selector"]["position"]["x"] + self._properties["buttons"]["selector"]["positionSpeed"] * dt, self._vars["buttons"]["selector"]["targetPosition"]["x"])
		# 	hasMoved = True

		# if (self._vars["buttons"]["selector"]["position"]["y"] > self._vars["buttons"]["selector"]["targetPosition"]["y"]):
		# 	self._vars["buttons"]["selector"]["position"]["y"] = max(self._vars["buttons"]["selector"]["position"]["y"] - self._properties["buttons"]["selector"]["positionSpeed"] * dt, self._vars["buttons"]["selector"]["targetPosition"]["y"])
		# 	hasMoved = True
		# elif (self._vars["buttons"]["selector"]["position"]["y"] < self._vars["buttons"]["selector"]["targetPosition"]["y"]):
		# 	self._vars["buttons"]["selector"]["position"]["y"] = min(self._vars["buttons"]["selector"]["position"]["y"] + self._properties["buttons"]["selector"]["positionSpeed"] * dt, self._vars["buttons"]["selector"]["targetPosition"]["y"])
		# 	hasMoved = True

		# if (self._vars["buttons"]["selector"]["size"]["width"] > self._vars["buttons"]["selector"]["targetSize"]["width"]):
		# 	self._vars["buttons"]["selector"]["size"]["width"] = max(self._vars["buttons"]["selector"]["size"]["width"] - self._properties["buttons"]["selector"]["scaleSpeed"] * dt, self._vars["buttons"]["selector"]["targetSize"]["width"])
		# 	hasMoved = True
		# elif (self._vars["buttons"]["selector"]["size"]["width"] < self._vars["buttons"]["selector"]["targetSize"]["width"]):
		# 	self._vars["buttons"]["selector"]["size"]["width"] = min(self._vars["buttons"]["selector"]["size"]["width"] + self._properties["buttons"]["selector"]["scaleSpeed"] * dt, self._vars["buttons"]["selector"]["targetSize"]["width"])
		# 	hasMoved = True

		# if (self._vars["buttons"]["selector"]["size"]["height"] > self._vars["buttons"]["selector"]["targetSize"]["height"]):
		# 	self._vars["buttons"]["selector"]["size"]["height"] = max(self._vars["buttons"]["selector"]["size"]["height"] - self._properties["buttons"]["selector"]["scaleSpeed"] * dt, self._vars["buttons"]["selector"]["targetSize"]["height"])
		# 	hasMoved = True
		# elif (self._vars["buttons"]["selector"]["size"]["height"] < self._vars["buttons"]["selector"]["targetSize"]["height"]):
		# 	self._vars["buttons"]["selector"]["size"]["height"] = min(self._vars["buttons"]["selector"]["size"]["height"] + self._properties["buttons"]["selector"]["scaleSpeed"] * dt, self._vars["buttons"]["selector"]["targetSize"]["height"])
		# 	hasMoved = True
		# self._vars["buttons"]["selector"]["isMoving"] = hasMoved

	def draw(self, screen, transition, inTransition, timeTransition):
		w, h = py.display.get_surface().get_size()

		# Background
		screen.fill(tuple(self._properties["background"]["color"]))
		for x in range(-self._images["backgroundTileGreen"].get_width(), w + self._images["backgroundTileGreen"].get_width(), self._images["backgroundTileGreen"].get_width()):
			for y in range(-self._images["backgroundTileGreen"].get_height(), h + self._images["backgroundTileGreen"].get_height(), self._images["backgroundTileGreen"].get_height()):
				screen.blit(self._images["backgroundTileGreen"], (x - self._vars["background"]["offset"], y + self._vars["background"]["offset"]))
		
		# Alpha Clip Surface
		alphaClipSurface = py.Surface((w, self._properties["alphaClip"]["height"]))
		alphaClipSurface.set_alpha(self._properties["alphaClip"]["alpha"])
		alphaClipSurface.fill(tuple(self._properties["alphaClip"]["color"]))
		screen.blit(alphaClipSurface, (0, 0)) # Top alpha clip surface
		screen.blit(alphaClipSurface, (0, h - self._properties["alphaClip"]["height"])) # Bottom alpha clip surface

		# Buttons
		#buttonWidth = (w / 2) - self._properties["buttons"]["gap"] * 2
		#buttonHeight = ((h - self._properties["alphaClip"]["height"] * 2) / 2) - self._properties["buttons"]["gap"] * 2

		# Button Selector
		#py.draw.rect(screen, tuple(self._properties["buttons"]["selector"]["color"]), py.Rect(self._vars["buttons"]["selector"]["position"]["x"], self._vars["buttons"]["selector"]["position"]["y"], self._vars["buttons"]["selector"]["size"]["width"], self._vars["buttons"]["selector"]["size"]["height"]), self._properties["buttons"]["selector"]["width"], self._properties["buttons"]["selector"]["cornerRadius"])

		# Local Button
		#buttonX = self._properties["buttons"]["gap"]
		#buttonY = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"]
		#screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["local"]["color"]["background"]), tuple(self._properties["buttons"]["local"]["color"]["iconBackground"]), self._images["localIcon"], self._images["localText"]), (buttonX, buttonY))

		# Options Button
		#buttonX = (w / 2) + self._properties["buttons"]["gap"]
		#buttonY = self._properties["alphaClip"]["height"] + self._properties["buttons"]["gap"]
		#screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["options"]["color"]["background"]), tuple(self._properties["buttons"]["options"]["color"]["iconBackground"]), self._images["optionsIcon"], self._images["optionsText"]), (buttonX, buttonY))

		# Online Button
		#buttonX = self._properties["buttons"]["gap"]
		#buttonY = self._properties["alphaClip"]["height"] + ((h - self._properties["alphaClip"]["height"] * 2) / 2) + self._properties["buttons"]["gap"]
		#screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["online"]["color"]["background"]), tuple(self._properties["buttons"]["online"]["color"]["iconBackground"]), self._images["onlineIcon"], self._images["onlineText"]), (buttonX, buttonY))

		# Quit Button
		#buttonX = (w / 2) + self._properties["buttons"]["gap"]
		#buttonY = self._properties["alphaClip"]["height"] + ((h - self._properties["alphaClip"]["height"] * 2) / 2) + self._properties["buttons"]["gap"]
		#screen.blit(BigButton(buttonWidth, buttonHeight, tuple(self._properties["buttons"]["quit"]["color"]["background"]), tuple(self._properties["buttons"]["quit"]["color"]["iconBackground"]), self._images["quitIcon"], self._images["quitText"]), (buttonX, buttonY))

		if (inTransition):
			screen.blit(transition.getSurface(w, h, timeTransition), (0, 0))

		py.display.flip()