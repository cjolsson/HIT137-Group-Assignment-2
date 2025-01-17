def en_de_crypt(textIn, m, n, oneOrMinusOne):
   
   def encrypt(inCharacter, m, n, oneOrMinusOne): #Function both encrypts and decrypts text.  The oneOrMinusOne parameter value determines whether the function is encrypting (1) or decrypting (-1) text.
      
      denominator = 13 #Because there are 13 alphabetical characters from a to m, n to z, A to M and N to Z
      
      if   "a" <= inCharacter <= "m":

         outCharacter = chr(((ord(inCharacter) - ord("a") + ((n * m)  * oneOrMinusOne)) % denominator) + ord("a"))
         
      elif "n" <= inCharacter <= "z":

         outCharacter = chr(((ord(inCharacter) - ord("n") - ((n + m)  * oneOrMinusOne)) % denominator) + ord("n"))
         
      elif "A" <= inCharacter <= "M":
 
         outCharacter = chr(((ord(inCharacter) - ord("A") - (n        * oneOrMinusOne)) % denominator) + ord("A"))
         
      elif "N" <= inCharacter <= "Z":

         outCharacter = chr(((ord(inCharacter) - ord("N") + ((m ** 2) * oneOrMinusOne)) % denominator) + ord("N"))
         
      else:

         outCharacter = inCharacter #Character is not a letter, return as is
         
      return outCharacter
#-----------------------------------------------------------------------------------------------------------------
   textOut = str()

   for thisLetter in textIn:

      if ' ' <= thisLetter <= '~': #Only printable characters between space and tilde are acceptable

         letterOut = thisLetter

         if thisLetter.isupper() or thisLetter.islower(): #Only letters are encrypted or decrypted

            letterOut = encrypt(thisLetter, m, n, oneOrMinusOne)

      else:

         print("Error: Invalid character in input text")
         break

      textOut += letterOut #Build the output text one character at a time

   return textOut
#-----------------------------------------------------------------------------------------------------------------
def comparison(textRead, encryptedText, unEncryptedText): #Compares the original and decrypted texts to verify encryption and decryption processes success
   
   if textRead == unEncryptedText: #Check if the original text and the decrypted text match
      
      g = open("encrypted_text.txt", 'w') #Write the encrypted text to a file
      g.write(encryptedText)
      g.close()
   
      print("Success: Encryption and decryption succeeded.  Original text and decrypted text match")
      
      return True
      
   else:
      
      print("Error: Encryption and decryption failed.  Original text and decrypted text do not match")
      
      return False
#-----------------------------------------------------------------------------------------------------------------
def main():

   m = int(input("Enter value of m: "))
   n = int(input("Enter value of n: "))
   
   if m == 0 and n == 0:
      
      print("Error: m and n cannot both be zero")
      
   else:

      f = open("raw_text.txt",'r') #Get the text to be encrypted from a file
      textRead = f.read()
      f.close()

      encryptedText   = str.format(en_de_crypt(textRead,      m, n,  1)) #Encrypt the text

      unEncryptedText = str.format(en_de_crypt(encryptedText, m, n, -1)) #Decrypt the text

      comparison(textRead, encryptedText, unEncryptedText) #Compare the original text with the decrypted text
   
if __name__ == "__main__":
   main()