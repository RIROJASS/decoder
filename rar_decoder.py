# decoder.py
def print_menu():
    print("Menu")
    print("-------------")
    print("2. Decode")
    print("3. Exit")

def decode_password(encoded_password):
    original_password = ''
    encoded_password = str(encoded_password)
    for num in encoded_password:
        num = int(num)
        num -= 3
        original_password += str(num % 10)  # Ensure digits wrap around below 0

    return int(original_password)

def main():
    while True:
        print_menu()
        option = input("Please enter an option: ")
        if option == "2":
            password_to_decode = int(input("Please enter your password to decode: "))
            decoded_password = decode_password(password_to_decode)
            print("Your password has been decoded and restored!")
            print(f"Original password: {decoded_password}")
        elif option == '3':
            break

if __name__ == "__main__":
    main()
