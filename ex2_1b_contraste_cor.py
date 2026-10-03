"""
2.1b - Ajuste de contraste em imagem RGB preservando as cores
Saída esperada: imagem original + imagem resultante + justificativa da estratégia.
Base possível: rgb_hsi_conv.py e 04_contraste_partes.py (do professor).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
# TODO: importar rgb_2_hsi e hsi_2_rgb do rgb_hsi_conv.py (se for usar HSI)


def alongamento_linear(canal, p_min=1, p_max=99):
    # TODO: converter para float
    # TODO: calcular r_min e r_max (usar percentis em vez de min/max absolutos)
    # TODO: tratar o caso r_max == r_min (evitar divisão por zero)
    # TODO: aplicar s = (r - r_min) / (r_max - r_min) * 255
    # TODO: clip em [0, 255] e converter para uint8
    pass


def contraste_preservando_cor(img_bgr):
    # TODO: converter BGR -> RGB antes do rgb_2_hsi (o cv2.imread lê em BGR)
    # TODO: converter para HSI
    # TODO: aplicar alongamento_linear SOMENTE no canal I
    # TODO: manter H e S intactos
    # TODO: converter HSI -> RGB e depois RGB -> BGR para exibir com OpenCV
    pass


def contraste_por_canal(img_bgr):
    # TODO (para comparação/justificativa): aplicar alongamento_linear em B, G e R
    #       separadamente, mostrando que isso pode deslocar as cores
    pass


def executar():
    # TODO: escolher e ler uma imagem RGB com BAIXO contraste
    # TODO: gerar o resultado com contraste_preservando_cor
    # TODO: (opcional) gerar o resultado com contraste_por_canal para comparar
    # TODO: exibir original x resultado(s) e salvar em resultados/
    pass


if __name__ == "__main__":
    executar()

# JUSTIFICATIVA (escrever no README ou falar na apresentação):
# TODO: explicar por que ajustar R, G e B separadamente altera a cor (muda as proporções)
# TODO: explicar por que ajustar só a intensidade (I) preserva matiz e saturação
# TODO: comentar o efeito do clip na volta para RGB (pixels fora do gamut mudam de cor)
