import pygame
import time
import random
pygame.font.init()

# Window size (X, Y)
WIDTH, HEIGHT = 1000, 800

# Create the window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set a caption or name of the game
pygame.display.set_caption("Space Dodge")

# Background image and scale it to the size of the window
BG = pygame.transform.scale(pygame.image.load("stars.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# Player velocity in pixels
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 12

STAR_VEL = 3

FONT = pygame.font.SysFont("arial", 30) # font name and size

# On this window top-left is coord. 0,0; top right is 0,1000 (because our width); bottom right is 800,1000 (height starts at 0 and goes down); bottom left 800,0
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0)) # asking where to put background image top-left corner
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white") # (string (rounded),1 is anti alias, color)
    WIN.blit(time_text, (10, 10)) # 10, 10 is the position of the time text
    
    pygame.draw.rect(WIN, "yellow", player) # can use RGB as well

    for star in stars: # this makes it apply to every star not just one (like the player)
        pygame.draw.rect(WIN, "brown", star) # if you draw the stars after the player like here they will appear on top of the player, if before then behind the player
    
    pygame.display.update() # just needed to update the screen

def main():
# This will allow us to quit the game by hitting the x button in the top left corner (on Mac) of the game window.
    run = True

    player = pygame.Rect(500, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) # (X,Y,Width,Height) Since it works on top left corners this should put the player at the bottom of the screen
    
    # Depending on the performence of the computer this loop might run faster or slower making the character move faster or slower so this clock bit will stardardize that.
    clock = pygame.time.Clock()

    start_time = time.time() # gets the start time of the loop while time.time() gets the current time
    elapsed_time = 0

    star_add_increment = 2000 # in miliseconds
    star_count = 0

    stars = []
    hit = False
    
    while run:
        star_count += clock.tick(60) # going to run at a max of 60 frames per second, it was just clock.tick(60) before adding the projectiles
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            # use _ as variable when you dont care about the iteration count
            for _ in range(3): # 3 coudl be any number its just how many projectile come on the screen at a time
                star_x = random.randint(0, WIDTH - STAR_WIDTH) # giving the x coordinates for where the stars should materialize
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50) # this makes the stars appear faster as the game goes longer because it is decreasing the star_add_increment as the game progresses from 2000 to 1950 to 1900 etc.
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: # if you wanted to use for isntance the 'a' key it would be .K_a instead of .K_LEFT
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH: # the and player.x .... creates the boundaries so the player can't go off screen
            player.x += PLAYER_VEL
        
        for star in stars[:]: # [:] makes a copy of the stars list so youre working with a copy of the list instead of the actual list
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break 

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2)) # this draws it in the center of the screen
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    
    pygame.quit()

# Don't fully understand but this makes it so we aren't importing the file and are only running this current file.
if __name__ == "__main__":
    main()
