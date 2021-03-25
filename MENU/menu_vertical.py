import pygame
from button import Button

def draw_button(screen, button, bg_color, font, highlighted=False):
    if highlighted:
        pygame.draw.rect(screen, button.alternative_color, button.rect)
    else:
        pygame.draw.rect(screen, button.main_color, button.rect)
    pygame.draw.rect(screen, bg_color, button.rect, 2)
    text = font.render(button.label, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (
        button.offset[0] + button.size[0] // 2,
        button.offset[1] + button.size[1] // 2
    )
    #text_size = (text.get_width(), text.get_height())
    screen.blit(text, text_rect)#button.text_offset(text_size))

# Inicializando pygame:
pygame.init()

# Configurando a tela:
bg_color = (255, 255, 255)
res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Menu Pykemon")
width = screen.get_width()
height = screen.get_height()
# Importando a fonte:
font = pygame.font.Font('fontePygame.ttf', height // 20)

# Configurações globais de botões:
colors = ((55, 55, 55), (109, 0, 0))
button_dim = (width // 2, height // 7)
origin = (width // 2, height // 2.5)

# Criando o primeiro botão:
position1 = (origin[0] - button_dim[0] // 2, origin[1] - button_dim[1] * 2)
label1 = "Pikachu"
button1 = Button(label1, button_dim, position1, colors)

# Criando o segundo botão:
position2 = (origin[0] - button_dim[0] // 2, origin[1] - button_dim[1])
label2 = "Charmander"
button2 = Button(label2, button_dim, position2, colors)

# Criando o terceiro botão:
position3 = (origin[0] - button_dim[0] // 2, origin[1])
label3 = "Squirtle"
button3 = Button(label3, button_dim, position3, colors)

# Criando o quarto botão:
position4 = (origin[0] - button_dim[0] // 2, origin[1] + button_dim[1])
label4 = "Dragonite"
button4 = Button(label4, button_dim, position4, colors)

# Criando o quinto botão:
position5 = (origin[0] - button_dim[0] // 2, origin[1] + button_dim[1] * 2)
label5 = "MewTwo"
button5 = Button(label5, button_dim, position5, colors)

buttons = [button1, button2, button3, button4, button5]
positions = [position1, position2, position3, position4, position5]
cursor = 0

running = True
while running:

    # Definindo a posição do cursor:
    cursor_position_shifted = positions[cursor]
    cursor_position = (
        cursor_position_shifted[0] + button_dim[0] // 20,
        cursor_position_shifted[1] + button_dim[1] // 2
    )

    # Capturando eventos:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            break
        if ev.type == pygame.KEYDOWN:

            # Manipulando o cursor:
            if ev.key == pygame.K_UP:
                cursor -= 1
            elif ev.key == pygame.K_DOWN:
                cursor += 1

            # Verificando os limites do cursor:
            if cursor >= len(positions):
                cursor -= len(positions)
            elif cursor < 0:
                cursor += len(positions)
            
            if ev.key == pygame.K_RETURN:
                for button in buttons:
                    if cursor_position in button:
                        print(button.label)

    screen.fill(bg_color)

    for button in buttons:
        if cursor_position in button:
            draw_button(screen, button, bg_color, font, True)
        else:
            draw_button(screen, button, bg_color, font)

    # Exibindo o cursor:
    sc = 16
    xcc, ycc = cursor_position
    x0c, y0c = xcc - sc // 2, ycc - sc // 2
    x1c, y1c = xcc + sc // 2, ycc + sc // 2
    pygame.draw.polygon(
        screen, (255, 255, 255),
        [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
    )
    pygame.display.update()

pygame.quit()
