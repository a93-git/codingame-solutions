""" Print the morse code equivalent of a 10-digit mobile number and 'Untransformable' otherwise"""

mn=input()
c={'1':'.----','2':'..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','0': '-----'}
u='Untransformable'
if len(mn)==10:
    try:
        r=''
        for i in mn:
            r=r+' '+ c[i]
    except:
        r=u
else:
    r=u
print(r.strip())