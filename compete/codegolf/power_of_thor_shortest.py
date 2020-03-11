a,b,c = int,input,print
lx, ly, ix, iy = [a(i) for i in b().split()]


while True:
    rt = a(b())
    if ix < lx and iy < ly:
        c('SE')
        ix += 1
        iy += 1
    elif ix > lx and iy > ly:
        c('NW')
        ix -= 1
        iy -= 1
    elif ix > lx and iy < ly:
        c('SW')
        ix -= 1
        iy += 1
    elif ix < lx and iy > ly:
        c('NW')
        ix += 1
        iy -= 1
    elif ix < lx and iy == ly:
        c('E')
        ix += 1
        iy += 0
    elif ix > lx and iy == ly:
        c('W')
        ix -= 1
        iy += 0
    elif ix == lx and iy < ly:
        c('S')
        ix += 0
        iy += 1
    elif ix == lx and iy > ly:
        c('N')
        ix += 0
        iy -= 1