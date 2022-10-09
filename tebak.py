import random
 

print("tebak nama\n")
 
# set the initial values
the_number = random.randint(1, 10)
guess = int(input("tebak nama: "))
tries = 1
 
# guessing loop
while guess != the_number:
    if guess > the_number:
        print("salah...")
    else:
        print("benar...")
 
    guess = int(input("Take a guess: "))
    tries += 1
    if tries == 31:
        print ("You failed to guess in time!")
        break
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        name = ''
 
while name != 'dika':
    print('siapa namanya?')
    name = input()
 
print('Ya, nama saya ' + name + '. selamat')