#Ejercicio 3 Examen Final
#Julio Gianni Martínez Cruz A01732382

nodos= '12345678'
x = '-'
M= [[x,1,2,x,x,x,x,x],\
    [x,x,1,5,2,x,x,x],\
    [x,x,x,2,1,4,x,x],\
    [x,x,x,x,3,6,8,x],\
    [x,x,x,x,x,3,7,x],\
    [x,x,x,x,x,x,5,2],\
    [x,x,x,x,x,x,x,6],\
    [x,x,x,x,x,x,x,x]]
    #1 2 3 4 5 6 7 8

m = '*'+nodos+'\n'
for f in range(len(M)):
    m += nodos[f]
    for c in range(len(M)):
        if f != c:
            m += str(M[f][c])
        else:
            m += "*"
    m += '\n'
    
print ("Matriz de conexiones: ")
print(m)

corta = [[0,0,0]]*len(M)
dists = [0]*len(M)
for j in range (1,len(M)):
    pos = []
    for i in range(0,len(M)):
        if M[i][j] !=x:
            dis = dists[i] + M[i][j]
            pos.append([dis,nodos[i],nodos[j]])
            
    corta[j] = min(pos)
    dists[j] = corta[j][0]
    
line = corta[-1]
s = '8'
let ='8'
while let != '1':
    p = line[1]
    for q in corta:
        if q[2] == p:
            s = q[2]+'-'+s
            line = q
    
    let = line[1]
s = '1-'+s

print("Nodos de la ruta más corta: ",s)
print("Distancia total: ", corta[-1][0])
