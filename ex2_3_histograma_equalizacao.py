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
    # usar cv2.calcHist para obter n_k (256 posições)
    # achatar o resultado para vetor 1D
    n_k = cv2.calcHist([img_gray], [0], None, [256], [0, 256]).flatten()
    return n_k.astype(np.float64)  # garante que seja inteiro


def equalizar(img_gray):
    # obter n_k com calcular_histograma
    n_k = calcular_histograma(img_gray)
    # calcular p(r_k) = n_k / (M * N)
    p = n_k / img_gray.size
    # calcular a CDF com np.cumsum
    cdf = np.cumsum(p, dtype=np.float64)
    # calcular s_k = round((L - 1) * CDF), com L = 256
    lut = np.round((255) * cdf)
    lut = np.clip(lut, 0, 255).astype(np.uint8)  # garante que os valores estejam entre 0 e 255

    img_equalizada = lut[img_gray]  # Aplicar a LUT na imagem original

    return img_equalizada, n_k, p, cdf, lut


def tabela_mapeamento(niveis, n_k, p, cdf, lut):
    """Exibe o caminho do mapeamento para cada nível escolhido."""

    print("\nTabela de mapeamento da equalização")
    print("-" * 75)
    print(
        f"{'r_k':>6} {'n_k':>12} {'p(r_k)':>12} "
        f"{'CDF(r_k)':>12} {'s_k':>8}"
    )
    print("-" * 75)

    for nivel in niveis:
        print(
            f"{nivel:>6} "
            f"{int(n_k[nivel]):>12} "
            f"{p[nivel]:>12.6f} "
            f"{cdf[nivel]:>12.6f} "
            f"{int(lut[nivel]):>8}"
        )



if __name__ == "__main__":
    # TODO: ler a imagem em tons de cinza (preferir uma de baixo contraste)
    img_gray = cv2.imread("images/colour_flower_opac.tif", cv2.IMREAD_GRAYSCALE)
    # TODO: calcular e plotar o histograma original (matplotlib)
     # Equalização manual.
    img_equalizada, n_k, p, cdf, lut = equalizar(img_gray)

    # Equalização com OpenCV (para validação).
    img_equalizada_cv2 = cv2.equalizeHist(img_gray)
    hist_equalizada_cv2 = calcular_histograma(img_equalizada_cv2)

    # Calcula o histograma da imagem resultante.
    hist_equalizado = calcular_histograma(img_equalizada)

    # Seleciona três níveis distintos que realmente existem.
    niveis_presentes = np.flatnonzero(n_k > 0)

    if len(niveis_presentes) < 3:
        raise ValueError(
            "A imagem precisa conter pelo menos três níveis "
            "de intensidade distintos."
        )

    niveis = [
        int(niveis_presentes[0]),
        int(niveis_presentes[len(niveis_presentes) // 2]),
        int(niveis_presentes[-1])
    ]

    # Exibe a tabela de mapeamento.
    tabela_mapeamento(niveis, n_k, p, cdf, lut)

    # Monta uma figura com os quatro resultados.
    fig, axes = plt.subplots(3, 2, figsize=(12, 9))

    # Imagem original.
    axes[0, 0].imshow(
        img_gray, cmap="gray", vmin=0, vmax=255
    )
    axes[0, 0].set_title("Imagem Original")
    axes[0, 0].axis("off")

    # Histograma original.
    axes[0, 1].plot(np.arange(256), n_k)
    axes[0, 1].set_title("Histograma Original")
    axes[0, 1].set_xlabel("Intensidade")
    axes[0, 1].set_ylabel("Frequência")
    axes[0, 1].set_xlim(0, 255)
    axes[0, 1].grid(True, alpha=0.3)

    # Imagem equalizada.
    axes[1, 0].imshow(
        img_equalizada, cmap="gray", vmin=0, vmax=255
    )
    axes[1, 0].set_title("Imagem Equalizada")
    axes[1, 0].axis("off")

    # Imagem equalizada por cv2 (para validação).
    axes[2, 0].imshow(
        img_equalizada_cv2, cmap="gray", vmin=0, vmax=255
    )
    axes[2, 0].set_title("Imagem Equalizada (cv2)")
    axes[2, 0].axis("off")

    # Histograma equalizado por cv2 (para validação).
    axes[2, 1].plot(np.arange(256), hist_equalizada_cv2)
    axes[2, 1].set_title("Histograma Equalizado (cv2)")
    axes[2, 1].set_xlabel("Intensidade")
    axes[2, 1].set_ylabel("Frequência")
    axes[2, 1].set_xlim(0, 255)
    axes[2, 1].grid(True, alpha=0.3)

    # Histograma resultante.
    axes[1, 1].plot(np.arange(256), hist_equalizado)
    axes[1, 1].set_title("Histograma Equalizado")
    axes[1, 1].set_xlabel("Intensidade")
    axes[1, 1].set_ylabel("Frequência")
    axes[1, 1].set_xlim(0, 255)
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

# PARA A ARGUIÇÃO:
# TODO: saber explicar por que o histograma equalizado não fica plano
# TODO: saber explicar por que se usa a CDF (crescente, preserva a ordem dos tons)
# TODO: saber montar a tabela à mão para uma imagem pequena
