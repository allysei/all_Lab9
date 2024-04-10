def encoder(password):
    new_password=""
    for char in password:
        x=int(char)+3
        new_password+=str(x)

    return new_password





