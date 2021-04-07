def noIntervalo(n, a, b):
    return a <= n and n <= b

def eRetangulo(a, b, c, d):
  return (a == b and c == d) or (a == c and b == d) or (a == d and b == c)

def somaKPotencias(k, xs, idx = 0):
  return sum([k * x**k for x in xs])

def ePangrama(txt):
    txt = txt.lower()
    aASCII = ord('a')
    for letra in range(0, 26):
        if chr(aASCII + letra) not in txt:
            return False
    return True

def meio(lst):
    return len(lst) // 2

def linhaPascal(linha):
    lst = [1, 1]
    
    for x in range(meio(linha)):
        prox = linha[x] + linha[x+1]
        meioLst = meio(lst)
        
        lst.insert(meioLst, prox)
        if x != meio(linha) - 1:
          lst.insert(meioLst, prox)
    return lst

