"""
2.4 - Reamostragem (vizinho mais próximo e bilinear)
Saída esperada: redução e ampliação da MESMA imagem com os dois métodos + comparação.
Proibido: cv2.resize (só para validação).
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

def vizinho_mais_proximo(img: np.ndarray, sch, scw):
    """
    1. Dados:
        img original I: Ri x Ci
        img saida J: Ro x Co

    2. fator escala:
        na linha Sr: Ri / Ro
        na coluna Sc: Ci / Co

    3. Mapeamento:
        rm = [0 1 2 ... Ro-1] * Sr
        cm = [0 1 2 ... Co-1] * Sc
    
    4. coord. dos viz. mais proximos:
        r = round(rm) e c = round(cm)

    5. para l=0 ... Ro-1 e m=0 ... Co-1:
        J(l,m) = I(r[l], c[m])
    """
    # 1. Dados
    # ri, ci, channels = img.shape
    # ro, co = (int(ri * sch), int(ci * scw))
    # sr = ri / ro # cast to float
    # sc = ci / co # cast to float

    # img_out = np.zeros((ro, co, channels), dtype=np.uint8)

    # for r in range(ro):
    #     rm = int(ro * sr)
    #     for c in range(co):
    #         cm = int(co * sc)
    #         img_out[ro, co] = img[rm, cm]

    # return img_out
    ri, ci, channels= img.shape
    ro, co = int(ri * sch), int(ci * scw)
    sr = ri / ro
    sc = ci / co
    img_out = np.zeros((ro, co, channels), dtype=np.uint8) # Inicializa a imagem de saída
    for r0 in range(ro):
        rm = int(r0 * sr)
        for c0 in range(co):
            cm = int(c0 * sc)
            img_out[r0, c0] = img[rm, cm]
    return img_out


# interpolação bilinear
def bilinear(img: np.ndarray, sch, scw):
    """
    1. Dados:
        img original I: Ri x Ci
        img saida J: Ro x Co

    2. fator escala:
        na linha Sr: Ri / Ro
        na coluna Sc: Ci / Co

    3. Mapeamento:
        rm = r * sr para r=[0 1 2 ... Ro-1]
        cm = c * sc para c=[0 1 2 ... Co-1]
    
    4. cacule (r0, c0) para cada par (rm, cm):
        (r0, c0) = (floor(rm), floor(cm))

    5. para cada par (rm, cm) obtido de (r, c):
        J(r, c) = I(r0, c0) * (1 - (delta_r)
                  + I(r0 + 1, c0) * (delta_r) * (1 - (delta_c))
                  + I(r0, c0 + 1) * (1 - (delta_r)) * (delta_c)
                  + I(r0 + 1, c0 + 1) * (delta_r) * (delta_c) 
    """
    ri, ci, channels = img.shape
    ro, co = int(ri * sch), int(ci * scw)

    sr = float(ri) / float(ro)
    sc = float(ci) / float(co)

    img_out = np.zeros((ro, co, channels), float) # Inicializa a imagem de saída
    
    for r in range(ro):
        rm = r * sr
        r0 = (np.floor(rm))
        delta_r = rm - r0
        for c in range(co):
            cm = c * sc
            c0 = (np.floor(cm))
            delta_c = cm - c0

            r0 = int(min(r0, ri - 2))
            c0 = int(min(c0, ci - 2))

            ia = img[r0,         c0]
            ib = img[r0 + 1,     c0]
            ic = img[r0,     c0 + 1]
            id = img[r0 + 1, c0 + 1]

            wa = (1 - delta_r) * (1 - delta_c)
            wb = (delta_r) * (1 - delta_c)
            wc = (1 - delta_r) * (delta_c)
            wd = (delta_r) * (delta_c)

            pixel = ia * wa + ib * wb + ic * wc + id * wd

            img_out[r, c] = pixel
            
        

    return img_out.astype(np.uint8)



if __name__ == "__main__":
    # # Matriz 4x4 simulando uma imagem com uma borda nítida (preto para branco)
    # img_pequena = np.array([
    #     [0,   0,   255, 255],
    #     [0,   0,   255, 255],
    #     [255, 255, 0,   0],
    #     [255, 255, 0,   0]
    # ], dtype=np.uint8).reshape(4, 4, 1)

    # # Ampliando a matriz em um fator pequeno (ex: 2.0) para conseguirmos ler no terminal
    # fator_ampliacao = 2.0
    
    # # Passando os dois fatores (sch e scw) exigidos pelas funções
    # img_nn = vizinho_mais_proximo(img_pequena, fator_ampliacao, fator_ampliacao)
    # img_bilinear = bilinear(img_pequena, fator_ampliacao, fator_ampliacao)

    # # Exibindo os valores numéricos no terminal (usamos squeeze() para remover o canal extra na hora do print)
    # print("--- MATRIZ ORIGINAL (4x4) ---")
    # print(img_pequena.squeeze())
    
    # print(f"\n--- VIZINHO MAIS PRÓXIMO (Ampliação {fator_ampliacao}x) ---")
    # print("Notem que ele apenas duplica os valores 0 e 255 (efeito bloco):")
    # print(img_nn.squeeze())
    
    # print(f"\n--- BILINEAR (Ampliação {fator_ampliacao}x) ---")
    # print("Notem o surgimento de valores intermediários suavizando a transição:")
    # print(img_bilinear.squeeze())

    # # Agora vamos visualizar graficamente com um fator grande para evidenciar o efeito visual
    # fator_visual = 20.0 # Amplia 20x para vermos bem os pixels
    
    # # Passando os dois fatores novamente
    # img_nn_plot = vizinho_mais_proximo(img_pequena, fator_visual, fator_visual)
    # img_bilinear_plot = bilinear(img_pequena, fator_visual, fator_visual)

    # plt.figure(figsize=(12, 4))
    
    # plt.subplot(1, 3, 1)
    # plt.imshow(img_pequena.squeeze(), cmap="gray", vmin=0, vmax=255)
    # plt.title("Original (4x4)")
    # plt.axis("off")
    
    # plt.subplot(1, 3, 2)
    # plt.imshow(img_nn_plot.squeeze(), cmap="gray", vmin=0, vmax=255)
    # plt.title("Vizinho mais próximo\n(Efeito de Blocos)")
    # plt.axis("off")
    
    # plt.subplot(1, 3, 3)
    # plt.imshow(img_bilinear_plot.squeeze(), cmap="gray", vmin=0, vmax=255)
    # plt.title("Bilinear\n(Transição Suave / Borrada)")
    # plt.axis("off")
    
    # plt.tight_layout()
    # plt.show()

    # Carregando uma imagem real do seu diretório
    img_bgr = cv2.imread("images/gata_deitado.jpeg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # Para exibir as cores corretas no matplotlib
    
    # Definindo os fatores
    fator_reducao = 0.4   # Reduz para 40% do tamanho
    fator_ampliacao = 4.0 # Amplia para 400% do tamanho
    
    # 1. REDUÇÃO
    img_red_nn = vizinho_mais_proximo(img_rgb, fator_reducao, fator_reducao)
    img_red_bil = bilinear(img_rgb, fator_reducao, fator_reducao)
    
    # 2. AMPLIAÇÃO
    img_amp_nn = vizinho_mais_proximo(img_rgb, fator_ampliacao, fator_ampliacao)
    img_amp_bil = bilinear(img_rgb, fator_ampliacao, fator_ampliacao)
    
    # ==========================
    # APRESENTAÇÃO DOS RESULTADOS
    # ==========================
    fig = plt.figure(figsize=(12, 8))
    
    # Redução
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img_red_nn)
    ax1.set_title(f"Redução ({fator_reducao}x)\nVizinho Mais Próximo")
    ax1.axis("off")
    
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(img_red_bil)
    ax2.set_title(f"Redução ({fator_reducao}x)\nBilinear")
    ax2.axis("off")
    
    # Ampliação
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.imshow(img_amp_nn)
    ax3.set_title(f"Ampliação ({fator_ampliacao}x)\nVizinho Mais Próximo")
    ax3.axis("off")
    
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.imshow(img_amp_bil)
    ax4.set_title(f"Ampliação ({fator_ampliacao}x)\nBilinear")
    ax4.axis("off")
    
    plt.tight_layout()
    plt.show()

