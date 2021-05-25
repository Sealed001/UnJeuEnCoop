from .boyfriend import Boyfriend
import pygame as py
import os

characters = [{"name": "Boyfriend", "character": Boyfriend, "preview": py.image.load(f"{os.path.dirname(__file__)}/../Assets/Characters/Boyfriend/preview.png")}]