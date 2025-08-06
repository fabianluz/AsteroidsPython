import pygame
import random
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfile import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)    
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                        random_angle = random.uniform(20, 50)
                        new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
                        
                        v1 = asteroid.velocity.rotate(random_angle) * 1.2
                        new_asteroid1 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                        new_asteroid1.velocity = v1
                        
                        v2 = asteroid.velocity.rotate(-random_angle) * 1.2
                        new_asteroid2 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                        new_asteroid2.velocity = v2

                    asteroid.kill()

        screen.fill("black")    
        for drawable_Thing in drawable:
            drawable_Thing.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60)/1000)



if __name__ == "__main__":
    main()
