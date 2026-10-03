"""
2.4 - Reamostragem (vizinho mais próximo e bilinear)
Saída esperada: redução e ampliação da MESMA imagem com os dois métodos + comparação.
Proibido: cv2.resize (só para validação).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def coordenadas_origem(altura_saida, largura_saida, escala):
    # TODO: usar mapeamento INVERSO (da saída para a entrada)
    # TODO: x_orig = (x_saida + 0.5) / escala - 0.5 (idem para y)
    pass


def vizinho_mais_proximo(img, escala):
    # TODO: calcular o tamanho da saída (altura e largura * escala)
    # TODO: obter as coordenadas de origem
    # TODO: arredondar para o pixel mais próximo
    # TODO: limitar os índices com clip (não sair da imagem)
    # TODO: copiar os pixels de origem para a saída
    # TODO: funcionar para imagem cinza e colorida
    pass


def bilinear(img, escala):
    # TODO: calcular o tamanho da saída
    # TODO: obter as coordenadas de origem (float)
    # TODO: x0 = floor(x), x1 = x0 + 1 (idem y), com clip nas bordas
    # TODO: dx = x - x0, dy = y - y0
    # TODO: topo = a*(1-dx) + b*dx ; base = c*(1-dx) + d*dx
    # TODO: resultado = topo*(1-dy) + base*dy
    # TODO: arredondar, clip e converter para uint8
    pass


def executar():
    # TODO: ler a imagem
    # TODO: pedir (ou fixar) o fator de redução (ex.: 0.5) e de ampliação (ex.: 2 ou 4)
    # TODO: reduzir com os dois métodos
    # TODO: ampliar com os dois métodos
    # TODO: exibir lado a lado e salvar em resultados/
    # TODO: mostrar um recorte ampliado (zoom) para evidenciar blocos x suavização
    pass


if __name__ == "__main__":
    executar()

# COMPARAÇÃO (para a apresentação):
# TODO: vizinho mais próximo -> blocos/serrilhado na ampliação, perda de detalhes na redução
# TODO: bilinear -> transições suaves, mas imagem mais borrada
# TODO: saber explicar por que o mapeamento inverso evita buracos
# TODO: saber fazer a conta bilinear à mão (4 vizinhos, dx, dy)
