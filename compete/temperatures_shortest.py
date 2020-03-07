z,p,w,u,s = input,print,min,int,abs
n = u(z())
v = []
for i in z().split():
    t = u(i)
    v.append(t)
q = []
for i in v:
    q.append(s(0-i))
try:
    if q.count(w(q)) > 1:
        _a = []
        _min = v[q.index(w(q))]
        for i in range(len(q)):
            if s(_min) == s(v[i]):
               _a.append(i)
        p(max([v[x] for x in _a]))
    else:
        p(v[q.index(w(q))])
except:
    p(0)