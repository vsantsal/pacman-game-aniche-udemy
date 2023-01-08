# model
# @ -> pacman (our hero)
# G -> Ghost
# P -> Pills
# . -> empty spaces
# | and - -> walls

game_map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|........|",
    "|--------|",
]


def find_pacman(pacman_map):
    """"""
    pacman_x = -1
    pacman_y = -1

    for x in range(len(pacman_map)):
        for y in range(len(pacman_map[x])):
            if pacman_map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y
