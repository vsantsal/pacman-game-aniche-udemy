def ui_print(pacman_map):
    """

    :param pacman_map:
    :return:
    """
    for row in pacman_map:
        for column in row:
            print(column, end='')
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
