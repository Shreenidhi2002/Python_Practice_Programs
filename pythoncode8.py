#guess game 
secret_number=9
guess_count=0

while guess_count <3:
    guess = int(input("Guess : "))
    guess_count += 1
    if(guess == secret_number):
        print("you won")
        break
else:
    print("you lose")    
