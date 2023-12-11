def encrypt(simple_str):
    encrypted_str = ""
    for i in simple_str:

            ascii_code_char = ord(i)
            modified_ascii_code_char = (ascii_code_char + 10 ) - 64 
            encrypted_str += chr(modified_ascii_code_char)

    return encrypted_str

def decrypt(simple_str):
    decrypted_str = ""
    for i in simple_str:

            ascii_code_char = ord(i)
            modified_ascii_code_char = (ascii_code_char - 10 ) + 64
            decrypted_str += chr(modified_ascii_code_char)

    return decrypted_str
    
print("\n\t\tENCRYPT : DECRYPT\n")

while(True):

    print("\n1 . Encrypt Text")
    print("2 . Decrypt Text")
    print("0 . Exit")

    input_choice = int(input("\nEnter Choice From Above ( 1 / 2 / 0 ) : "))

    if(input_choice == 1):

        print("\nEncrypt Text")

        simple_str = input("\nEnter Text You Want To Encrypt : ")

        print("Encrypted Text : " , encrypt(simple_str)) 

    elif(input_choice == 2):

        print("\nDecrypt Text")

        simple_str = input("\nEnter Text You Want To Decrypt : ")

        print("Decrypted Text : " , decrypt(simple_str))  

    elif(input_choice == 0):

        print("\nProgram Exited : Thanks For Using ")
        break

    else:
        print("\nPlease Enter '1' For Encryption , '2' For Decryption , '0' For Exit")