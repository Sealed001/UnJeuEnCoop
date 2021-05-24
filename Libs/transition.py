import os
import pygame as py
import yaml

transitionProperties = {}
with open(f"{os.path.dirname(__file__)}/transition.yml", 'r') as file:
	transitionProperties = yaml.safe_load(file)

# Easing functions
def LINEAR(x: float) -> float:
	return x

def EASEINCUBIC(x: float) -> float:
	return pow(x, 3)

def EASEOUTCUBIC(x: float) -> float:
	return 1 - pow(1 - x, 3)

def EASEINOUTCUBIC(x: float) -> float:
	if (x < 0.5):
		return 4 * pow(x, 3)
	else:
		return 1 - pow(-2 * x + 2, 3) / 2

# Transitions
class GrowingDotsTransition:
	_easingFunc = None

	def __init__(self, easingFunc = LINEAR):
		self._easingFunc = easingFunc

	def getSurface(self, width: int, height: int, t: float):
		transitionSurface = py.Surface((width, height), py.SRCALPHA, 32)

		if (t <= 0.5):
			easedT = self._easingFunc(t * 2)
			transitionPosition = int((easedT * (width + transitionProperties["growingDots"]["transitionWidth"] + 4)) - transitionProperties["growingDots"]["transitionWidth"])

			py.draw.rect(transitionSurface, tuple(transitionProperties["growingDots"]["color"]), py.Rect(0, 0, transitionPosition, height))
			
			lineNumber = 0
			for localY in range(-transitionProperties["growingDots"]["size"], height + transitionProperties["growingDots"]["size"], transitionProperties["growingDots"]["size"]):
				lineNumber += 1
				for x in range(-transitionProperties["growingDots"]["size"], width + transitionProperties["growingDots"]["size"], transitionProperties["growingDots"]["size"] * 2):
					if ((transitionPosition - transitionProperties["growingDots"]["size"] * 2) < x < (transitionPosition + transitionProperties["growingDots"]["transitionWidth"])):
						localX = x + (lineNumber % 2) *  transitionProperties["growingDots"]["size"]
						localT = 0
						if (localX <= transitionPosition):
							localT = 1
						elif (localX <= (transitionPosition + transitionProperties["growingDots"]["transitionWidth"])): 
							localT = 1 - (localX - transitionPosition) / transitionProperties["growingDots"]["transitionWidth"]

						if (localT > 0):
							py.draw.circle(transitionSurface, tuple(transitionProperties["growingDots"]["color"]), (localX, localY), transitionProperties["growingDots"]["size"] * localT)
		else:
			easedT = self._easingFunc((t - 0.5) * 2)
			transitionPosition = int((easedT * (width + transitionProperties["growingDots"]["transitionWidth"] + 4)) - transitionProperties["growingDots"]["transitionWidth"] - 4)

			py.draw.rect(transitionSurface, tuple(transitionProperties["growingDots"]["color"]), py.Rect(transitionPosition + transitionProperties["growingDots"]["transitionWidth"], 0, width - (transitionPosition + transitionProperties["growingDots"]["transitionWidth"]), height))
			
			lineNumber = 0
			for localY in range(-transitionProperties["growingDots"]["size"], height + transitionProperties["growingDots"]["size"], transitionProperties["growingDots"]["size"]):
				lineNumber += 1
				for x in range(-transitionProperties["growingDots"]["size"], width + transitionProperties["growingDots"]["size"], transitionProperties["growingDots"]["size"] * 2):
					if (transitionPosition < x < (transitionPosition + transitionProperties["growingDots"]["transitionWidth"] + transitionProperties["growingDots"]["size"] * 2)):
						localX = x + (lineNumber % 2) *  transitionProperties["growingDots"]["size"]
						localT = 0
						if (localX >= (transitionPosition + transitionProperties["growingDots"]["transitionWidth"])):
							localT = 1
						elif (localX >= transitionPosition):
							localT = (localX - transitionPosition) / transitionProperties["growingDots"]["transitionWidth"]

						if (localT > 0):
							py.draw.circle(transitionSurface, tuple(transitionProperties["growingDots"]["color"]), (localX, localY), transitionProperties["growingDots"]["size"] * localT)

		return transitionSurface