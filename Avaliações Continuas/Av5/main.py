def tribonacci(n, a=1, b=1, c=1):
    if n <= 2:
        return c
    return tribonacci(n-1, b, c, a+b+c)

def histograma(lista):
    if len(lista) == 0:
        return ''
    
    cabeca = lista[0]
    res = histograma(lista[1:])
    
    return f'{"*" * cabeca}\n{res}'

def kp(n, aux = 1, fat = 1):
    if fat % n == 0:
        return aux-1
    return kp(n, aux+1, fat*aux)

def nat(n):
    if n == 0:
        return []
    res = nat(n-1)
    return res + [res]

def seqPd(n, a=1, b=1, c=1):
    if n <= 2:
        return c
    return seqPd(n-1, b, c, a+b)