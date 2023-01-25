alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#An if statement can also be used within the function to achieve the same results.


def caesar(user_input, shift_number, direction):
    printed_text = ""

    if direction == 'decode':
        shift_number *= -1

    for letter in user_input:
        position = alphabet.index(letter)
        new_position = position + shift_number
        printed_text += alphabet[new_position]
    print(f"The {direction}d text is {printed_text}")


caesar(user_input=text, shift_number=shift, direction=direction)
