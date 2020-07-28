
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']
print({list1[each]:list2[each] for each in range(min(len(list1),len(list2)))})
