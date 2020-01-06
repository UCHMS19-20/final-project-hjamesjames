import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (500, 500) )
print(pygame.QUIT)
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():

        # This line will print each event to the terminal
        print(event)

        # Check to see if event is Keydown 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("moving up")
            elif event.key == pygame.K_DOWN:
                print("moving down")
            elif event.key == pygame.K_LEFT:
                print("moving left")
            elif event.key == pygame.K_RIGHT:
                print("moving right")
            elif event.key == pygame.K_z:
                print("selecting")
            elif event.key == pygame.K_x:
                print("cancelling")
            elif event.key == pygame.K_c:
                print("in the menu")
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()