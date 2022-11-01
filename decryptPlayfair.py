import string

def remove_characters(text, chars_to_remove):
    temp = ""
    for char in text:
        if char not in chars_to_remove:
            temp += char
    return temp


 
#    generates the 5x5 key square
def generateKeyTable(key, ks):
    keyT = [[0 for j in range(5)] for i in range(5)]
    dicty = [0 for i in range(26)]
 
    for i in range(ks):
        if key[i] != 'j':
            dicty[ord(key[i]) - 97] = 2
    
    dicty[ord('j') - 97] = 1
 
    i = 0
    j = 0

    for k in range(ks):
        if dicty[ord(key[k]) - 97] == 2:
            dicty[ord(key[k]) - 97] -= 1
            keyT[i][j] = key[k]
            j += 1
            if j == 5:
                i += 1
                j = 0

    for k in range(26):
        if dicty[k] == 0:
            keyT[i][j] = chr(k + 97)
            j += 1
            if j == 5:
                i += 1
                j = 0
    
    return keyT


#   Search for the characters of a digraph in the key square and return their position
def search(keyT, a, b):
    arr = [0 for i in range(4)]
    
    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
 
    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a :
                arr[0] = i
                arr[1] = j
            elif keyT[i][j] == b :
                arr[2] = i
                arr[3] = j
    return arr

 
#   Function to find the modulus with 5
def mod5(a):
    if a < 0:
        a += 5
    return a % 5

 
#   Function to decrypt
def decrypt(code, keyT, ps):
    for i in range(0, ps, 2):
        a = search(keyT, code[i], code[i + 1])
        
        code = list(code)
        if a[0] == a[2] :
            code[i] = keyT[a[0]][mod5(a[1] - 1)]
            code[i + 1] = keyT[a[0]][mod5(a[3] - 1)]
        elif a[1] == a[3] :
            code[i] = keyT[mod5(a[0] - 1)][a[1]]
            code[i + 1] = keyT[mod5(a[2] - 1)][a[1]]
        else :
            code[i] = keyT[a[0]][a[3]]
            code[i + 1] = keyT[a[2]][a[1]]
        code = ''.join(code)
    return code


#   Function to call decrypt
def decryptPlayfair(code, key):
    ks = len(key)
    key = remove_characters(key, string.punctuation + " ")
    key = key.lower()
    ps = len(code)
    code = code.lower()
    code = remove_characters(code, string.punctuation + " ")
    
    keyT = generateKeyTable(key, ks)
    code = decrypt(code, keyT, ps)
    return code


code = input("Ingrese el texto: ")
key = input("Ingrese la clave: ")
text = decryptPlayfair(code, key)
print("Texto plano:", text)