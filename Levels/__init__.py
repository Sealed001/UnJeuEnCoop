from .newYork import NewYork
import os
import pygame as py

levels = [{"name": "New York", "preview": py.image.load(f"{os.path.dirname(__file__)}/../Assets/Levels/newyork.png"),"level": NewYork}]