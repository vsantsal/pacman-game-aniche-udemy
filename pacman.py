# model
# @ -> pacman (our hero)
# G -> Ghost
# P -> Pills
# . -> empty spaces
# | and - -> walls
from enum import Enum

from exceptions import IllegalPacmanPositionException


class PacmanActors(Enum):
    PACMAN = '@'
    GHOST = 'G'
    PILL = 'P'
    EMPTY_SPACE = '.'
    HORIZONTAL_WALL = '|'
    VERTICAL_WALL = '-'


def find_pacman(pacman_map) -> (int, int):
    """
    Função que retorna a posição do pacman no jogo.

    :param pacman_map:
    :return: tupla com coordenadas cartesianas do pacman no jogo
    """
    # posições inexistentes no mapa do jogo (caso não se encontre pacman no mapa)
    pacman_x = -1
    pacman_y = -1

    # variável para controlar possibilidade (ilegal) de haver mais de um pacman no mapa
    contador_pacman = 0

    # busca posição a posição do pacman
    for x in range(len(pacman_map)):
        for y in range(len(pacman_map[x])):
            if pacman_map[x][y] == PacmanActors.PACMAN.value:
                contador_pacman += 1
                if contador_pacman > 1:
                    raise IllegalPacmanPositionException("Há mais de um pacman no jogo!")
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y
