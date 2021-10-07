n=int(input('introdu valoarea lui n: '))
matrice=[]
if n>10 or n<2:
    print('eroare')
else:
    c=[] #elementele de pe diagonala principala a matricei
    d=[] # elementele de pe diagonala secundara
    e=[] #elementele de mai sus de diagonala principala
    f=[] #elementele de mai jos de diagonala principala
    b=[] #elementele de sus mai de diagonala secundara
    g=[] #elementele de mai jos de diagonala secundara
    for l in range(0, n):
        a=[]
        for m in range(0, n):
            z=int(input('Introdu elementul: '))
            a.extend([z])
        matrice.append(a)
    print(matrice)
    for i in range(0, n):
        for j in range(0, n):
            if i-j==0:
                c.append(matrice[i][j])
            if i+j==len(matrice[0])-1:
                d.append(matrice[i][j]) 
            if i<j:
                e.append(matrice[i][j])
            if i>j:
                f.append(matrice[i][j])
            if i+j<len(matrice[0])-1:
                b.append(matrice[i][j])
            if i+j>len(matrice[0])-1:
                g.append(matrice[i][j])
    
    print('diagonala principala : ', c)
    print('suma elementelor de pe diagonala principala este: ', sum(c))
    print('elemente de pe diagonala secundara: ', d)
    print('suma elementelor de pe diagonala secundara este: ', sum(d))
    print('elementele de deasupra diagoalei principale', e)
    print('suma elementelor de mai sus de diagonala principal: ', sum(e))
    print('elementele de mai jos de diagonala principala: ', f)
    print('suma elementelor de mai jos de diagonala ', sum(f))
    print('elementele de situate deasupra diagonalei secundare ', b)
    print('suma elemenelor de deasupra diagonalei secundare: ', sum(b))
    print('elementele de sub diagonala secundara: ', g)
    print('suma elementelor de sub diagonala secundara: ', sum(g))