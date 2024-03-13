from understandability_checker import is_understandable

def encipher(text, shift):

    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_breaker(ciphered_text):

    possible_hits = []
    for key_shift in range(26):
        deciphered_text = encipher(ciphered_text, key_shift)
        if is_understandable(deciphered_text):
            possible_hits.append(deciphered_text)

    return possible_hits

