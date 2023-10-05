
list=[1,2,3,4,4,5,4,4,4,4,4,4,4,6,7,8,4,4,4,4,4,4,4,4]

result=list.count(4)
print(f"Number 4 was found '{result} times' in the list")

# C Soul :D 
def counter(list):
    counter=0
    for i in list:
        if i ==4 :
            counter+=1

    return counter
print(f"Number 4 was found '{counter(list)} times' in the list")

