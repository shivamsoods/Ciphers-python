import numpy as np
import math
import gmpy2

def decryptCeaserCipher(encrypted_string, key):
    decrypted_string_output = []
    for char in encrypted_string:
        decrypted_char = chr(ord(char) - key)
        decrypted_string_output.append(decrypted_char)
    print("Encrypted text: "+ ''.join(decrypted_string_output),"\n")

def encryptCeaserCipher(normal_string, key):
    encrypted_string_output = []
    for char in normal_string:
        encrypted_char = chr(ord(char) + key)
        encrypted_string_output.append(encrypted_char)
    print("Plain Text: "+ ''.join(encrypted_string_output),"\n")



def encryptSubCipher(inp):
    
    # Initialise final encrypted string
    fin = ""
    # Loop through each character in the input
    for i in range(len(inp)):
        # If lowercase alphabet
        if inp[i].islower():
            # Perform mathematical transformation as required
            a = ord('a')
            x = ord(inp[i])
            fin += chr(a + 25 - (x - a))
        # Else if uppercase alphabet
        elif inp[i].isupper():
            # Perform mathematical transformation as required
            a = ord('A')
            x = ord(inp[i])
            fin += chr(a + 25 - (x - a))
        # Otherwise, do not change
        else:
            fin += inp[i]

    # Put encrypted string in the ciphertext text box
    print("Encrypted Text: "+fin+"\n")

def decryptSubCipher(inp):
    # Initialise final decrypted string
    fin = ""
    # Loop through each character in the input
    for i in range(len(inp)):
        # If lowercase alphabet
        if inp[i].islower():
            # Perform mathematical transformation as required (same as the encryption function)
            a = ord('a')
            x = ord(inp[i])
            fin += chr(a + 25 - (x - a))
        # Else if uppercase alphabet
        elif inp[i].isupper():
            # Perform mathematical transformation as required (same as the encryption function)
            a = ord('A')
            x = ord(inp[i])
            fin += chr(a + 25 - (x - a))
        # Otherwise, do not change
        else:
            fin += inp[i]

    # Put decrypted string in the plaintext text box
    print("Plain Text: "+ fin+"\n")



def modinv(f, m):
    assert isinstance(f, np.ndarray)
    assert isinstance(m, int)
    det = int(np.round(np.linalg.det(f)))
    det_inv = int(gmpy2.invert(det, m))  # throws ZeroDivisionError if no inverse matrices exist
    g = det_inv * np.round(det * np.linalg.inv(f)).astype(int) % m
    assert np.array_equal(f.dot(g) % m, np.identity(len(f), dtype=int))
    assert isinstance(g, np.ndarray)
    return g

def encryptHillCipher(plaintext,alphabet,key):

    stov = lambda s, alphabet: [alphabet.index(c) for c in s]
    vtos = lambda x, alphabet: ''.join([alphabet[i] for i in x])

    is_square = lambda n: int(math.sqrt(n)) ** 2 == n
    chunk = lambda s, n: [s[i:i+n] for i in range(0, len(s), n)]

    m = len(alphabet) # modulo
    n = int(math.sqrt(len(key)))
    f = np.array(chunk(stov(key, alphabet), n)) # n x n matrix

    ciphertext = ''
    for s in chunk(plaintext, n):
        x = np.array(stov(s, alphabet))
        y = np.dot(f, x) % m
        ciphertext += vtos(y.tolist(), alphabet)
    return ciphertext

def decryptHillCipher(ciphertext,alphabet,key):
    stov = lambda s, alphabet: [alphabet.index(c) for c in s]
    vtos = lambda x, alphabet: ''.join([alphabet[i] for i in x])

    is_square = lambda n: int(math.sqrt(n)) ** 2 == n
    chunk = lambda s, n: [s[i:i+n] for i in range(0, len(s), n)]
    
    m = len(alphabet) # modulo
    n = int(math.sqrt(len(key)))
    f = np.array(chunk(stov(key, alphabet), n))

    g = modinv(f, m)
    invkey = vtos(sum(g.tolist(), []), alphabet)
    return encryptHillCipher(ciphertext, alphabet, invkey)
   



def transform(text, key, want_decrypted=False):
    CHARS = [c for c in (chr(i) for i in range(65, 91))]
    res = ""
    for i, c in enumerate(text):
        if c not in CHARS:
            res += c
        else:
            text_index = CHARS.index(c)
            key_index = CHARS.index(key[i % len(key)])
            if want_decrypted:
                key_index *= -1
            res += CHARS[(text_index + key_index) % len(CHARS)]
    return res

def encryptVigenereCipher(text, key):
    return transform(text, key)

def decryptVigenereCipher(text, key):
    return transform(text, key, True)

while True:
    print("#"*50,"\n")
    print("Select option\n1.Ceaser Cipher \n2.Substitution Cipher \n3.Hill Cipher \n4.Vigenere Cipher \n5.Exit \n")
    print("Option-> ",end="")
    option=input()
    if option=="1":
        print("#"*50,"\n")
        print("Select Option\n1.Encypt Ceaser Cipher \n2.Decrypt Ceaser Cipher")
        print("Option-> ",end="")
        opt=input()
        print("\n")
        if opt =="1":
            encryptCeaserCipher(input("Enter Plain Text: "),int(input("Enter Shift Key: ")))
        elif opt=="2":
            decryptCeaserCipher(input("Enter Encrypted Text: "),int(input("Enter Shift Key: ")))    
        else:
            print("\n ####Select valid option!!#### \n")

    elif option=="2":
        print("#"*50,"\n")
        print("Select Option\n1.Encypt Substitution Cipher\n2.Decrypt Substitution Cipher")
        print("Option-> ",end="")
        opt=input()
        print("\n")
        if opt =="1":
            encryptSubCipher(input("Enter Plain Text: "))
        elif opt=="2":
            decryptSubCipher(input("Enter Encrypted Text: "))    
        else:
            print("\n ####Select valid option!!#### \n")

    elif option=="3":
        print("#"*50,"\n")
        print("Select Option\n1.Encypt Hill Cipher \n2.Decrypt Hill Cipher")
        print("Option-> ",end="")
        opt=input()
        print("\n")
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if opt =="1":
            cipherText=encryptHillCipher(input("Enter Plain Text: ").upper(),alphabet,input("Enter Key: ").upper())
            print("Cipher Text: "+cipherText+"\n")
        elif opt=="2":
            plainText=decryptHillCipher(input("Enter Encrypted Text: ").upper(),alphabet,input("Enter Key: ").upper())    
            print("Plain Text: "+plainText+"\n")
        else:
            print("\n ####Select valid option!!#### \n")

    elif option=="4":
        print("#"*50,"\n")
        print("Select Option\n1.Encypt Vigenere Cipher \n2.Decrypt Vigenere Cipher")
        print("Option-> ",end="")
        opt=input()
        print("\n")
        if opt =="1":
            cipherText=encryptVigenereCipher(input("Enter Plain Text: ").upper(),input("Enter Key: ").upper())
            print("Cipher Text: "+cipherText+"\n")
        elif opt=="2":
            plainText=decryptVigenereCipher(input("Enter Encrypted Text: ").upper(),input("Enter Key: ").upper())    
            print("Plain Text: "+plainText+"\n")
        else:
            print("\n ####Select valid option!!#### \n")
        

    elif option=="5":
        print("Goodbye")
        exit()

    else:
        print("\n ####Select valid option!!#### \n")
