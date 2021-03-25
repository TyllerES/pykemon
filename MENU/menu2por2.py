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
button_dim = (width // 2.5, height // 10)
origin = (width // 2, height // 2)

# Criando o primeiro botão:
position1 = (origin[0] - button_dim[0], origin[1] - button_dim[1])
label1 = "FIGHT"
button1 = Button(label1, button_dim, position1, colors)

# Criando o segundo botão:
position2 = (origin[0], origin[1] - button_dim[1])
label2 = "BAG"
button2 = Button(label2, button_dim, position2, colors)

# Criando o terceiro botão:
position3 = (origin[0] - button_dim[0], origin[1])
label3 = "POKEMON"
button3 = Button(label3, button_dim, position3, colors)

# Criando o quarto botão:
position4 = (origin[0], origin[1])
label4 = "RUN"
button4 = Button(label4, button_dim, position4, colors)

buttons = [button1, button2, button3, button4]
positions = [position1, position2, position3, position4]
cursor = 0

running = True
while running:

    # Definindo a posição do cursor:
    cursor_position_shifted = positions[cursor]
    cursor_position = (
        cursor_position_shifted[0] + button_dim[0] // 10,
        cursor_position_shifted[1] + button_dim[1] // 2
    )

    # Capturando eventos:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            break
        if ev.type == pygame.KEYDOWN:

            # Manipulando o cursor:
            if ev.key == pygame.K_RIGHT:
                cursor += 1
            elif ev.key == pygame.K_LEFT:
                cursor -= 1
            elif ev.key == pygame.K_UP:
                cursor -= 2
            elif ev.key == pygame.K_DOWN:
                cursor += 2

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
    pokebola = pygame.image.load('pokebola')
    screen.blit(pokebola, (xcc, ycc))
    pygame.display.update()
pygame.exit()
