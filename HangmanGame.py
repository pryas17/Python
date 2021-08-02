import random
def welcome(name):
    print('Hey',name,'all the best for the game!')
    print()

name = input('Player name: ')
welcome(name)

movies = ['dilwale','sanam','aashiqui','ekthatiger','tamasha','sultan','pk','3idiots','anaconda','avatar','titanic','dabangg',
          'munnabhaimbbs','inception','chhichhore','dangal','golmaal','taarezameenpar','tumbbad','andhadhun']

random.shuffle(movies)
movie_guess = movies[0]
chances = len(movie_guess)+3
def Game_rules():
    print('GAME RULES:')
    print('1. You will have %d chances to guess the movie name correctly'%(chances))
    print()
    
Game_rules()

print()
print('movie name length is:',len(movie_guess))

movie_player = '-' * len(movie_guess)
print(movie_player)
movie_player_list = list(movie_player)

for i in range(1,chances+1):
    guess = input('Enter your guess: ')
    if movie_guess.count(guess)==2:
        print('Great job!, you have guessed correctly..Keep going..')
        m = movie_guess.find(guess)
        movie_player_list[m]=guess
        n = movie_guess.find(guess,m+1)
        movie_player_list[n]=guess
        movie_player = ''.join(movie_player_list)
        print(movie_player)
    elif movie_guess.count(guess)==3:
        print('Great job!, you have guessed correctly..Keep going..')
        m = movie_guess.find(guess)
        movie_player_list[m]=guess
        n = movie_guess.find(guess,m+1)
        movie_player_list[n]=guess
        o = movie_guess.find(guess,n+1)
        movie_player_list[o]=guess
        movie_player = ''.join(movie_player_list)
        print(movie_player)
    elif movie_guess.count(guess)==4:
        print('Great job!, you have guessed correctly..Keep going..')
        m = movie_guess.find(guess)
        movie_player_list[m]=guess
        n = movie_guess.find(guess,m+1)
        movie_player_list[n]=guess
        o = movie_guess.find(guess,n+1)
        movie_player_list[o]=guess
        p = movie_guess.find(guess,o+1)
        movie_player_list[p]=guess
        movie_player = ''.join(movie_player_list)
        print(movie_player)
    elif movie_guess.count(guess)==5:
        print('Great job!, you have guessed correctly..Keep going..')
        m = movie_guess.find(guess)
        movie_player_list[m]=guess
        n = movie_guess.find(guess,m+1)
        movie_player_list[n]=guess
        o = movie_guess.find(guess,n+1)
        movie_player_list[o]=guess
        p = movie_guess.find(guess,o+1)
        movie_player_list[p]=guess
        q = movie_guess.find(guess,p+1)
        movie_player_list[q]=guess
        movie_player = ''.join(movie_player_list)
        print(movie_player)
    elif guess in movie_guess:
        print('Good job!, you have guessed correctly..Keep going..')
        j = movie_guess.find(guess)
        movie_player_list[j]=guess
        movie_player = ''.join(movie_player_list)
        print(movie_player)
    else:
        print('Sorry!, wrong guess. Please try again')
    if movie_player == movie_guess:
        print('Congratulations...You won the game with chances left!!!')
        print("Movie name is: ",movie_guess)
        print("Movie name you entered: ",movie_player)
        break

if i==chances and movie_player != movie_guess:
    print()
    print('You are out of chances..Better luck next time..')
