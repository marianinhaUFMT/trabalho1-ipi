"""
2.2 - Limiarização global
Saída esperada: imagem original + binária para pelo menos dois valores de T + comparação.
Proibido: cv2.threshold (só para validação).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def limiarizar(img_gray, T):
    # TODO: retornar 255 onde img_gray > T e 0 caso contrário
    # TODO: garantir saída em uint8
    pass


def executar():
    # TODO: ler a imagem em tons de cinza (cv2.IMREAD_GRAYSCALE)
    # TODO: pedir o valor de T ao usuário e validar (0 a 255)
    # TODO: gerar a binária para pelo menos dois valores de T
    # TODO: exibir original + binárias lado a lado e salvar em resultados/
    # TODO (opcional): exibir o histograma marcando cada T, para justificar a escolha
    pass


if __name__ == "__main__":
    executar()

# COMPARAÇÃO (para a apresentação):
# TODO: descrever o que acontece com T baixo (fundo vaza para branco)
# TODO: descrever o que acontece com T alto (objeto perde partes)
# TODO: relacionar o melhor T com o vale entre os picos do histograma
