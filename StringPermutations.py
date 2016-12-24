

def getStringPermutations(s) :

    if len(s)==0 : return perms

    if len(s)==1 : return s

    ch=s[0]
    s=s[1:]

    small_perms=getStringPermutations(s)
    perms=[]

    for p in small_perms :

        for i in range(0,len(p)+1) :
            perms.append(p[0:i]+ch+p[i:])


    return perms


s="abcde"
print len(getStringPermutations(s))
