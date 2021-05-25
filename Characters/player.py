class Player:
	_position = {"x": 0, "y": 0}
	_speed = {"x": 0, "y": 0}
	_size = {"width": 0, "height": 0}
	_crouchSize = {"width": 0, "height": 0}
	_isCrouched = False

	def __init__(self, x, y, width, crouchWidth, height, crouchHeight):
		self._position = {"x": x, "y": y}
		self._size = {"width": width, "height": height}
		self._crouchSize = {"width": crouchWidth, "height": crouchHeight}