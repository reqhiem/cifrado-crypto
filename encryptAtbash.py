
# atbash encryption algorithm
def atbash(text):

    text = text.lower()

    alfabeto_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    tabla_atbash = 'zyxwvutsrqponmlkjihgfedcba'

    character = {
        'á':'a' , 'é':'e' , 'í':'i' , 'ó':'o' , 'ú':'u',
        ' ':''  
    }

    for k,v in character.items():
        text = text.replace(k,v)

    message = ''
    for i in text:
        index = alfabeto_minusculas.index(i)
        message += tabla_atbash[index]

    return message


if __name__ == "__main__":
    text = input('Ingrese texto a cifrar: ')
    pairs = atbash(text)
    print(pairs)