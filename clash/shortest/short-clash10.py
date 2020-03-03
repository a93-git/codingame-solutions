""" Modify the input url"""
p,u,f,h = print,input(),'ftp://','http://'
if (h in u or 'https://' in u or f in u):
    p(u)
elif '.' in u:
    p('{0}{1}'.format(h,u))
else:
    p('{0}{1}'.format(f,u))