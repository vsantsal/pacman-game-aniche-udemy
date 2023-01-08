def ui_print(pacman_map):
    """

    :param pacman_map:
    :return:
    """
    for row in pacman_map:
        for column in row:
            print(column, end='')
        print("")
