import caesar_cipher


enciphered_caesar = caesar_cipher.encipher("my bank account password: grzibek", 4)
print(caesar_cipher.caesar_breaker(enciphered_caesar))

