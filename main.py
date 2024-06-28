import pygame
import random

# Initialisation de PyGame
pygame.init()

# Configuration de la fenêtre du jeu
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeu de Devinettes")

# Couleurs
white = (232, 222, 171)
black = (63, 72, 204)
gray = (200, 200, 200)
light_gray = (170, 170, 170)
dark_gray = (100, 100, 100)

# Définir la police et la taille du texte
font = pygame.font.SysFont(None, 55)
input_font = pygame.font.SysFont(None, 45)
button_font = pygame.font.SysFont(None, 45)

# Variables du jeu
number_to_guess = random.randint(1, 100)
guess = None
message = "Devinez un nombre entre 1 et 100"
input_box = pygame.Rect(300, 350, 140, 50)
button_box = pygame.Rect(460, 350, 140, 50)
user_text = ''

# Fonction pour dessiner un bouton
def draw_button(surface, color, rect, text):
    pygame.draw.rect(surface, color, rect)
    text_surface = button_font.render(text, True, black)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_text.isdigit():
                    guess = int(user_text)
                    if guess < number_to_guess:
                        message = f"{guess} est trop petit! Essayez encore."
                    elif guess > number_to_guess:
                        message = f"{guess} est trop grand! Essayez encore."
                    else:
                        message = f"Bravo! Vous avez deviné {number_to_guess}."
                    user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_box.collidepoint(event.pos):
                if user_text.isdigit():
                    guess = int(user_text)
                    if guess < number_to_guess:
                        message = f"{guess} est trop petit! Essayez encore."
                    elif guess > number_to_guess:
                        message = f"{guess} est trop grand! Essayez encore."
                    else:
                        message = f"Bravo! Vous avez deviné {number_to_guess}."
                    user_text = ''

    # Remplir l'écran de blanc
    screen.fill(white)

    # Afficher le message
    text = font.render(message, True, black)
    screen.blit(text, (50, 250))

    # Afficher la boîte de saisie
    pygame.draw.rect(screen, gray, input_box, 2)
    text_surface = input_font.render(user_text, True, black)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    input_box.w = max(200, text_surface.get_width() + 10)

    # Afficher le bouton de validation
    draw_button(screen, light_gray, button_box, "Valider")

    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()
