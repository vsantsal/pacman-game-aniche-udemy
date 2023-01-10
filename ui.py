from pacman import PacmanActors

_mapa_visualizacoes = {
    PacmanActors.DASH_WALL.value: [
        "......",
        "......",
        "......",
        "......"
    ],
    PacmanActors.PIPE_WALL.value: [
        "......",
        "......",
        "......",
        "......"
    ],
    PacmanActors.GHOST.value: [
        " .-.  ",
        "| OO| ",
        "|   | ",
        "'^^^' "
    ],
    PacmanActors.PACMAN.value: [
        " .--. ",
        "/ _.-'",
        "\\  '-.",
        " '--' "
    ],
    PacmanActors.EMPTY_SPACE.value: [
        "      ",
        "      ",
        "      ",
        "      "
    ],
    PacmanActors.PILL.value: [
        "      ",
        " .-.  ",
        " '-'  ",
        "      "
    ],
}


def ui_print(pacman_map):
    """

    :param pacman_map:
    :return:
    """
    for row in pacman_map:
        for piece in range(4):
            for column in row:
                try:
                    print(_mapa_visualizacoes[column][piece], end='')
                except KeyError:
                    continue
            print("")


def ui_key() -> str:
    """
    Função para obter direção do usuário
    :return:
    """
    return input("Move pacman: ")


def ui_game_finished(has_won: bool) -> None:
    """
    Função para imprimir mensagem de fim de jogo, que variará conforme
    has_won é verdadeiro ou falso.

    :param has_won:
    :return:
    """
    mensagem = "Game over! " + ("You won" if has_won else "Pacman died")
    print(mensagem)
