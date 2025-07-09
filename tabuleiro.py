# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def tem_campeao(self):
        """
        Verifica se há um campeão no tabuleiro.
        Retorna o vencedor ou None.
        Exibe mensagem 'Você perdeu' se for o jogador IA.
        """
        for i in range(3):
            # Verifica linhas
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] != Tabuleiro.DESCONHECIDO:
                vencedor = self.matriz[i][0]
                self.exibir_vitoria(vencedor)
                return vencedor
            # Verifica colunas
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] != Tabuleiro.DESCONHECIDO:
                vencedor = self.matriz[0][i]
                self.exibir_vitoria(vencedor)
                return vencedor
        # Verifica diagonal principal
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != Tabuleiro.DESCONHECIDO:
            vencedor = self.matriz[0][0]
            self.exibir_vitoria(vencedor)
            return vencedor
        # Verifica diagonal secundária
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != Tabuleiro.DESCONHECIDO:
            vencedor = self.matriz[0][2]
            self.exibir_vitoria(vencedor)
            return vencedor
        return None

    def exibir_vitoria(self, vencedor):
        """
        Exibe mensagem de vitória dependendo do vencedor.
        """
        if vencedor == Tabuleiro.JOGADOR_X:
            print("Você perdeu!")
        elif vencedor == Tabuleiro.JOGADOR_0:
            print("Parabéns! Você ganhou!")
