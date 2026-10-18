"""
2.1b - Ajuste de contraste em imagem RGB preservando as cores
Saída esperada: imagem original + imagem resultante + justificativa da estratégia.
Base possível: rgb_hsi_conv.py e 04_contraste_partes.py (do professor).
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

    cv2.putText(
        img,
        text,
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        cor,
        2
    )

    return img

def hsi_2_rgb(img_hsi: np.ndarray)-> np.ndarray:
    img_hsi = img_hsi.astype(np.float64) / 255
    
    H = img_hsi[ :, :, 0] * 2 * np.pi
    S = img_hsi[ :, :, 1]
    I = img_hsi[ :, :, 2]

    R = np.zeros(H.shape)
    G = np.zeros(H.shape)
    B = np.zeros(H.shape)

    rad_120 = 2 * np.pi / 3
    rad_240 = 2 * rad_120
    rad_360 = 3 * rad_120
    rad_60  = rad_120 / 2
    
    # 0 <= H < 120
    mask = (H < rad_120)
    B[mask] = I[mask] * (1 - S[mask])
    R[mask] = I[mask] * (1 + ( (S[mask] * np.cos(H[mask]) / np.cos(rad_60 - H[mask])) ) )
    G[mask] = 3 * I[mask] - (R[mask] + B[mask])
    
    # 120 <= H < 240
    mask = ((H >= rad_120) & (H < rad_240))
    H[mask] = H[mask] - rad_120
    R[mask] = I[mask] * (1 - S[mask])
    G[mask] = I[mask] * ( 1 + (S[mask] * np.cos(H[mask]) / np.cos( rad_60 - H[mask] )) )
    B[mask] = 3 * I[mask] - (R[mask] + G[mask])

    # # 240 <= H < 360
    mask = (H >= rad_240)
    H[mask] = H[mask] - rad_240
    G[mask] = I[mask] * (1 - S[mask])
    B[mask] = I[mask] * (1 + (S[mask] * np.cos(H[mask]) / np.cos(rad_60 - H[mask])))
    R[mask] = 3 * I[mask] - (G[mask] + B[mask])

    img_cor = np.stack((R, G, B), axis=2)*255.0
    img_cor = np.clip(img_cor, 0, 255)

    return  (img_cor).astype(np.uint8)

def rgb_2_hsi(img: np.ndarray)-> np.ndarray:
    img = img.astype(np.float64) / 255.0

    R = img[ :, :, 0]
    G = img[ :, :, 1]
    B = img[ :, :, 2]

    # intensidade
    I = (R + G + B) / 3

    # Saturacao
    min_rgb = np.min(img, axis=2)
    S = 1 - ( 3 / (R + G + B + 1e-6) * min_rgb)

    # matriz Hue
    numerador = ( (R - G) + (R - B) ) / 2
    denominador = np.sqrt( (R - G)**2 + ((R - B) * (G - B)) )
    H = np.arccos( numerador / (denominador  + 1e-6))
    H[B > G] = 2 * np.pi - H[B > G]
    H = H / (2 * np.pi)

    img_hsi = np.stack((H, S, I), axis=2)
    return  (img_hsi * 255).astype(np.uint8)

def contraste_partes(img: np.ndarray)->np.ndarray:
    img_out = img.astype(np.float64)
    r_min = img.min()
    r_max = img.max()
    img_out = (255 / (r_max - r_min)) * (img_out - r_min)
    img_out = np.clip(img_out, 0, 255)
    return img_out.astype(np.uint8)

def contraste_cor(img_bgr: np.ndarray) -> np.ndarray:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_hsi = rgb_2_hsi(img_rgb)

    # so canal I
    img_hsi[ :, :, 2] = contraste_partes(img_hsi[:, :, 2])

    img_rgb_out = hsi_2_rgb(img_hsi)

    return cv2.cvtColor(img_rgb_out, cv2.COLOR_RGB2BGR)


if __name__ == '__main__':
    img = cv2.imread('images/colour_stream_dark.tif', cv2.IMREAD_COLOR)

    img_resultado = contraste_cor(img)

    out = cv2.hconcat([add_title(img, "Original"), add_title(img_resultado, "Contraste RGB Uniforme")])
    cv2.namedWindow('Comparativo 2.1.b', cv2.WINDOW_NORMAL)
    cv2.imshow('Comparativo 2.1.b', out)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# JUSTIFICATIVA (escrever no README ou falar na apresentação):
# TODO: explicar por que ajustar R, G e B separadamente altera a cor (muda as proporções)
# TODO: explicar por que ajustar só a intensidade (I) preserva matiz e saturação
# TODO: comentar o efeito do clip na volta para RGB (pixels fora do gamut mudam de cor)
