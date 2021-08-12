#Define a function to take a word and return negative meaning.
Given a word, return a new word where "not " has been added to the front. However, if the word already begins with "not", return the string unchanged.

def not_string(word):
   x=word.split()
   if "değil" in x:
      print(word)
   else :
     print("{} değil ".format(word))
 
not_string("kelime değil")