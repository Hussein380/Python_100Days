alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(caeser_text, shift_amount, caeser_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for lette rin text:
        position = alphabet.index(leetter)
        new_position = position + shift_amount
        The_caeser += alphabet[new_position]

    print(f"The {direction}d text is : {end_text}")

caeser(caeser_text=text, shift_amount=shift, ciper_direction=direction)

"""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in
    new_code = ""
    
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_code += new_letter
    print(f"The encoded text is {new_code}")
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def decrypt(cypher_text, shift_amount):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
       """ new_text _= alphabet[new_position]
    print(f"The decoded text is {new_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(cypher_text = text, shift_amount = shift)

"""
