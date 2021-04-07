import math

def distancia(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def sugerirCentroide(centros, pt):
    m = [0, distancia(centros[0], pt)]
    for i in range(1, len(centros)):
        dist = distancia(centros[i], pt)
        if dist < m[1]:
            m[0] = i
            m[1] = dist

    return m[0]

def encontrarCentroMassa(pts):
  x = sum([x[0] for x in pts]) / len(pts)
  y = sum([x[1] for x in pts]) / len(pts)
  
  return (x, y)

def aglomerar(k, pts, tol=0.001, maxIter=500):
    ant = pts[:k]
    atu = ant[:]
  
    i = 0
    while i < maxIter:
        # Associar aos centroides mais prox
        proximos = [[] for x in range(len(ant))]
        for pt in pts:
            proximos[sugerirCentroide(ant, pt)].append(pt)
        
        # Calc centro massa
        atu = [encontrarCentroMassa(proximos[x]) for x in range(len(ant))]
        
        # Ver se estão mto proximos
        soma = sum([distancia(ant[x], atu[x]) for x in range(len(ant))])
        if soma < tol:
            i = maxIter
            break
        
        # Incrementos e tal
        ant = atu[:]
        i += 1
      
    return atu  

def custear(centros, pts):
    return sum([distancia(centros[sugerirCentroide(centros, pt)], pt)**2 for pt in pts])

def sugerirK(pts, minK=2, maxK=10):
    """
    requires: minK >= 2
    requires: minK < maxK
    """
    res = [None, None]
    while minK <= maxK:
      centros = aglomerar(minK, pts)
      custo = custear(centros, pts) * minK ** 1.5
      
      if res[1] is None or custo < res[1]:
        res[0] = minK
        res[1] = custo
      
      minK += 1
      
    return res[0]