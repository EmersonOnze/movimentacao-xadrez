class Peca:
    def __init__(self, cor):
        self.cor = cor

    def movimentos_validos(self, posicao):
        pass


class Torre(Peca):
    def movimentos_validos(self, posicao):
        linha, coluna = posicao
        movimentos = []

        for i in range(8):
            if i != linha:
                movimentos.append((i, coluna))
            if i != coluna:
                movimentos.append((linha, i))

        return movimentos


class Bispo(Peca):
    def movimentos_validos(self, posicao):
        linha, coluna = posicao
        movimentos = []

        for i in range(-7, 8):
            if 0 <= linha + i < 8 and 0 <= coluna + i < 8:
                movimentos.append((linha + i, coluna + i))
            if 0 <= linha + i < 8 and 0 <= coluna - i < 8:
                movimentos.append((linha + i, coluna - i))

        return movimentos


class Rainha(Peca):
    def movimentos_validos(self, posicao):
        return Torre(self.cor).movimentos_validos(posicao) + \
               Bispo(self.cor).movimentos_validos(posicao)


class Cavalo(Peca):
    def movimentos_validos(self, posicao):
        linha, coluna = posicao
        movimentos = []

        movimentos_possiveis = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dl, dc in movimentos_possiveis:
            nova_linha = linha + dl
            nova_coluna = coluna + dc

            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                movimentos.append((nova_linha, nova_coluna))

        return movimentos


class Rei(Peca):
    def movimentos_validos(self, posicao):
        linha, coluna = posicao
        movimentos = []

        for dl in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dl == 0 and dc == 0:
                    continue

                nova_linha = linha + dl
                nova_coluna = coluna + dc

                if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                    movimentos.append((nova_linha, nova_coluna))

        return movimentos


class Peao(Peca):
    def movimentos_validos(self, posicao):
        linha, coluna = posicao
        movimentos = []

        direcao = -1 if self.cor == "branco" else 1

        if 0 <= linha + direcao < 8:
            movimentos.append((linha + direcao, coluna))

        return movimentos
