B,W,R,L,p,o,q='BLOCK','WAIT','RIGHT','LEFT',print,int,input
a, b, c, d, e, f, g, h = [o(i) for i in q().split()]

i = {}
for r in range(h):
    j, k=[o(j) for j in q().split()]
    i[j]=k
while True:
    l,m,n=q().split()
    l=o(l)
    m=o(m)
    if m==b - 1 or m==0: p(B)
    else:
        if(l==d and m<e and n==L)or(l==d and m>e and n==R): p(B)
        try:
            p(B) if ((m>i[l] and n==R)or(m<i[l] and n==L)) else p(W)
        except:
            p(W)