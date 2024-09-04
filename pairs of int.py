def pair_sum(myList, Sum):
    # TODO
    result=[]
    
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==Sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result
pair_list=[2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(pair_sum(pair_list,7))