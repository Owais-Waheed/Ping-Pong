import pygame

# Create the scores
player1_score = 0
player2_score = 0

#Create restart condition
game_restart = False

# Create the winning score
winning_score = 5

# Initialize pygame
pygame.init()

# Set the window size
size = (1100, 700)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Pong Game")

# Define colors
white = (255, 255, 255)

#Create Flash Screen
def flash_screen():
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw a message on the screen
    font = pygame.font.Font(None, 30)
    text = font.render("Press any key to start the game", True, white)
    screen.blit(text, (size[0]//2 - text.get_width()//2, size[1]//2 - text.get_height()//2))

    # Update the screen
    pygame.display.flip()

    # Wait for a key press
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            return




# Create the ball
ball_radius = 20
ball_color = white
ball_x = size[0] // 2
ball_y = size[1] // 2
ball_speed_x = 7
ball_speed_y = 7

# Create the paddles
paddle_width = 20
paddle_height = 100
paddle1_x = 10
paddle2_x = size[0] - paddle_width - 10
paddle1_y = (size[1] - paddle_height) // 2
paddle2_y = (size[1] - paddle_height) // 2
paddle_speed = 5

# Create a clock
clock = pygame.time.Clock()

# Create the game loop
running = True
# calling the function before starting the game loop
flash_screen()

# Handle events


while running:
    # Handle events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill((0, 0, 0))


    # Move the ball


    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed


    # keeping paddle inside screen.
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y + paddle_height > size[1]:
        paddle1_y = size[1] - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y + paddle_height > size[1]:
        paddle2_y = size[1] - paddle_height



    # Check for collisions with the walls
    if ball_y + ball_radius >= size[1] or ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y
    if ball_x + ball_radius >= size[0]:
        player1_score+=1
        ball_speed_x = -ball_speed_x
    if ball_x - ball_radius <= 0:
        player2_score += 1
        ball_speed_x = -ball_speed_x

    # Check for collisions with the paddles
    if (ball_x - ball_radius <= paddle1_x + paddle_width and
           ball_y + ball_radius >= paddle1_y and
            ball_y - ball_radius <= paddle1_y + paddle_height ):
         
        ball_speed_x = -ball_speed_x
        if(ball_y + ball_radius >= paddle1_y and
            ball_y - ball_radius >= paddle1_y + paddle_height//2):
            ball_speed_y = -ball_speed_y
        


    if (ball_x + ball_radius >= paddle2_x and
            ball_y + ball_radius >= paddle2_y and
            ball_y - ball_radius <= paddle2_y + paddle_height):
        ball_speed_x = -ball_speed_x
        if(ball_y + ball_radius >= paddle2_y and
            ball_y - ball_radius >= paddle2_y + paddle_height//2):
            ball_speed_y = -ball_speed_y
        
        

    # Check win condition.
    if player1_score == winning_score:
        # Draw a message on the screen
        font = pygame.font.Font(None, 30)
        text = font.render("Player 1 wins", True, white)
        screen.blit(text, (size[0]//2 - text.get_width()//2, size[1]//2 - text.get_height()//2))
        restart_text = font.render("Press R to restart", True, white)
        screen.blit(restart_text, (size[0]//2 - restart_text.get_width()//2, size[1]//2 - text.get_height()//2 + 50))
        pygame.display.flip()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
        # Restart the game
                    player1_score = 0
                    player2_score = 0
                    ball_x = size[0] // 2
                    ball_y = size[1] // 2
                    game_restart == False
                    break

    elif player2_score == winning_score:
        # Draw a message on the screen
        font = pygame.font.Font(None, 30)
        text = font.render("Player 2 wins", True, white)
        screen.blit(text, (size[0]//2 - text.get_width()//2, size[1]//2 - text.get_height()//2))
        restart_text = font.render("Press R to restart", True, white)
        screen.blit(restart_text, (size[0]//2 - restart_text.get_width()//2, size[1]//2 - text.get_height()//2 + 50))
        pygame.display.flip()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
        # Restart the game
                    player1_score = 0
                    player2_score = 0
                    ball_x = size[0] // 2
                    ball_y = size[1] // 2
                    game_restart == False
                    break
    
 

    # Draw the ball and the paddles
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    
    # Draw the scores
    font = pygame.font.Font(None, 30)
    player1_text = font.render(f"Player 1: {player1_score}", True, white)
    player2_text = font.render(f"Player 2: {player2_score}", True, white)
    screen.blit(player1_text, (10, 10))
    screen.blit(player2_text, (size[0]-player2_text.get_width()-10, 10))

    pygame.display.update()


    # Control the game speed
    clock.tick(60)

# Quit pygame
pygame.quit()
