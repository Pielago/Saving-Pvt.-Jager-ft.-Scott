import pygame
import math
from Functions import constrain


class Scott(pygame.sprite.Sprite):
    # Create player
    def __init__(self, screen):

        pygame.sprite.Sprite.__init__(self)

        # Sets the image
        self.image = pygame.image.load("SC.PNG").convert()
        # Sets the initial location
        self.center = (650, 300)
        self.width, self.height = screen.get_size()
        # Creates a rect at location
        self.rect = self.image.get_rect(center=self.center)
        # Defines how fast movement is
        self.step = 5
        # self.angle = self.get_angle(py.mouse.get_pos())

    def get_angle(self, mouse):
        # Find angle between center of player and mouse location
        offset = (self.rect.centerx - mouse[0], self.rect.centery - mouse[1])
        self.angle = math.degrees(math.atan2(offset[0], offset[1])) - 135

    def update(self):
        # Movement
        # Constrain is present to keep the player from moving out of bounds
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.step
            self.rect.centerx = constrain(self.rect.centerx, 0, self.width - self.step)
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= self.step
            self.rect.centerx = constrain(self.rect.centerx, 0, self.width - self.step)
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= self.step
            self.rect.centery = constrain(self.rect.centery, 0, self.height - self.step)
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += self.step
            self.rect.centery = constrain(self.rect.centery, 0, self.height - self.step)

    def get_event(self, event, bulletList):
        # Check for mouse button pressed (left)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bulletList.add(Bullet(self.rect.center, self.angle))
        # Check for mouse movement
        if event.type == pygame.MOUSEMOTION:
            self.get_angle(event.pos)

    def draw(self, surface):
        # Draw image
        surface.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    # Class for bullets
    def __init__(self, location, angle):

        pygame.sprite.Sprite.__init__(self)

        # Creates bullet
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 0, 0))
        # Calculates angle based off of angle from Player class
        self.angle = -math.radians(angle-135)
        # Create a rect at the center of location
        self.rect = self.image.get_rect(center=location)
        # Speed magnitude (can change for faster bullet)
        self.speed_magnitude = 10
        # Determines speed based off of angles
        self.speed = (self.speed_magnitude*math.cos(self.angle), self.speed_magnitude*math.sin(self.angle))
        self.screen_rect = pygame.display.get_surface().get_rect()

    def update(self, screen_rect):
        # Add speed to coordinates for movement of bullet
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        # New coordinates
        self.rect.topleft = [self.rect.x, self.rect.y]
        # Bullets that have left the screen will be removed from the sprite group
        self.remove(screen_rect)

    def remove(self, screen_rect):
        # Removes bullet from screen
        if not self.rect.colliderect(screen_rect):
            self.kill()


class Jager(pygame.sprite.Sprite):
    # Create Jager
    def __init__(self, screen):

        pygame.sprite.Sprite.__init__(self)
        # Sets the image
        self.image = pygame.image.load("Jager.PNG").convert()
        # Sets the initial location
        self.center = (650, 500)
        self.width, self.height = screen.get_size()
        # Creates a rect at location
        self.rect = self.image.get_rect(center=self.center)

    def draw(self, surface):
        # Draw image
        surface.blit(self.image, self.rect)