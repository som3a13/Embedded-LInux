#Using sort

list=[4,5,8,20,40,10,12,8,199,60,100,55,88,170,99]

sortedlist=list.sort() # from low to high number
largest=(list[-1]) # assign last element in largest 

print(f"largest number in list = {largest}")

#using Loop

def search(list):
    largest=list[0]
    for i in list:
        if i > largest:
            largest=i
    return largest
print(f"largest number in list = {search(list)}")

