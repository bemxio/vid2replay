import config as cf
import pygame
import pickle
import os

with open("locations.p", "rb") as f:
    locations = list(pickle.load(f))

divider = cf.video_resolution[1] / cf.pygame_resolution[1]
print(divider)
for index, location in enumerate(locations):
    if location:
        location = list(location)
        locations[index] = (location[0] / divider,
                            location[1] / divider,
                            location[2] / divider,
                            location[3] / divider)
    else:
        locations[index] = None

res = cf.pygame_resolution
cursor = pygame.image.load(cf.cursor_path)

pygame.init()
win = pygame.display.set_mode(res)
clock = pygame.time.Clock()

for frame, location in zip(os.listdir(cf.dir_name), locations):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    img = pygame.image.load(f"{cf.dir_name}/" + frame)
    img = pygame.transform.scale(img, res)
    win.blit(img, (0, 0))
    if location:
        pygame.draw.rect(win, (255, 0, 0), location, width=1)

    pygame.display.update()
    clock.tick(cf.fps)
