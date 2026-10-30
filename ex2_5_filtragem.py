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


def padding(img, m, n):
    M, N = img.shape

    a = int((m - 1) / 2)
    b = int((n - 1) / 2)

    img_padded = np.zeros((M + m -1, N + n - 1), np.uint8)
    img_padded[ a : -a,  b: -b] = img

    return img_padded

def filtro_box(img, ksize):
    M, N = img.shape

    kernel = np.ones((ksize, ksize), dtype=np.float64) / (ksize * ksize)

    m, n = kernel.shape

    img_padded = padding(img, m, n)

    img_out = np.zeros((M, N), dtype=np.float64)

    for x in range(M):
        for y in range(N):
            pixel = np.sum(img_padded[x:x+m, y:y+n] * kernel)
            img_out[x, y] = pixel

    return np.clip(np.round(img_out), 0, 255).astype(np.uint8)

# def kernel_gaussiano(ksize, sigma):
#     centro = ksize // 2
#     kernel = np.zeros((ksize, ksize, 1), dtype=float)

#     for i in range(ksize):
#         for j in range(ksize):
#             s = i - centro
#             t = j - centro
#             # calcular exp(-(x^2 + y^2) / (2 * sigma^2))
#             kernel[i, j] = np.exp(-(s**2 + t**2) / (2 * sigma**2))
#     # normalizar o kernel para que a soma seja 1
#     kernel = kernel / kernel.sum()

#     return kernel

# def filtro_gaussiano(img, ksize=9, sigma=2.0):
#     kernel = kernel_gaussiano(ksize, sigma)
#     img_padded = padding(img, ksize, ksize)

#     M, N, channels = img.shape
#     img_out = np.zeros((M, N, channels), dtype=np.float64)

#     for x in range(M):
#         for y in range(N):
#             for c in range(channels):
#                 # aplicar o kernel a janela de pixels
#                 pixel = np.sum(img_padded[x:x+ksize, y:y+ksize, c] * kernel[:, :, 0])
#                 img_out[x, y, c] = pixel

#     return np.clip(np.round(img_out), 0, 255).astype(np.uint8)

def filtro_mediana(img, ksize):
    M, N = img.shape
    img_padded = padding(img, ksize, ksize)
    img_out = np.zeros((M, N), dtype=np.uint8)
    
    # vamos implementar
    for x in range(M):
        for y in range(N):
            janela = img_padded[x : x + ksize, y : y + ksize]
            img_out[x, y] = np.median(janela)

    return img_out


if __name__ == "__main__":

    img = cv2.imread("images/filtro.tif", cv2.IMREAD_GRAYSCALE)

    k = int(input("Digite o tamanho da janela (ímpar): "))
    if k % 2 == 0:
        raise ValueError("k deve ser ímpar")
    # sigma = float(input("Digite o valor de sigma (para o filtro gaussiano): "))
    img_box = filtro_box(img, k)
    # img_gauss = filtro_gaussiano(img, k, sigma)
    img_median = filtro_mediana(img, k)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(img_box, cv2.COLOR_BGR2RGB))
    plt.title(f"Filtro Box (k={k})")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB))
    plt.title(f"Filtro Mediana (k={k})")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

