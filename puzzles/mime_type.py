""" Print the mimetype of the file """
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    d[ext] = mt
e = {}
for k, v in d.items():
    e[k.lower()] = v
    
a = []
for i in range(q):
    fname = input().lower().split('.')  # One file name per line.
    a.append(fname)
    if len(fname) == 1:
        print('UNKNOWN')
    elif fname[-1] in e.keys():
        print(e[fname[-1]])
    else:
        print('UNKNOWN')