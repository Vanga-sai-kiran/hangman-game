import random
#step 1:- make a list of words
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
word_list=["technology","computer","random","hangsman","valuation","project"]
#step2:-choose a random word from the word_list and assign it to a variabe
choosen_word=random.choice(word_list)
print(choosen_word)
#step3:-ask a letter from the user and assign it to the variable
stop=False
blanks=[]
for i in range(0,len(choosen_word)):
       blanks.append("_")
while not stop:
   guess=input("guess a letter  :\n")
   #step 5:now generate a list of blanks that equal to length of choosen_word
   
  #step4:-now check whether a guessed letter is in the choosen word
   for position in range(len(choosen_word)):
      letter=choosen_word[position]
      if letter==guess:
         blanks[position]=letter
   if guess not in choosen_word:
     lives-=1
     
     if lives==0:
       stop=True
       print("you lose! betterluck next time!!")   
   if guess in choosen_word:
      print(blanks)
   if "_" not in blanks:
     stop=True
     print("you won")
   print(stages[lives])

