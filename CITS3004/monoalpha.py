# CITS 3004
# Name: Monoalphabetic Cypher
# Authors: Russell Ballestrini, Jin Hong, Alvaro Monsalve
# Last Update: 06 JUL 2021
# Requirements: Python 3.8

from string import ascii_letters, digits
from random import shuffle

def random_monoalpha_cipher():
    """Generate a Monoalphabetic Cipher
       Returns a dictionary of substitution table randomly generated
    """
    pool = ascii_letters + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))

def key_monoalpha_cipher(key):
    """Generate a Monoalphabetic Cipher using the key provided
       Returns a dictionary of substitution table using the key
    """

    #
    # TO DO
    #

    return 0

def inverse_monoalpha_cipher(monoalpha_cipher):
    """Given a Monoalphabetic Cipher (dictionary) return the inverse."""
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha[value] = key
    return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
    """Encrypts message using the substitution table monoalpha_cipher"""
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    """Decrypts message using the substitution table monoalpha_cipher"""
    return encrypt_with_monoalpha(
               encrypted_message,
               inverse_monoalpha_cipher(monoalpha_cipher)
           )

#Example usage
message = 'this is a secret message'
key = 'pineapple'
print('Message is: ', message)
#print('key is: ', key)
cipher = random_monoalpha_cipher()
#cipher = key_monoalpha_cipher(key)
ciphertext = encrypt_with_monoalpha(message, cipher)
print('Encrypted Message is: ', ciphertext)
plaintext = decrypt_with_monoalpha(ciphertext, cipher)
print('Decrypted Message is: ', plaintext)