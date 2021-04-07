def ordenarTriplo(a, b, c):
    lista = []
    if a > b:
        lista = [a, b]
    else:
        lista = [b, a]
    
    for i in range(2):
        if c >= lista[i]:
            lista.insert(i, c)
            break
        
    if len(lista) != 3:
        lista.append(c)
    return tuple(lista)

def mediana(lista):
    comp = len(lista)
    if comp % 2 == 0:
        return float((lista[comp // 2 - 1] + lista[comp // 2]) / 2)
    else:
        return float(lista[comp // 2])

def numDigitos(n):
    if n == 0:
        return 0
    return 1 + numDigitos(n // 10)

def minimo(xs):
    comp = len(xs) 
    if comp == 0:
        return []
        
    cabeca = xs[0]
    if comp == 1:
        return cabeca
        
    res = minimo(xs[1:])
    return cabeca if cabeca<res else res

def apenas_5_3(num):
    if num in (5, 3):
        return True
    if num < 5:
        return False
    
    if num % 3 == 0:
        if(apenas_5_3(num / 3)):
            return True
    
    return apenas_5_3(num - 5)    