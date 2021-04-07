import re

def carregarVocabulario(filename):
  dic = set()
  for line in open(filename, 'r', encoding='utf8'):
    dic.add(line.rstrip().lower())
  return sorted(dic)

dic = carregarVocabulario('vocabulario.txt')

def gerarPalavras(texto):
    nlista = re.split('[ \n,.()[\]!?:;"#$%&/={}\d\\\_\-<>*+«»]', texto)
    return [x for x in nlista if len(x)]

def mmLetras(palavra1, palavra2):
    cnt = 0
    compmin = min(len(palavra1), len(palavra2))
    compmax = max(len(palavra1), len(palavra2))
    
    for idx in range(compmin):
        if palavra1[idx] == palavra2[idx]:
            cnt += 1
    return compmax - cnt

def minPalavra(mat, x, y, custo):
    testes = ( (x-1, y-1, custo), (x-1, y, 1), (x, y-1, 1))

    minimo = None    
    for a, b, custo in testes:
        if a < 0 or b < 0 or a > len(mat) or b > len(mat[a]):
            continue
        calc = mat[a][b] + custo
        if minimo == None or calc < minimo:
            minimo = calc
    return minimo

def edicoes(palavra1, palavra2):
    mat = [[0]]
    for x in range(1, len(palavra2)+1):
        mat[0].append(x)
    for x in range(1, len(palavra1)+1):
        mat.append([x])
    
    for p1 in range(1, len(palavra1)+1):
        for p2 in range(1, len(palavra2)+1):
            custo = int(palavra1[p1-1] != palavra2[p2-1])
            mat[p1].append(minPalavra(mat, p1, p2, custo))
    return mat[-1][-1]

def sugerir(dic, palavra, distancia, maxSugestoes=5):
    lista = [[i, pal, distancia(palavra, pal)] for i,pal in enumerate(dic)]
    lista = sorted(lista, key = lambda x: x[2])
    
    escolhidas = lista[:maxSugestoes]
    escolhidas = sorted(escolhidas, key = lambda x: x[0])
    
    return [el[1] for el in escolhidas]

def corretor(dic, texto, distancia, maxSugestoes=5): 
    for p in gerarPalavras(texto):
        if p in dic:
            continue
        
        sugestoes = sugerir(dic, p, distancia, maxSugestoes)
        print(f'{p} --> {str(sugestoes)}')