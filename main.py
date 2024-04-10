def encoder(password):        #Ally Seiverd
    new_password=""
    for char in password:
        x=int(char)+3
        new_password+=str(x)

    return new_password

def decoder(new_password):
    password=''
    for char in new_password:
        y = int(char)-3
        password += str(y)
    return password

def main():
    while True:
        print("Menu","\n-------------","\n1. Encode","\n2. Decode","\n3. Quit")
        choice=int(input("\nPlease enter an option: "))
        if choice==1:
            password=input("Please enter your password to encode: ")
            encoded=encoder(password)
            print("Your password has been encoded and stored!")
            print()
        if choice == 2:
            decoded = decoder(encoded)
            print("The encoded password is " +str(encoded) + ", and the original password is " +str(decoded) + ".")
        if choice==3:
            break
if __name__=="__main__":
    main()




