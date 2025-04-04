import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle settings
paddle_width, paddle_height = 10, 100
paddle_speed = 10

# Ball settings
ball_size = 20
ball_speed_x, ball_speed_y = 5, 5

# Initialize paddles and ball
left_paddle = pygame.Rect(10, height//2 - paddle_height//2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 20, height//2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(width//2 - ball_size//2, height//2 - ball_size//2, ball_size, ball_size)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= width:
        ball.x, ball.y = width//2 - ball_size//2, height//2 - ball_size//2
        ball_speed_x *= -1

    # Fill screen
    window.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(window, white, left_paddle)
    pygame.draw.rect(window, white, right_paddle)
    pygame.draw.ellipse(window, white, ball)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()