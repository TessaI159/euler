# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using data/euler59_input.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

from euler import read_input
from string import ascii_lowercase
from decorator import time_and_memory_decorator as tamd
import inspect




# >>> from lingua import Language, LanguageDetectorBuilder
# >>> languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
# >>> detector = LanguageDetectorBuilder.from_languages(*languages).build()
# >>> detector.detect_language_of("languages are awesome")


filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

# Common words is a list of the 80 most common words in the English language
with open("data/common_words.txt") as fptr:
        common_words = fptr.readlines()

common_words = [x.strip() for x in common_words]
useless_characters = '+!@#$%^&*()-;:><{}'


# Obviously, this took some human intervention to figure out
def legible(text):
    if text[:10] == 'An extract':
        return True
    return False


def decode(secret, key):
    # Secret is a list of numbers representing ASCII characters
    # Key is a list of three lowercase letters representing our key

    decoded = ''
    for index, char in enumerate(secret):
        decoded += chr(ord(key[index % 3]) ^ char)
    

    for word in decoded.split(' '):
        if word in common_words:
            return decoded


def naive_answer():
    # The key is exp
    # Input data is a list of integers representing ASCII characters
    input_data = read_input(filename)
    input_data = ''.join(input_data)
    input_data = input_data.split(',')
    input_data = [int(num) for num in input_data]
    

    alphabet = ascii_lowercase
    # Loop through every three letter combination of lowercase letters
    for letter1 in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                if (decoded := decode(input_data, [letter1, letter2, letter3])):
                    if legible(decoded):
                        return decoded
                


@tamd
def find_answer():
    answer = 0
    for character in naive_answer():
        answer += ord(character)
    return answer


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
