import os
import pygame as py
import yaml

uiProperties = {}
with open(f"{os.path.dirname(__file__)}/ui.yml", 'r') as file:
	uiProperties = yaml.safe_load(file)

def BigButton(width, height, backgroundColor, backgroundColorIcon, icon, text):
	btnSurface = py.Surface((width, height), py.SRCALPHA, 32)

	py.draw.rect(btnSurface, backgroundColor, py.Rect(0, 0, width, height), 0, uiProperties["bigButton"]["roundCornerRadius"])
	py.draw.rect(btnSurface, backgroundColorIcon,(uiProperties["bigButton"]["iconBackgroundGap"], uiProperties["bigButton"]["iconBackgroundGap"], height - uiProperties["bigButton"]["iconBackgroundGap"] * 2, height - uiProperties["bigButton"]["iconBackgroundGap"] * 2), 0, uiProperties["bigButton"]["roundCornerRadius"])

	if (icon != None):
		iconSize = int(height - (uiProperties["bigButton"]["iconBackgroundGap"] + uiProperties["bigButton"]["iconGap"]) * 2)
		btnSurface.blit(py.transform.scale(icon, (iconSize, iconSize)), (uiProperties["bigButton"]["iconBackgroundGap"] + uiProperties["bigButton"]["iconGap"], uiProperties["bigButton"]["iconBackgroundGap"] + uiProperties["bigButton"]["iconGap"]))
	
	if (text != None):
		textW = int(width - height - uiProperties["bigButton"]["iconBackgroundGap"] * 4)
		textH = int((textW / text.get_width()) * text.get_height())
		textScaled = py.transform.scale(text, (textW, textH))

		textX = height + (width - height - uiProperties["bigButton"]["iconBackgroundGap"]) / 2 - textScaled.get_width() / 2
		textY = height / 2 - textScaled.get_height() / 2
		btnSurface.blit(textScaled, (textX, textY))

	return btnSurface

def CharacterContainer(width, height):
	characterContainerSurface = py.Surface((width, height), py.SRCALPHA, 32)

	py.draw.rect(characterContainerSurface, tuple(uiProperties["characterContainer"]["color"]), py.Rect(0, 0, width, height), 0, uiProperties["characterContainer"]["roundCornerRadius"])

	return characterContainerSurface

def CharacterContainerSelector(width, height):
	characterContainerSurface = py.Surface((width, height), py.SRCALPHA, 32)

	py.draw.rect(characterContainerSurface, (255, 255, 255), py.Rect(0, 0, width, height), 3, uiProperties["characterContainer"]["roundCornerRadius"])

	return characterContainerSurface