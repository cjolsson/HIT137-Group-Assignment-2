def en_de_crypt(textIn, m, n, oneOrMinusOne):
   
   def encrypt(inCharacter, m, n, oneOrMinusOne):     
      
      denominator = 13
      
      if "a" <= inCharacter <= "m":

         outCharacter = chr(((ord(inCharacter) - ord("a") + ((n * m)  * oneOrMinusOne)) % denominator) + ord("a"))
         
      elif "n" <= inCharacter  <= "z":

         outCharacter = chr(((ord(inCharacter) - ord("n") - ((n + m)  * oneOrMinusOne)) % denominator) + ord("n"))
         
      elif "A" <= inCharacter  <= "M":
 
         outCharacter = chr(((ord(inCharacter) - ord("A") - (n        * oneOrMinusOne)) % denominator) + ord("A"))
         
      elif "N" <= inCharacter  <= "Z":

         outCharacter = chr(((ord(inCharacter) - ord("N") + ((m ** 2) * oneOrMinusOne)) % denominator) + ord("N"))
         
      else:

         outCharacter = inCharacter
         
      return outCharacter
#----------------------------------------------------------------------------------------
   textOut = str()

   for thisLetter in textIn:

      if ' ' <= thisLetter <= '~':

         letterOut = thisLetter

         if thisLetter.isupper() or thisLetter.islower():

            letterOut = encrypt(thisLetter, m, n, oneOrMinusOne)

      else:

         print("Error: Invalid character in input text")
         break

      textOut += letterOut

   return textOut
#----------------------------------------------------------------------------------------
def main():

   m = int(input("Enter value of m: "))
   n = int(input("Enter value of n: "))

   f = open("raw_text.txt",'r')
   textRead = f.read()
   f.close()

   encryptedText   = str.format(en_de_crypt(textRead,      m, n,  1))

   unEncryptedText = str.format(en_de_crypt(encryptedText, m, n, -1))

   if textRead == unEncryptedText:
      
      g = open("encrypted_text.txt", 'w')
      g.write(encryptedText)
      g.close()
      
if __name__ == "__main__":
   main()
