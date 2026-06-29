'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
youstr = input("Enter your choice: ")
youDict = {
    "s" : 1, "w": -1, "g":0 
}
reverseDict = {1:"Snake",0:"Gun", -1: "Water"}
you = youDict[youstr]
print(f"You chose {reverseDict[you]} Computer chose {reverseDict[computer]}")
if computer == you:
    print("Its a Draw")
else:
    if computer == -1 and you == 1:
        print("You win")
    elif computer == -1 and you == 1:
        print("You Lose")
    elif computer == 1 and you == -1:
        print("You Lose") 
    elif computer == 1 and you == 0:
        print("You Win")  
    elif computer == 0 and you == -1:
        print("You win")
    elif computer == 0 and you == 1:
        print("You Lose")
    else:
        print("Something went wrong!")
    
