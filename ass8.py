def sort_as_firstElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[0]))
def sort_as_secondElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[1]))
def sort_as_lastElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[-1]))

tuple_list=[(2,'cat',890,50),(1,'dog',203,10),(5,'apple',332,40),(4,'xyz',110,20),(3,'boll',421,30)]
#a=int(input("Enter How many tuple list you want to Enter :"))
print("Orriginal List=",tuple_list)
print("Sort according to last Element =",sort_as_lastElement_list(tuple_list))
print("Sort according to 2nd Element =",sort_as_secondElement_list(tuple_list))
print("Sort according to 1st Element =",sort_as_firstElement_list(tuple_list))
