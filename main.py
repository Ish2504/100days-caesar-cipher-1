alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
import math
def encrypt(text, shift):


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

  text_list = []
  for x in text:
    text_list.append(x)

 
  text_alphabet_index = []

  for x in text_list:

    text_alphabet_index.append(alphabet.index(x))

  encoded_text_index = []

  for x in text_alphabet_index:
    if x + shift > 25:
      new_x = abs((25 - x) - (shift - 1))
      encoded_text_index.append(new_x)
    else:
      encoded_text_index.append(x + shift)


  new_encoded_text = []

  for x in encoded_text_index:
    new_encoded_text.append(alphabet[x])

  print(new_encoded_text)

  cipher_text = ''.join(new_encoded_text)


  print(f"The encoded text is {cipher_text}") 

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)