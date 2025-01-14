
def encrypt_text(text, n, m):
    encrypted = ""
    for ch in text:
        if ch.islower(): #checks whether all char in a string are lowercase
            if ord(ch)- ord("a") < m: #lowercase requirement (a-m)
             ch = chr( (ord(ch)-ord('a')+ n*m) % 26 + ord('a')) #chr converts an integer to its unicode char and returns it
            elif ord('z')- ord(ch) < n: #lowercase requirement (n-m)
             ch = chr( (ord(ch)-ord('a') -n-m + 26) % 26 + ord('a')) 
        elif ch.isupper(): # Checks whether the character is uppercase
            if ord(ch)- ord("A") < m: # Uppercase requirement (A-M)
             ch = chr( (ord(ch)-ord('A')-n+26) % 26 + ord('A')) 
            elif ord('Z')- ord(ch) < n:# Uppercase requirement (Z-N)
             ch = chr( (ord(ch)-ord('A')+ m**2) % 26 + ord('A')) 
        encrypted += ch
    return encrypted
    
def decrypt_text(encrypted, n, m):
    text = ""
    for ch in encrypted:
        if ch.islower():
            if ord(ch)- ord("a") < m:
                ch = chr( (ord(ch)-ord('a')- n*m + 26) % 26 + ord('a'))
            elif ord('z')- ord(ch) < n:
             ch = chr( (ord(ch)-ord('a') +n+m) % 26 + ord('a'))
        elif ch.isupper(): # Checks whether the character is uppercase
            if ord(ch)- ord("A") < m:
                ch = chr( (ord(ch)-ord('A')+n) % 26 + ord('A'))
            elif ord('Z')- ord(ch) < n:
             ch = chr( (ord(ch)-ord('A')- m**2 + 26) % 26 + ord('A')) 
        text += ch
    return text
    
def check_correctness(content, content1):
    if content == content1:
        print("The decrytion is correct")
    else:
        print("The decryption is incorrect")
    
m = int(input("Enter a value for m: ")) #Get user input for n and m 
n = int(input("Enter a value for n: "))
with open("raw_text.txt", "r") as f:
    content = f.read()
    print("Original content:", content) # Print statement for debugging
    encrypted = encrypt_text(content, n, m)
    print("Encrypted content:",(encrypted) )
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)
    
    content1 = decrypt_text(encrypted, n, m)
    print("Decrypted content:", content1) # Print statement for debugging

    check_correctness(content, content1)

