def separa_a_frase_numa_lista_de_palavras(texto):
    lista = texto.split(" ")
    return lista


def gera_string_com_a_ordem_inversa_de_uma_lista(lista):
    i = len(lista)
    texto_invertido = ""

    for p in lista:
        i -= 1
        texto_invertido = texto_invertido + lista[i] + " "

    # remove o ultimo espaço em branco deixado na concatenação
    texto_invertido = texto_invertido[:len(texto_invertido)-1]

    return texto_invertido


def recebe_uma_frase_e_inverte_a_ordem_das_palavras(frase):
    lista = separa_a_frase_numa_lista_de_palavras(frase)
    frase_invertida = gera_string_com_a_ordem_inversa_de_uma_lista(lista)
    return frase_invertida


frase = input("Digite uma frase: ")

print(recebe_uma_frase_e_inverte_a_ordem_das_palavras(frase))
