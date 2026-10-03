"""
2.1a - Correção Gamma
Saída esperada: imagem original + imagem resultante.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def add_title(img, text):
    img = np.ascontiguousarray(img)

    canais = 1 if img.ndim == 2 else img.shape[2]

    if canais == 1:
        cor = 255
    else:
        cor = tuple([255] * canais)

    cv2.putText(img, text, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor, 2)

    return img


def correcao_gamma(img: np.ndarray, gamma: float) -> np.ndarray:
    img_out = img.astype(np.float64)

    c = 255 / (255 ** gamma)  # constante de normalização para manter a faixa [0, 255]

    img_out = c * (img_out ** gamma) # correcao gamma

    img_out = np.clip(img_out, 0, 255)

    return img_out.astype(np.uint8)


def executar():
    img = cv2.imread("imagens/ex2_1a_gamma.jpg", cv2.IMREAD_GRAYSCALE)

    gamma = float(input("Digite o valor de gamma (maior que 0): "))

    while gamma <= 0:
        gamma = float(input("Valor inválido. Digite o valor de gamma (maior que 0): "))

    img_resultante = correcao_gamma(img, gamma)

    out = cv2.hconcat([add_title(img, "Original"), add_title(img_resultante, "Resultado")])
    cv2.namedWindow("comparativo", cv2.WINDOW_NORMAL)
    cv2.imshow("comparativo", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


if __name__ == "__main__":
    executar()

# PARA A ARGUIÇÃO:
# TODO: saber explicar por que a normalização é necessária
# TODO: saber explicar o efeito de gamma < 1 e gamma > 1
# TODO: saber fazer a conta à mão (ex.: pixel 64 com gamma 0.5 e com gamma 2)
