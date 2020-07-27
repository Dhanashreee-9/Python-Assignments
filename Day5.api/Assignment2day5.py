
list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
print("Unordered list:",list3)
new_list=[]
while list3:
    min = list3[0]  
    for x in list3: 
        if x < min:
            min = x
    new_list.append(min)
    list3.remove(min)    

print("Ordered list:",new_list)



