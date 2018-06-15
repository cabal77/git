import random
p1in=("Player 1 Wins")
p2in=("Player 2 Wins")

player1=input("Player: Rock, Paper or Scissors? ").lower()
player2=random.randint(0,2)

if player2==0:
    player2="rock"
elif player2==1:
    player2="paper"
elif player2==2:
    player2="scissors"
print(player2)
if player1==player2:
    print("Tie")

elif player1=="rock":
    if player2=="scissors":
        print(p1in)
    if player2=="paper":
        print(p2in)

elif player1=="scissors":
    if player2=="rock":
        print(p2in)
    if player2=="paper":
        print(p1in)

elif player1=="paper":
    if player2=="scissors":
        print(p2in)
    elif player2=="rock":
        print(p1in)
else:
    print("One or both players entered incorrect value. Check spelling.")