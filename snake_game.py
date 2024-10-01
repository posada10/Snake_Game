import pygame  # Importa la librería pygame
import random  # Importa la librería random

pygame.init()  # Inicializa todos los módulos de pygame

# Colores definidos en formato RGB
blanco = (255, 255, 255)  # Color blanco
negro = (0, 0, 0)  # Color negro
rojo = (213, 50, 80)  # Color rojo
verde = (0, 255, 0)  # Color verde
azul = (50, 153, 213)  # Color azul

# Dimensiones de la pantalla
ancho = 800  # Ancho de la pantalla
alto = 600  # Alto de la pantalla

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ancho, alto))  # Crea una ventana con las dimensiones especificadas
pygame.display.set_caption('Juego de la Culebrita')  # Establece el título de la ventana

reloj = pygame.time.Clock()  # Crea un objeto Clock para controlar el tiempo

# Tamaño de cada cuadro de la culebra y su velocidad
tamaño_cuadro = 10  # Tamaño de cada segmento de la culebra
velocidad_culebra = 15  # Velocidad de la culebra

# Fuente para los mensajes en pantalla
fuente = pygame.font.SysFont("bahnschrift", 25)  # Fuente bahnschrift de tamaño 25

# Función para mostrar mensajes en pantalla
def mensaje(msg, color):
    mesg = fuente.render(msg, True, color)  # Renderiza el mensaje con la fuente y color especificados
    pantalla.blit(mesg, [ancho / 6, alto / 3])  # Dibuja el mensaje en la pantalla en la posición especificada

# Función principal del juego
def juego():
    game_over = False  # Variable para controlar el estado del juego
    game_cerrado = False  # Variable para controlar si el juego está cerrado

    # Posición inicial de la culebra
    x1 = ancho / 2  # Posición x inicial
    y1 = alto / 2  # Posición y inicial

    # Cambio en la posición de la culebra
    x1_cambio = 0  # Cambio en la posición x
    y1_cambio = 0  # Cambio en la posición y

    culebra_lista = []  # Lista para almacenar los segmentos de la culebra
    largo_culebra = 1  # Longitud inicial de la culebra

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0  # Posición x de la comida
    comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0  # Posición y de la comida

    # Posición inicial de la comida grande
    comida_grande_x = round(random.randrange(0, ancho - tamaño_cuadro * 2) / 10.0) * 10.0  # Posición x de la comida grande
    comida_grande_y = round(random.randrange(0, alto - tamaño_cuadro * 2) / 10.0) * 10.0  # Posición y de la comida grande

    # Variables para el puntaje
    score = 0  # Puntaje inicial
    comida_seguida = 0  # Contador de comida seguida

    # Bucle principal del juego
    while not game_over:

        # Bucle para cuando el juego está cerrado
        while game_cerrado == True:
            pantalla.fill(negro)  # Llena la pantalla de color negro
            mensaje("Perdiste! Presiona Q para salir o C para jugar de nuevo", rojo)  # Muestra el mensaje de pérdida
            pygame.display.update()  # Actualiza la pantalla

            # Bucle para eventos
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
                    if evento.key == pygame.K_q:  # Si la tecla es 'Q'
                        game_over = True  # Termina el juego
                        game_cerrado = False  # Cierra el estado de juego cerrado
                    if evento.key == pygame.K_c:  # Si la tecla es 'C'
                        juego()  # Reinicia el juego

        # Bucle para eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si se cierra la ventana
                game_over = True  # Termina el juego
            if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if evento.key == pygame.K_LEFT:  # Si la tecla es la flecha izquierda
                    x1_cambio = -tamaño_cuadro  # Cambia la posición x hacia la izquierda
                    y1_cambio = 0  # No cambia la posición y
                elif evento.key == pygame.K_RIGHT:  # Si la tecla es la flecha derecha
                    x1_cambio = tamaño_cuadro  # Cambia la posición x hacia la derecha
                    y1_cambio = 0  # No cambia la posición y
                elif evento.key == pygame.K_UP:  # Si la tecla es la flecha arriba
                    y1_cambio = -tamaño_cuadro  # Cambia la posición y hacia arriba
                    x1_cambio = 0  # No cambia la posición x
                elif evento.key == pygame.K_DOWN:  # Si la tecla es la flecha abajo
                    y1_cambio = tamaño_cuadro  # Cambia la posición y hacia abajo
                    x1_cambio = 0  # No cambia la posición x

        # Verifica si la culebra choca con los bordes de la pantalla
        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_cerrado = True  # Activa el estado de juego cerrado
        x1 += x1_cambio  # Actualiza la posición x de la culebra
        y1 += y1_cambio  # Actualiza la posición y de la culebra
        pantalla.fill(azul)  # Llena la pantalla de color azul
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_cuadro, tamaño_cuadro])  # Dibuja la comida
        pygame.draw.rect(pantalla, rojo, [comida_grande_x, comida_grande_y, tamaño_cuadro * 2, tamaño_cuadro * 2])  # Dibuja la comida grande

        # Actualiza la lista de segmentos de la culebra
        culebra_cabeza = []  # Lista para la cabeza de la culebra
        culebra_cabeza.append(x1)  # Añade la posición x de la cabeza
        culebra_cabeza.append(y1)  # Añade la posición y de la cabeza
        culebra_lista.append(culebra_cabeza)  # Añade la cabeza a la lista de segmentos
        if len(culebra_lista) > largo_culebra:  # Si la longitud de la lista es mayor que la longitud de la culebra
            del culebra_lista[0]  # Elimina el primer segmento de la lista

        # Verifica si la culebra choca consigo misma
        for x in culebra_lista[:-1]:
            if x == culebra_cabeza:
                game_cerrado = True  # Activa el estado de juego cerrado

        # Dibuja la culebra
        for i, x in enumerate(culebra_lista):
            color = rojo if i % 2 == 0 else negro  # Alterna el color entre rojo y negro
            pygame.draw.rect(pantalla, color, [x[0], x[1], tamaño_cuadro, tamaño_cuadro])  # Dibuja cada segmento de la culebra

        # Dibuja los ojos de la culebra
        ojo_tamaño = 3
        ojo_offset = 2
        if x1_cambio == -tamaño_cuadro:  # Si la culebra se mueve a la izquierda
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + ojo_offset), int(culebra_cabeza[1] + ojo_offset)), ojo_tamaño)
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + ojo_offset), int(culebra_cabeza[1] + tamaño_cuadro - ojo_offset)), ojo_tamaño)
        elif x1_cambio == tamaño_cuadro:  # Si la culebra se mueve a la derecha
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + tamaño_cuadro - ojo_offset), int(culebra_cabeza[1] + ojo_offset)), ojo_tamaño)
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + tamaño_cuadro - ojo_offset), int(culebra_cabeza[1] + tamaño_cuadro - ojo_offset)), ojo_tamaño)
        elif y1_cambio == -tamaño_cuadro:  # Si la culebra se mueve hacia arriba
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + ojo_offset), int(culebra_cabeza[1] + ojo_offset)), ojo_tamaño)
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + tamaño_cuadro - ojo_offset), int(culebra_cabeza[1] + ojo_offset)), ojo_tamaño)
        elif y1_cambio == tamaño_cuadro:  # Si la culebra se mueve hacia abajo
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + ojo_offset), int(culebra_cabeza[1] + tamaño_cuadro - ojo_offset)), ojo_tamaño)
            pygame.draw.circle(pantalla, blanco, (int(culebra_cabeza[0] + tamaño_cuadro - ojo_offset), int(culebra_cabeza[1] + tamaño_cuadro - ojo_offset)), ojo_tamaño)

        # Dibuja la lengua de la culebra
        lengua_tamaño = 5
        if x1_cambio == -tamaño_cuadro:  # Si la culebra se mueve a la izquierda
            pygame.draw.line(pantalla, rojo, (int(culebra_cabeza[0]), int(culebra_cabeza[1] + tamaño_cuadro / 2)), 
                             (int(culebra_cabeza[0] - lengua_tamaño), int(culebra_cabeza[1] + tamaño_cuadro / 2)), 2)
        elif x1_cambio == tamaño_cuadro:  # Si la culebra se mueve a la derecha
            pygame.draw.line(pantalla, rojo, (int(culebra_cabeza[0] + tamaño_cuadro), int(culebra_cabeza[1] + tamaño_cuadro / 2)), 
                             (int(culebra_cabeza[0] + tamaño_cuadro + lengua_tamaño), int(culebra_cabeza[1] + tamaño_cuadro / 2)), 2)
        elif y1_cambio == -tamaño_cuadro:  # Si la culebra se mueve hacia arriba
            pygame.draw.line(pantalla, rojo, (int(culebra_cabeza[0] + tamaño_cuadro / 2), int(culebra_cabeza[1])), 
                             (int(culebra_cabeza[0] + tamaño_cuadro / 2), int(culebra_cabeza[1] - lengua_tamaño)), 2)
        elif y1_cambio == tamaño_cuadro:  # Si la culebra se mueve hacia abajo
            pygame.draw.line(pantalla, rojo, (int(culebra_cabeza[0] + tamaño_cuadro / 2), int(culebra_cabeza[1] + tamaño_cuadro)), 
                             (int(culebra_cabeza[0] + tamaño_cuadro / 2), int(culebra_cabeza[1] + tamaño_cuadro + lengua_tamaño)), 2)

        # Mostrar el puntaje en la pantalla
        valor_puntaje = fuente.render("Puntaje: " + str(score), True, blanco)
        pantalla.blit(valor_puntaje, [0, 0])

        pygame.display.update()  # Actualiza la pantalla

        # Verifica si la culebra come la comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0  # Genera una nueva posición x para la comida
            comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0  # Genera una nueva posición y para la comida
            largo_culebra += 3  # Incrementa la longitud de la culebra en 3
            score += 1  # Incrementa el puntaje
            comida_seguida += 1  # Incrementa el contador de comida seguida

            # Verifica si la culebra ha comido 5 cuadros seguidos
            if comida_seguida == 5:
                comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0  # Genera una nueva posición x para la comida especial
                comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0  # Genera una nueva posición y para la comida especial
                pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_cuadro, tamaño_cuadro])  # Dibuja la comida especial
                pygame.display.update()  # Actualiza la pantalla

                # Verifica si la culebra come la comida especial
                if x1 == comida_x and y1 == comida_y:
                    score *= 100  # Multiplica el puntaje por 100
                    comida_seguida = 0  # Reinicia el contador de comida seguida

        # Verifica si la culebra come la comida grande
        if x1 == comida_grande_x and y1 == comida_grande_y:
            comida_grande_x = round(random.randrange(0, ancho - tamaño_cuadro * 2) / 10.0) * 10.0  # Genera una nueva posición x para la comida grande
            comida_grande_y = round(random.randrange(0, alto - tamaño_cuadro * 2) / 10.0) * 10.0  # Genera una nueva posición y para la comida grande
            largo_culebra += 10  # Incrementa la longitud de la culebra en 10
            score += 5  # Incrementa el puntaje en 5

        reloj.tick(velocidad_culebra)  # Controla la velocidad del juego

    pygame.quit()  # Cierra pygame
    quit()  # Sale del programa

juego()  # Inicia el juego
