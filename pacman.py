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
    DASH_WALL = '-'
    PIPE_WALL = '|'


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


def move_pacman(pacman_map, next_pacman_x, next_pacman_y):
    """
    Função que recoloca pacman em nova posição (coordenadas
    next_pacman_x, next_pacman_y) do pacman_map.

    :param pacman_map:
    :param next_pacman_x:
    :param next_pacman_y:
    :return:
    """
    # obtem posição atual do pacman no mapa
    pacman_x, pacman_y = find_pacman(pacman_map)

    # retiramos pacman da posiação atual
    pacman_map[pacman_x] = _replace_position_in_pacman_row(
        pacman_map[pacman_x],
        pacman_y,
        PacmanActors.EMPTY_SPACE.value
    )

    # o colocamos na nova posição
    pacman_map[next_pacman_x] = _replace_position_in_pacman_row(
        pacman_map[next_pacman_x],
        next_pacman_y,
        PacmanActors.PACMAN.value
    )


def next_position(pacman_map, key: str) -> (int, int):
    """
    a <-- left
    d --> right
    w --> up
    s --> down

    :param pacman_map:
    :param key:
    :return:
    """
    # posição onde pacman está
    x, y = find_pacman(pacman_map)

    # mapa com ajustes de posição
    mapa_movimentacao = {
        'a': (0, -1),
        'd': (0, 1),
        'w': (-1, 0),
        's': (1, 0),
    }

    # deriva posições novas
    try:
        next_x, next_y = mapa_movimentacao[key.lower()]
    except KeyError:
        raise ValueError(f"Direção '{key}' não reconhecida")
    return x + next_x, y + next_y


def total_pills(pacman_map) -> int:
    """

    Função que conta pills no jogo.

    :param pacman_map:
    :return:
    """
    count = 0
    for row in range(len(pacman_map)):
        for column in pacman_map[row]:
            if column == PacmanActors.PILL.value:
                count += 1
    return count


def play(pacman_map, key) -> (bool, bool, bool):
    """
    Função retorna tupla de booleanos -
    * primeira posição indica se jogada
    foi válida
    * segunda posição se pacman está vivo
    * terceira posição se jogo acabou

    :param pacman_map:
    :param key:
    :return:
    """
    # obtém coordenadas de destino a partir da key passada
    try:
        next_x, next_y = next_position(pacman_map, key)
    except ValueError:
        return False, True, False

    if not _is_within_borders(pacman_map, next_x, next_y):
        return False, True, False

    if _has_hit_wall(pacman_map, next_x, next_y):
        return False, True, False

    if _has_hit_ghost(pacman_map, next_x, next_y):
        return True, False, False

    move_pacman(pacman_map, next_x, next_y)

    if total_pills(pacman_map) == 0:
        return True, True, True

    return True, True, False


def _has_hit_ghost(pacman_map, next_x: int, next_y: int) -> bool:
    return pacman_map[next_x][next_y] == PacmanActors.GHOST.value


def _has_hit_wall(pacman_map, next_x: int, next_y: int) -> bool:
    return (
            pacman_map[next_x][next_y] == PacmanActors.PIPE_WALL.value or
            pacman_map[next_x][next_y] == PacmanActors.DASH_WALL.value
    )


def _is_within_borders(pacman_map, next_x: int, next_y: int) -> bool:
    number_of_rows: int = len(pacman_map)
    x_is_valid: bool = 0 <= next_x < number_of_rows

    number_of_columns: int = len(pacman_map[0])
    y_is_valid: bool = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid


def _replace_position_in_pacman_row(pacman_row: str,
                                    position_index: int,
                                    position_new_value: str) -> str:
    """
    Função auxiliar (privada) para construir nova linha com subsituição
    na position_index de pacman_row passada por position_new_value passado

    :param pacman_row:
    :param position_index:
    :param position_new_value:
    :return:
    """
    return pacman_row[:position_index] + position_new_value + pacman_row[position_index+1:]
