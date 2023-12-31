import package, pygame

pygame.init()

window = pygame.display.set_mode([500, 500])

running = True

planet = package.planet_object(25, 1, [250, 250], window)
moon = package.orbit_object(planet, [250, 150], 1, window)
moon2 = package.orbit_object(planet, [350, 250], 1, window)

cube = package.physics_object([250, 250], [1, 0], 25, 1, 1, window)

cube_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cube_y = 1
                


    window.fill((255, 255, 255))

    planet.update()
    moon.update()
    moon2.update()
    cube.update([0, cube_y])

    pygame.display.flip()
    if cube_y >= 1:
        cube_y = 0

pygame.quit()