import pygame
from constants import *
from entities import Entity, Ant

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ant Foraging Simulation")
    clock = pygame.time.Clock()

    food = Entity(FOOD_POSITION, FOOD_SIZE, FOOD_COLOR)
    nest = Entity(NEST_POSITION, NEST_SIZE, NEST_COLOR)
    ants = [Ant(NEST_POSITION, ANT_SIZE, ANT_COLOR, 5) for _ in range(NUM_ANTS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        food.draw(screen)
        nest.draw(screen)
        for ant in ants:
            ant.move(food, nest, ants)  # Pass the entire ants list here
            ant.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()