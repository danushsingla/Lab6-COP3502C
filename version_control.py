# Danush Singla - Encode
# Nicholas Blauz - Decode

def encode(password):               # encodes the password
    encoded_password = ""

    for character in password:      # goes through each character in the password string
        if int(character) >= 7:
            character = (int(character) + 3) - 10        # subtracts 10 to wrap the value around
            encoded_password += str(character)           # converts the character back into a string
        else:
            encoded_password += str(int(character) + 3)     # adds three to the character and returns as a string

    return encoded_password

def decode(encoded_password):
    original_password = ""

    for num in encoded_password:
        decoded_num = str((int(num) - 3) % 10)
        original_password += decoded_num

    return original_password

def print_menu():                    # prints the menu
    print("Menu")
    print("-"*13)
    print('1. Encode')
    print("2. Decode")
    print("3. Quit")
    print("")

    return int(input("Please enter an option: "))           # takes the input option


if __name__ == '__main__':
    encoded_password = ""                   # initializes the encoded password to be stored later

    while True:
        option = print_menu()

        if option == 1:                     # encodes
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")
        if option == 2:                     # decodes
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print("")
        if option == 3:
            quit()                          # quits the program