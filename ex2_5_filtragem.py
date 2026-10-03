"""
2.5 - Filtragem espacial
Obrigatório: filtro Box/média + (Gaussiano OU Mediana).
Saída esperada: os dois filtros aplicados à mesma imagem + explicação.
Proibido: cv2.blur, cv2.boxFilter, cv2.GaussianBlur, cv2.medianBlur (só para validação).
Permitido: np.pad para o padding.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def aplicar_padding(img, k):
    # TODO: usar np.pad com borda de k // 2 pixels
    # TODO: escolher o modo ('edge' ou 'reflect') e saber justificar
    pass


def filtro_box(img, k):
    # TODO: validar k ímpar
    # TODO: aplicar padding
    # TODO: para cada pixel, calcular a média da janela k x k
    # TODO: converter o resultado para uint8
    pass


# TODO: ESCOLHER UM dos dois filtros abaixo e apagar o outro

def kernel_gaussiano(k, sigma):
    # TODO: montar a grade de coordenadas centrada em 0
    # TODO: calcular exp(-(x^2 + y^2) / (2 * sigma^2))
    # TODO: normalizar para a soma dar 1
    pass


def filtro_gaussiano(img, k, sigma):
    # TODO: obter o kernel
    # TODO: aplicar padding
    # TODO: para cada pixel, soma ponderada da janela pelo kernel
    # TODO: converter o resultado para uint8
    pass


def filtro_mediana(img, k):
    # TODO: aplicar padding
    # TODO: para cada pixel, ordenar os valores da janela e pegar o do meio
    # TODO: converter o resultado para uint8
    pass


def executar():
    # TODO: ler a imagem (se usar mediana, uma imagem com ruído sal e pimenta mostra bem a diferença)
    # TODO: pedir o tamanho k (e sigma, se gaussiano)
    # TODO: aplicar o box e o filtro escolhido na MESMA imagem
    # TODO: exibir original + resultados e salvar em resultados/
    # TODO (opcional): testar mais de um k para mostrar o efeito do tamanho da janela
    pass


if __name__ == "__main__":
    executar()

# EXPLICAÇÃO (para a apresentação):
# TODO: box -> todos os vizinhos com o mesmo peso; suaviza ruído e borra bordas
# TODO: gaussiano -> peso diminui com a distância; borramento mais natural; papel do sigma
# TODO: mediana -> não linear; remove ruído impulsivo e preserva bordas
# TODO: saber calcular média e mediana de uma janela 3x3 à mão
# TODO: saber explicar o efeito do padding nas bordas
