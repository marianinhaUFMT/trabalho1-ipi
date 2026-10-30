"""
2.2 - Limiarização global
Saída esperada: imagem original + binária para pelo menos dois valores de T + comparação.
Proibido: cv2.threshold (só para validação).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def limiarizar(img_gray, T):
    # g(x, y) = 255 se f(x, y) > T, e 0 caso contrário
    # retorna 255 onde img_gray > T e 0 caso contrario
    return np.where(img_gray > T, 255, 0).astype(np.uint8)


if __name__ == "__main__":

    img_gray = cv2.imread("images/colour_flower_opac.tif", cv2.IMREAD_GRAYSCALE)

    # garantir que seja entre 0 e 255 (uint8)
    T1 = int(input("Digite o valor de T1 (0 a 255): "))
    while T1 < 0 or T1 > 255:
        T1 = int(input("Valor inválido. Digite o valor de T1 (0 a 255): "))
    T2 = int(input("Digite o valor de T2 (0 a 255): "))
    while T2 < 0 or T2 > 255:
        T2 = int(input("Valor inválido. Digite o valor de T2 (0 a 255): "))

    img_bin1 = limiarizar(img_gray, T1)
    img_bin2 = limiarizar(img_gray, T2)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img_bin1, cmap='gray')
    plt.title(f'Binária (T={T1})')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img_bin2, cmap='gray')
    plt.title(f'Binária (T={T2})')
    plt.axis('off')

    plt.show()
