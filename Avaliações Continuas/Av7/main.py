def pivotSoma(lista):
    somaEsq = 0
    somaDir = sum(lista)
    
    for i, x in enumerate(lista):
        somaDir -= x
        if somaEsq == somaDir:
            return i
        somaEsq += x
    return -1

grelha = [
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"] ]
  
def mostrarGrelha(grelha):
  print('\n'.join([''.join(['{:3}'.format(str(item)) for item in linha]) 
                   for linha in grelha]))

def inc(grelha, l, c, comp, alt):
    indices = [
        (l-1, c-1), (l-1, c), (l-1, c+1),
        (l, c-1)  ,           (l, c+1)  ,
        (l+1, c-1), (l+1, c), (l+1, c+1) ]
        
    for i in indices:
        x, y = i
        if x < 0 or y < 0 or x >= alt or y >= comp or grelha[x][y] == '#':
            continue
        grelha[x][y] += 1

def minesweeper(grelha):
    mat = [ [ col if col == '#' else 0 for col in lin] for lin in grelha]
    
    comp = None
    alt = len(grelha)
    for l, lin in enumerate(grelha):
        if comp == None:
            comp = len(lin)
            
        for c, col in enumerate(lin):
            if col == '#':
                inc(mat, l, c, comp, alt)
    return mat

s = "50515253"  # exemplo de string

def contarAscendente(s):
    compTot = len(s)
    comp = 1
    prox = int(s[0]) + 1
    i = 1
    res = False
    while i < compTot:
        lenAtu = len(str(prox))
        atu = int(s[i:i+lenAtu])
    
        if atu == prox:
            prox = atu + 1
            comp = lenAtu
            i += comp
            res = True
        else:
            comp += 1
            prox = int(s[0:comp]) + 1
            i = comp
            res = False
            
    return res