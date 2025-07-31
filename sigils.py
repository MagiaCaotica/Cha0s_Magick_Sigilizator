import matplotlib.pyplot as plt
import numpy as np

# Definición de las formas básicas de las letras del alfabeto latino
shapes = {
    'A': [(0, 0), (1, 1), (2, 0), (1, 1), (1, 0)],  # Triángulo
    'B': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1), (1, 0), (1, 2)],
    'C': [(1, 0), (0, 0), (0, 2), (1, 2)],
    'D': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1)],
    'E': [(0, 0), (0, 2), (1, 2), (0, 1), (1, 1), (0, 0)],
    'F': [(0, 0), (0, 2), (1, 2), (0, 1)],
    'G': [(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (0, 2)],
    'H': [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    'I': [(0, 0), (1, 0), (0, 2), (1, 2)],
    'J': [(0, 0), (0, 1), (1, 2), (1, 0)],
    'K': [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    'L': [(0, 0), (0, 2), (1, 2)],
    'M': [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)],
    'N': [(0, 0), (0, 2), (2, 0), (2, 2)],
    'O': [(0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2)],
    'P': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1)],
    'Q': [(0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (1, 0)],
    'R': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1), (1, 0)],
    'S': [(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (0, 2)],
    'T': [(0, 2), (1, 2), (1, 0)],
    'U': [(0, 0), (0, 2), (1, 2), (1, 0)],
    'V': [(0, 0), (1, 2), (2, 0)],
    'W': [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)],
    'X': [(0, 0), (2, 2), (0, 2), (2, 0)],
    'Y': [(0, 0), (1, 1), (2, 0), (1, 2)],
    'Z': [(0, 0), (2, 0), (0, 2), (2, 2)],
}

def draw_shape(ax, shape, offset=(0, 0), scale=1):
    """Dibuja una forma básica en el gráfico."""
    x, y = zip(*shape)
    ax.plot(np.array(x) * scale + offset[0], np.array(y) * scale + offset[1], 'k')

def create_sigil(phrase):
    """Crea un sigilo a partir de una frase."""
    unique_letters = list(dict.fromkeys(phrase.replace(" ", "").upper()))  # Eliminar espacios y letras repetidas
    fig, ax = plt.subplots()

    # Inicializa el desplazamiento
    offset_x = 0
    offset_y = 0

    # Dibuja todas las formas en el mismo espacio
    for letter in unique_letters:
        if letter in shapes:
            shape = shapes[letter]
            draw_shape(ax, shape, offset=(offset_x, offset_y), scale=0.5)

            # Modificar el desplazamiento para superponer las formas
            offset_x += np.random.uniform(-0.3, 0.3)  # Desplazamiento aleatorio en x
            offset_y += np.random.uniform(-0.3, 0.3)  # Desplazamiento aleatorio en y

    ax.set_aspect('equal')
    plt.axis('off')  # Ocultar ejes
    plt.show()

if __name__ == "__main__":
    phrase = input("Introduce la frase a sigilizar: ")
    create_sigil(phrase)
