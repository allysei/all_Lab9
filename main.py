def encoder(password):        #Ally Seiverd
    new_password=""
    for char in password:
        x=int(char)+3
        new_password+=str(x)

    return new_password



def main():
    while True:
        print("Menu","\n-------------","\n1. Encode","\n2. Decode","\n3. Quit")
        choice=int(input("\nPlease enter an option: "))
        if choice==1:
            password=input("Please enter your password to encode: ")
            encoded=encoder(password)
            print("Your password has been encoded and stored!")
            print()
        if choice==3:
            break
if __name__=="__main__":
    main()




