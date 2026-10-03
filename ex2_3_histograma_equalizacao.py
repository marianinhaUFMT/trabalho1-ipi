"""
2.3 - Histograma e equalização
Saída esperada: imagem original, histograma original, imagem equalizada,
histograma equalizado e tabela de mapeamento para 3 níveis.
Permitido: cv2.calcHist, np.cumsum. Proibido: cv2.equalizeHist (só para validação).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def calcular_histograma(img_gray):
    # TODO: usar cv2.calcHist para obter n_k (256 posições)
    # TODO: achatar o resultado para vetor 1D
    pass


def equalizar(img_gray):
    # TODO: obter n_k com calcular_histograma
    # TODO: calcular p(r_k) = n_k / (M * N)
    # TODO: calcular a CDF com np.cumsum
    # TODO: calcular s_k = round((L - 1) * CDF), com L = 256
    # TODO: montar a LUT e aplicar: saida = lut[img_gray]
    # TODO: retornar também n_k, p, cdf e lut (necessários para a tabela)
    pass


def tabela_mapeamento(niveis, n_k, p, cdf, lut):
    # TODO: para cada um dos 3 níveis escolhidos, imprimir r_k, n_k, p(r_k), CDF(r_k), s_k
    # TODO: escolher níveis que REALMENTE ocorram na imagem (n_k > 0)
    pass


def executar():
    # TODO: ler a imagem em tons de cinza (preferir uma de baixo contraste)
    # TODO: calcular e plotar o histograma original (matplotlib)
    # TODO: equalizar
    # TODO: calcular e plotar o histograma da imagem equalizada
    # TODO: exibir as 4 saídas (imagem + histograma, antes e depois) e salvar em resultados/
    # TODO: imprimir a tabela de mapeamento para 3 níveis
    # TODO (opcional): comparar com cv2.equalizeHist apenas como validação
    pass


if __name__ == "__main__":
    executar()

# PARA A ARGUIÇÃO:
# TODO: saber explicar por que o histograma equalizado não fica plano
# TODO: saber explicar por que se usa a CDF (crescente, preserva a ordem dos tons)
# TODO: saber montar a tabela à mão para uma imagem pequena
