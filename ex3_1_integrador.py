"""
3.1 - Problema integrador: identificação e contagem dos objetos maiores (gado)
Usar SEMPRE a imagem original (a de referência serve só para saber quais objetos interessam).
Combinar pelo menos DOIS métodos estudados, reaproveitando as funções dos outros arquivos.
Saída esperada: original + resultado de cada etapa + parâmetros + contagem manual + discussão.
Não desenhar contornos, retângulos, rótulos ou marcações em vermelho no resultado.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

def canais(img_bgr):
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV) 
    img_b = img_bgr[:, :, 0]
    img_g = img_bgr[:, :, 1]
    img_r = img_bgr[:, :, 2]
    
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB))
    plt.title("Escala de Cinza")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB))
    plt.title("Canal B")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(cv2.cvtColor(img_g, cv2.COLOR_BGR2RGB))
    plt.title("Canal G")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB))
    plt.title("Canal R")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(cv2.cvtColor(img_hsv[:, :, 1], cv2.COLOR_BGR2RGB))
    plt.title("Saturação (HSV)")
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.imshow(cv2.cvtColor(img_hsv[:, :, 2], cv2.COLOR_BGR2RGB))
    plt.title("Valor (HSV)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

def padding(img, m, n):
    a = int((m - 1) / 2)
    b = int((n - 1) / 2)
    return np.pad(img, ((a, a), (b, b)), mode="edge")

def filtro_mediana(img, ksize):
    M, N = img.shape
    img_padded = padding(img, ksize, ksize)
    img_out = np.zeros((M, N), dtype=np.uint8)
    
    for x in range(M):
        for y in range(N):
            janela = img_padded[x : x + ksize, y : y + ksize]
            img_out[x, y] = np.median(janela)

    return img_out

def filtro_gaussiano(img, kernel):
    M, N = img.shape
    m, n = kernel.shape
    img_padded = padding(img, m, n)
    img_out = np.zeros((M, N), dtype=float)
    for x in range(M):
        for y in range(N):
            pixel = np.sum(img_padded[x:x + m, y:y + n] * kernel)
            img_out[x, y] = pixel
    return np.clip(np.round(img_out), 0, 255).astype(np.uint8)

def kernel_gaussiano(ksize, sigma):
    a = int((ksize - 1) / 2)
    kernel = np.zeros((ksize, ksize), dtype=float)
    for x in range(-a, a + 1):
        for y in range(-a, a + 1):
            kernel[x + a, y + a] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)
    return kernel

def limiarizar(img_gray, T):
    return np.where(img_gray > T, 255, 0).astype(np.uint8)

def calcular_histograma(img_gray):
    n_k = cv2.calcHist([img_gray], [0], None, [256], [0, 256]).flatten()
    return n_k.astype(np.float64)

if __name__ == "__main__":
    # Carrega a imagem original
    img_original = cv2.imread("images/bois.jpg", cv2.IMREAD_COLOR)
    if img_original is None:
        raise FileNotFoundError("Imagem images/bois.jpg não encontrada!")

    canais = canais(img_original)  # Exibe os canais da imagem
    canal_b = img_original[:, :, 0]  # Canal B

    # Processamentos
    kernel_gauss = kernel_gaussiano(ksize=15, sigma=2.0)
    filtrada_gauss = filtro_gaussiano(canal_b, kernel_gauss)
    hist = calcular_histograma(filtrada_gauss) 
    limiarizada = limiarizar(filtrada_gauss, 190)
    filtrada_mediana = filtro_mediana(limiarizada, ksize=3)

    # Janela única consolidada em 2 linhas e 3 colunas
    plt.figure(figsize=(16, 9))

    # 1. Canal B Original / Referência
    plt.subplot(2, 3, 1)
    plt.imshow(canal_b, cmap='gray')
    plt.title("1. Canal B Original")
    plt.axis('off')

    # 2. Imagem após Filtro Gaussiano
    plt.subplot(2, 3, 2)
    plt.imshow(filtrada_gauss, cmap='gray')
    plt.title("2. Filtro Gaussiano (k=15, σ=2.0)")
    plt.axis('off')

    # 3. Gráfico do Histograma
    plt.subplot(2, 3, 3)
    plt.plot(hist, color='blue')
    plt.title("3. Histograma do Canal Filtrado")
    plt.xlabel("Intensidade")
    plt.ylabel("Nº de Pixels")
    plt.xlim([0, 255])
    plt.grid()

    # 4. Imagem Binária após Limiarização
    plt.subplot(2, 3, 4)
    plt.imshow(limiarizada, cmap='gray')
    plt.title("4. Limiarização (T=190)")
    plt.axis('off')

    # 5. Segunda Passagem (Filtro de Mediana)
    plt.subplot(2, 3, 5)
    plt.imshow(filtrada_mediana, cmap='gray')
    plt.title("5. Pós-Filtro Mediana (k=3)")
    plt.axis('off')

    # 6. Imagem Original Colorida (RGB) para contexto geral
    plt.subplot(2, 3, 6)
    plt.imshow(cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB))
    plt.title("6. Imagem Original (RGB)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()