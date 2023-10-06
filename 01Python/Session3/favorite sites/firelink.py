import webbrowser

def firefox(url,num):
    if num<=3:
        webbrowser.get("firefox").open(url[num])
    else:
        print("Please choose form 0 to 3.")