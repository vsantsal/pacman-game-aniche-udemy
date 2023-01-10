from pacman import play
from ui import ui_print, ui_key, ui_game_finished

mapa = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|",
]

game_finished = False

while not game_finished:
    ui_print(mapa)
    key = ui_key()
    valid_key, pacman_is_alive, pacman_won_the_game = play(mapa, key)
    game_finished = pacman_won_the_game or not pacman_is_alive
    if game_finished:
        ui_game_finished(pacman_won_the_game)
