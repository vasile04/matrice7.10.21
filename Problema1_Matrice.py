x=[[1, 2, 3, 4, 5],
[45, 23, 67, 100, 101], 
[99, 78, 21, 789, 0], 
[55, 88, 34, 82, 12],
[112, 465, 785, 2345, 586]]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
w=[]
for i in x:
    c.extend(x[0])
    d.extend(x[1])
    e.extend(x[2])
    f.extend(x[3])
    g.extend(x[4])
print('suma de pe primul rand este: ', sum(c))
print('suma de pe al doilea rand este: ', sum(d))
print('suma de pe al treilea rand este: ', sum(e))
print('suma de pe al patrulea rand este: ', sum(f))
print('suma de pe al cincilea rand este: ', sum(g))

for i in range(len(x)):
    for j in range(len(x[0])):
        if i-j==0:
            h.append(x[i][j])
        if i+j==len(x[0])-1:
            w.append(x[i][j])    
print( 'diagonala principala', h)
print('diagonala secundara', w)