from pecas import Torre, Bispo, Rainha, Cavalo, Rei, Peao

def testar_peca(peca, nome):
    print(f"\nMovimentos da {nome} na posição (4,4):")
    movimentos = peca.movimentos_validos((4, 4))
    print(movimentos)


if __name__ == "__main__":
    testar_peca(Torre("branco"), "Torre")
    testar_peca(Bispo("branco"), "Bispo")
    testar_peca(Rainha("branco"), "Rainha")
    testar_peca(Cavalo("branco"), "Cavalo")
    testar_peca(Rei("branco"), "Rei")
    testar_peca(Peao("branco"), "Peão")
