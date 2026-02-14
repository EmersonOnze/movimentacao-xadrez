class Tabuleiro:
    def __init__(self):
        self.tamanho = 8

    def posicao_valida(self, linha, coluna):
        return 0 <= linha < self.tamanho and 0 <= coluna < self.tamanho
