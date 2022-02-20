from itertools import combinations

input = 'Ifailuhkqq'
input = 'banana'
input = input.lower()


# https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python
# https://www.geeksforgeeks.org/permutation-and-combination-in-python/
def stringValue(input):
    soma = 0
    for c in input:
        soma += ord(c)
    return soma


class Substring:
    def __init__(self, letters=0, checkSum=0, position=0):
        self.letters = letters
        self.checkSum = checkSum
        self.position = position


def getSubstring(input, tamanho, posiLetra, dir, iter):
    passo = (posiLetra - iter) if (dir == 'e') else (posiLetra + iter)
    if (passo < tamanho and 0 <= passo):
        substring = input[passo:posiLetra + 1] if (dir == 'e') else input[posiLetra:passo + 1]
        posiSubstring = list(range(passo, posiLetra + 1)) if (dir == 'e') else list(range(posiLetra, passo + 1))
        return Substring(substring, stringValue(substring), posiSubstring)
    else:
        return None


def solucao(input, type=0):
    # if type = 0, não se aceita palavras iguais
    # if type = 1, é aceito palavras iguais
    type = False if (type == 0) else True
    resposta = dict()
    ocorrencias = dict()
    tamanho = len(input)
    for i, c in enumerate(input):
        if (c in ocorrencias.keys()):
            ocorrencias[c].append(i)
        else:
            ocorrencias[c] = [i]
    for k, v in ocorrencias.items():  # key, value for each dict entry
        if (len(v) > 1):
            resposta[k, k] = [v]
            # iterar a letra 'k' na palavra
            start = 0
            stop = 1
            while (True):
                iter = 1
                while (True):
                    posiLetraEsq = v[
                        start]  # Posição, na palavra, da ocorrência mais a esquerda da 'k' letra na palavra
                    posiLetraDir = v[stop]  # Posição, na palavra, da ocorrência mais a direita da 'k' letra na palavra
                    startLeft = getSubstring(input, tamanho, posiLetraEsq, 'e', iter)
                    stopLeft = getSubstring(input, tamanho, posiLetraDir, 'e', iter)
                    startRight = getSubstring(input, tamanho, posiLetraEsq, 'd', iter)
                    stopRight = getSubstring(input, tamanho, posiLetraDir, 'd', iter)
                    temp = [startLeft, stopLeft, startRight, stopRight]
                    if (temp.count(None) >= 3):
                        break
                    comb = list()
                    for t in temp:
                        if (t):  # checa se t NÃO é None, e ai adiciona a lista
                            comb.append(t)

                    comb = combinations(comb, 2)
                    for c in comb:
                        if ((c[0].checkSum == c[1].checkSum) and ((c[0].letters != c[1].letters) or type)):
                            add = True
                            for key in resposta.keys():
                                if (c[0].letters in key and c[1].letters in key):
                                    add = False
                            if (add):
                                resposta[c[0].letters, c[1].letters] = [c[0].position, c[1].position]
                    iter += 1
                if (stop < len(v) - 1):
                    stop += 1
                elif (start < stop - 1):
                    start += 1
                else:
                    break
    return resposta


resposta = solucao(input)
print(resposta)