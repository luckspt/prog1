def contarDigitos(n):
    if n < 0:
        n *= -1
    elif n == 0:
        return 1
        
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
        
    return cnt

def idxMaxPar(lista):
  maior = -1
  
  for idx in range(len(lista)):
    if lista[idx] % 2 == 0 and (maior == -1 or lista[idx] > lista[maior]):
        maior = idx

  return maior

def neutralizarSinais(s1, s2):
    nova = ''
    for idx in range(len(s1)):
        nova += s1[idx] if s1[idx] == s2[idx] else '0'
    return nova

def somaAcc(lista):
    comp = len(lista)
    if comp == 0:
        return []

    nova = [lista[0]]
    for idx in range(1, comp):
      nova += [nova[idx-1] + lista[idx]]
      
    return nova

def classificar(paisagem):
    pic = 0
    dep = 0
    
    for idx in range(1, len(paisagem)-1):
        ant = paisagem[idx-1]
        atu = paisagem[idx]
        pos = paisagem[idx+1]
        
        if atu > ant and atu > pos:
            pic += 1
        elif atu < ant and atu < pos:
            dep += 1
    
    if pic == 1 and dep == 0:
        return 'montanha'
    elif dep == 1 and pic == 0:
        return 'vale'
    else:
        return 'nenhum'

"""
def classificar(paisagem):
    maior = max(paisagem)
    menor = min(paisagem)
    pontas = [paisagem[0], paisagem[-1]]
    
    if paisagem.count(maior) == 1 and maior not in pontas:
        return 'montanha'
    if paisagem.count(menor) == 1 and menor not in pontas:
        return 'vale'
    else:
        return 'nenhum'
"""