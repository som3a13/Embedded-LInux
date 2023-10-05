user_input= input("PLease enter a letter : ")
voel_set={'a','e','i','o','u'}

def voel_finder():
    if user_input in voel_set:
        print("voel is founded")
    else:
        print("voel not founded")

voel_finder()