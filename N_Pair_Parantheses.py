def getParanthesesCombinations(s) :


    if s=='()' :
        return ['()']

    prefix='()'
    rest=s[2:]


    perms=getParanthesesCombinations(rest)
    out=set()


    for p in perms :


        for i in range(0,len(p)+1) :
            new=p[0:i]+prefix+p[i:]
            out.add(new)


    return out


print getParanthesesCombinations('()()()')
