# Raul Rojas

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

def decode_password(encoded_password):
    original_password = ''
    encoded_password = str(encoded_password)
    for num in encoded_password:
        num = int(num)
        num -= 3
        if num < 0:
            num += 10  # Ensure digits wrap around below 0
        original_password += str(num)
    return original_password

# code from Brianna Vo
def encode_password(password):
    new_password = ''
    password = str(password)
    for num in password:
        num = int(num)
        num += 3
        if num > 9:
            num -= 10  # Ensure digits wrap around above 9
        new_password += str(num)
    return new_password

def main():
    encoded_password = None
    while True:
        print_menu()
        option = input("Please enter an option: ")
        if option == "1":
            password_to_encode = input("Please enter your password to encode: ")
            encoded_password = encode_password(password_to_encode)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password:
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is: {encoded_password}, and the original password is {decoded_password}")
            else:
                print("Please encode a password first.")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
