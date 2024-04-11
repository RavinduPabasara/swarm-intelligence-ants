import numpy as np
import pygame
from constants import *

class Entity:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, self.size, self.size))

class Ant(Entity):
    def __init__(self, position, size, color, perception_range):
        super().__init__(position, size, color)
        self.perception_range = perception_range
        self.carrying_food = False
        self.pheromone_trail = []

    def move(self, food, nest, ants):  # Add ants as a parameter here
        if self.carrying_food:
            self.move_to(nest.position)
            if self.position == nest.position:
                self.carrying_food = False
                self.color = ANT_COLOR
                self.pheromone_trail = []
        elif np.linalg.norm(np.array(self.position) - np.array(food.position)) <= self.perception_range:
            self.carrying_food = True
            self.color = CARRYING_FOOD_COLOR
            self.move_to(food.position)
            self.pheromone_trail.append(self.position)
        else:
            self.follow_pheromone(ants) or self.explore()  # Pass ants to follow_pheromone

    def move_to(self, target_position):
        direction = np.sign(np.array(target_position) - np.array(self.position))
        self.position = tuple(np.array(self.position) + direction)

    def explore(self):
        self.position = tuple(np.clip(np.array(self.position) + np.random.randint(-1, 2, 2), 0, WORLD_SIZE - 1))

    def follow_pheromone(self, ants):  # Add ants as a parameter here
        for ant in ants:
            if ant.pheromone_trail and np.linalg.norm(np.array(self.position) - np.array(ant.pheromone_trail[0])) <= self.perception_range:
                self.move_to(ant.pheromone_trail[0])
                return True
        return False

