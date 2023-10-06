import firelink


def main():
    while True:
        list_websites=["https://www.youtube.com","https://www.facebook.com","https://www.linkedin.com","https://www.github.com"]
        num=int(input("Choose a website to open:\n0:YOutube\n1:facebook\n2:linkeding\n3: GItHub\nYour Choice:\n"))
        firelink.firefox(list_websites,num)


if __name__ == "__main__":
    main()