str1="What we think we become; we are python programmers."
len(str1)
substring = "we"

index=str1.find(substring,0,7)
index1=str1.find(substring,7,23)
index2=str1.find(substring,23,51)
count = str1.count(substring, 0, 51)

# print index and count
print("The index of first 'we' in string is:", index)
print("The index of second 'we' in string is:", index1)
print("The index of third 'we' in string is:", index2)
print("The count of occurance of 'we' in string is:", count)