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
    # usar np.pad com borda de k // 2 pixels
    pad = k // 2
    # escolher o modo ('edge' ou 'reflect') e saber justificar
    return np.pad(img, ((pad, pad), (pad, pad)) + ((0, 0),) * (img.ndim - 2), mode='edge')

def filtro_box(img, k):
    # valida k ímpar
    if k % 2 == 0:
        raise ValueError("k deve ser ímpar")
    # padding
    img_pad = aplicar_padding(img, k)
    # para cada pixel, calcular a media da janela k x k
    img_out = np.zeros(img.shape, dtype=np.float64)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_out[i, j] = np.mean(img_pad[i:i+k, j:j+k], axis=(0, 1))
    
    return np.clip(np.round(img_out), 0, 255).astype(np.uint8)

# def kernel_gaussiano(k, sigma):
#     # montar a grade de coordenadas centrada em 0
#     # calcular exp(-(x^2 + y^2) / (2 * sigma^2))
#     # normalizar para a soma dar 1
#     pass


# def filtro_gaussiano(img, k, sigma):
#     # obter o kernel
#     # aplicar padding
#     # para cada pixel, soma ponderada da janela pelo kernel
#     # converter o resultado para uint8
#     pass


def filtro_mediana(img, k):
    # padding
    img_pad = aplicar_padding(img, k)
    # para cada pixel, ordenar os valores da janela e pegar o do meio
    img_out = np.zeros(img.shape, dtype=np.float64)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Recorta a janela k x k ao redor do pixel atual.
            janela = img_pad[i:i + k, j:j + k]
            # Ordena os valores da janela e escolhe o valor central.
            img_out[i, j] = np.median(janela, axis=(0, 1))

    return np.clip(np.round(img_out), 0, 255).astype(np.uint8)


if __name__ == "__main__":
    # TODO: ler a imagem (se usar mediana, uma imagem com ruído sal e pimenta mostra bem a diferença)
    img = cv2.imread("images/filtro.tif", cv2.IMREAD_COLOR)
    # TODO: pedir o tamanho k (e sigma, se gaussiano)
    k = int(input("Digite o tamanho da janela (ímpar): "))
    if k % 2 == 0:
        raise ValueError("k deve ser ímpar")
    # sigma = float(input("Digite o valor de sigma (para o filtro gaussiano): "))
    # TODO: aplicar o box e o filtro escolhido na MESMA imagem
    img_box = filtro_box(img, k)
    # img_gauss = filtro_gaussiano(img, k, sigma)
    img_median = filtro_mediana(img, k)
    # TODO: exibir original + resultados e salvar em resultados/
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
    # TODO (opcional): testar mais de um k para mostrar o efeito do tamanho da janela
    pass

# EXPLICAÇÃO (para a apresentação):
# TODO: box -> todos os vizinhos com o mesmo peso; suaviza ruído e borra bordas
# TODO: gaussiano -> peso diminui com a distância; borramento mais natural; papel do sigma
# TODO: mediana -> não linear; remove ruído impulsivo e preserva bordas
# TODO: saber calcular média e mediana de uma janela 3x3 à mão
# TODO: saber explicar o efeito do padding nas bordas
