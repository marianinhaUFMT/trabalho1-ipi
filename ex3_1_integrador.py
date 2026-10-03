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
# TODO: importar as funções necessárias dos outros arquivos (ex.: limiarizar, filtro_box, ...)


def etapa_1_escolha_do_canal(img_bgr):
    # TODO: decidir qual representação separa melhor o boi (branco) do pasto (verde)
    # TODO: testar cinza, canais B/G/R separados e saturação (HSI/HSV)
    # TODO: comparar os histogramas de cada opção e escolher o de vale mais claro
    pass


def etapa_2_pre_processamento(img):
    # TODO: decidir se precisa de suavização ou ajuste de contraste antes de limiarizar
    # TODO: justificar o filtro e o tamanho de janela escolhidos
    pass


def etapa_3_limiarizacao(img):
    # TODO: escolher o T (justificar pelo histograma)
    pass


def etapa_4_remocao_objetos_pequenos(img_bin):
    # TODO: definir como eliminar objetos pequenos usando só métodos da disciplina
    #       (ex.: borrar a binária e limiarizar de novo; ou reduzir/ampliar a imagem)
    # TODO: decidir como tratar a mata no topo da imagem
    pass


def executar():
    # TODO: ler a imagem original (arquivo original fornecido pelo professor)
    # TODO: executar as etapas na ordem escolhida
    # TODO: exibir e salvar o resultado de CADA etapa em resultados/
    # TODO: imprimir os parâmetros usados em cada etapa
    pass


if __name__ == "__main__":
    executar()

# ANÁLISE (para a apresentação):
# TODO: contar manualmente os objetos na imagem final
# TODO: comparar com a imagem de referência
# TODO: discutir bois de interesse que NÃO foram preservados (e por quê)
# TODO: discutir objetos pequenos ou indesejados que permaneceram (e por quê)
# TODO: justificar a ordem das etapas
