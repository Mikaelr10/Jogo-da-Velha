# -*- coding: utf-8 -*-
from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

    def getJogada(self) -> (int, int): # type: ignore
        # R1: Prioriza ataque ou defesa com base nas somas (2 = ataque, 8 = defesa)
        jogada = self.verificar_somas()
        if jogada:
            return jogada

        # R2: Jogada que cria duas sequências simultâneas
        jogada = self.criar_duas_sequencias()
        if jogada:
            return jogada

        # R3: Marca o centro
        if self.tabuleiro.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Marca canto oposto ao oponente
        jogada = self.marcar_canto_oposto()
        if jogada:
            return jogada

        # R5: Marca um canto vazio
        jogada = self.marcar_canto_vazio()
        if jogada:
            return jogada

        # R6: Escolhe aleatoriamente uma posição
        return self.escolher_aleatorio()

    def verificar_somas(self):
        """
        Verifica as somas nas linhas, colunas e diagonais.
        Se soma == 8 (defesa) ou soma == 2 (ataque), retorna a posição para jogar.
        """
        # Verifica Linhas e Colunas
        for i in range(3):
            # Linhas
            soma_linha = sum(self.tabuleiro.matriz[i])
            if soma_linha == 8 or soma_linha == 2:
                for j in range(3):
                    if self.tabuleiro.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                        return (i, j)
            # Colunas
            soma_coluna = sum([self.tabuleiro.matriz[j][i] for j in range(3)])
            if soma_coluna == 8 or soma_coluna == 2:
                for j in range(3):
                    if self.tabuleiro.matriz[j][i] == Tabuleiro.DESCONHECIDO:
                        return (j, i)

        # Verifica Diagonal Principal
        soma_diag1 = sum([self.tabuleiro.matriz[i][i] for i in range(3)])
        if soma_diag1 == 8 or soma_diag1 == 2:
            for i in range(3):
                if self.tabuleiro.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                    return (i, i)

        # Verifica Diagonal Secundária
        soma_diag2 = sum([self.tabuleiro.matriz[i][2 - i] for i in range(3)])
        if soma_diag2 == 8 or soma_diag2 == 2:
            for i in range(3):
                if self.tabuleiro.matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                    return (i, 2 - i)

        return None

    def criar_duas_sequencias(self):
        """Procura por uma jogada que crie duas sequências simultâneas de duas marcações."""
        for l in range(3):
            for c in range(3):
                if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.tabuleiro.matriz[l][c] = self.tipo
                    contagem = 0
                    if self.verificar_somas():
                        contagem += 1
                    self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if contagem >= 2:
                        return (l, c)
        return None

    def marcar_canto_oposto(self):
        """Marca o canto oposto ao ocupado pelo oponente."""
        cantos_opostos = {(0, 0): (2, 2), (0, 2): (2, 0), (2, 0): (0, 2), (2, 2): (0, 0)}
        for canto, oposto in cantos_opostos.items():
            if self.tabuleiro.matriz[canto[0]][canto[1]] == self.oponente and self.tabuleiro.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto
        return None

    def marcar_canto_vazio(self):
        """Marca qualquer canto vazio disponível."""
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for l, c in cantos:
            if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        return None

    def escolher_aleatorio(self):
        """Escolhe aleatoriamente um quadrado vazio."""
        lista = [(l, c) for l in range(3) for c in range(3) if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO]
        if lista:
            p = randint(0, len(lista) - 1)
            return lista[p]
        return None