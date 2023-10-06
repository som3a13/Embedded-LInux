import os
def writer():
    mypath=os.path.dirname(os.path.realpath(__file__))+"/init.c"
    fd=open(mypath,'a')
    bits="0b"+user_selection() #callback function :o
    init=f"void Init_PORTA_DIR(void){{\n\
    DDRA= {bits} ;\n\
    }}\n\
    "   
    print(init)
    fd.write(init)
    fd.close

def user_selection():
    list=[]
    for i in range(0,8):
        while True:
            user_input=input(f"Please enter bit {i} mode:")
            if user_input=="in":                               
                list.append(0)
                break
            elif user_input=="out":
                list.append(1)
                break
            else:
                print("please enter valid direction")
                
    #Reverse bits , and join them to be in string           
    list.reverse()
    bits=''.join(map(str,list))
    return bits

writer()


