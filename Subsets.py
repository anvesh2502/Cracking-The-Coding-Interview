

def getAllSubsets(l,size=0,subsets=[],element_index=dict()) :

    if size==len(l) :
        return subsets

    if size==0 :
        i=0
        for v in l :
            element_index[v]=i
            subsets.append([v])
            i+=1




    else :

        for i in range(0,len(subsets)) :

            if len(subsets[i])!=size :
                continue

            last=subsets[i][-1]
            index=element_index[last]
            index+=1
            while index<len(l) :
                subsets.append(subsets[i]+[l[index]])
                index+=1


    return getAllSubsets(l,size+1,subsets,element_index)


l=[1,2,3,4,5,6]
print len(getAllSubsets(l))
