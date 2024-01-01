import pygame, math, time


class planet_object():
    def __init__(self, scale = int, density = int, position = list, pygame_window = pygame.display):
        self.mass = scale*density*2
        self.scale = scale
        self.position = position
        self.screen = pygame_window
        print(self.mass)
    def update(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.position[0], self.position[1]), self.scale)

class orbit_object():
    def __init__(self, planet_reference, position = list, speed = float, pygame_window = pygame.display):
        self.orbit_coords = planet_reference.position

        self.position = position

        self.speed = speed/1000

        self.distance = planet_reference.mass/(speed/4)

        self.screen = pygame_window
        
        # Calculate direction
        dx = position[0] - planet_reference.position[0]
        dy = position[1] - planet_reference.position[1]

        rads = math.atan2(-dy,dx)
        rads %= 2*math.pi
        self.dir = math.degrees(rads)
    def update(self):
        x = self.position[0]; y = self.position[1]
        ox = self.orbit_coords[0]; oy = self.orbit_coords[1]
        self.dir += self.speed
        #distance = math.sqrt((x-ox)*(x-ox) + (y-oy)*(y-oy))
        self.position = [self.orbit_coords[0] + (math.sin(self.dir)*self.distance), self.orbit_coords[1] + (math.cos(self.dir)*self.distance)]
        pygame.draw.circle(self.screen, (0, 255, 0), (self.position[0], self.position[1]), 10)

class physics_object():
    def __init__(self, position, velocity, scale, density, timescale, pygame_window):
        self.xpos = position[0]
        self.xvel = velocity[0]

        self.ypos = position[1]
        self.yvel = velocity[1]

        self.gravity = 0.8

        self.mass = scale*density*self.gravity*(timescale/10000)

        self.screen = pygame_window
        self.scale = scale
    def update(self, apply_velocity = list):
        self.xvel += apply_velocity[0]
        self.yvel += apply_velocity[1]
        
        pygame.draw.rect(self.screen, (0, 0, 255), (self.xpos, self.ypos, self.scale, self.scale))

        if self.ypos >= 500-self.scale:
            self.yvel = (-1.5/(10000*self.mass))*self.yvel
            self.ypos = 500-self.scale

        if self.xpos >= 500-self.scale or self.xpos <= 0:
            self.xvel = (-1.5/(10000*self.mass))*self.xvel
            self.xpos = 0 if self.xpos <= self.scale else 500-self.scale
        
        self.xpos += self.xvel
        self.ypos += -1*self.yvel

        self.xvel = self.xvel * 0.9999
        self.yvel -= self.gravity * self.mass