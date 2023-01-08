class IllegalPacmanPositionException(Exception):
    """
    Exceção para controlar posições ilegais no jogo.
    """
    def __init__(self, message):
        super().__init__(message)
