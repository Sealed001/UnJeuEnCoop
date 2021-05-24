import pygame as py

class RouteManager:
	_routes = {}
	_routeName = ""
	_route = None
	_nextRoute = None
	_transition = None
	_inTransition = False
	_timeTransition = 0
	_transitionDuration = 2
	_time = 0
	showFps = False

	def __init__(self, transition, transitionDuration, routes: dict = False, defaultRoute: str = False):
		# Transition
		self._transition = transition
		self._transitionDuration = transitionDuration

		# Set routes
		if (routes == False):
			raise TypeError("Routes is not defined")
		elif (len(routes) > 0):
			self._routes = routes
		else:
			raise TypeError("Routes is empty")
		
		# Set default route
		routeName = ""
		if (defaultRoute == False):
			print(f"Default route is not set, redirecting to {self._routeName}")
			routeName = self._routes.keys()[0]
		elif (self._routeExist(defaultRoute)):
			routeName = defaultRoute
		else:
			print(f"Incorrect default route, redirecting to {self._routeName}")
			routeName = self._routes.keys()[0]
		
		# Initialize default route
		self.go(routeName, wait=False)

		# Initialize clock
		self._time = py.time.get_ticks() / 1000

	def _routeExist(self, route: str):
		return (route in self._routes.keys())

	def go(self, route: str = None, parameters = None, wait: bool = True):
		if (not(self._inTransition)):
			if (route != None):
				if (self._routeExist(route)):
					if (self._routeName != route):
						self._routeName = route
						if (wait):
							self._nextRoute = self._routes[route](parameters)
							self._inTransition = True
						else:
							self._route = self._routes[route](parameters)
					else:
						print("Requirement already satisfied")
				else:
					raise TypeError(f"The route '{route}' doesn't exist")
			else:
				raise TypeError("You really want to go nowhere ?!")

	def update(self, game):
		dt = py.time.get_ticks() / 1000 - self._time
		if (self._inTransition):
			self._timeTransition += dt / self._transitionDuration
			if (self._timeTransition > 0.5):
				if (self._nextRoute != None):
					self._route = self._nextRoute
					self._nextRoute = None
				if (self._timeTransition >= 1):
					self._inTransition = False
					self._timeTransition = 0
		self._time = py.time.get_ticks() / 1000
		if (callable(getattr(self._route, "update", None))):
			self._route.update(dt, game)

		if (self.showFps):
			print(f"{int(1/dt)} fps")

	def draw(self, screen):
		if (callable(getattr(self._route, "draw", None))):
			self._route.draw(screen, self._transition, self._inTransition, self._timeTransition)