import random
def game():
    while True:
        print("random guessing game start!")
        whilecount = 0
        score = 100
        count = 0
        k = 10
        totalscore = 0
        while count < 10:
            randomvariable = random.randint(1, k)
            while True:
                inputtedvariable = int(input("enter the number you think is right but between  1 and " + str(k) + " : "))
                if randomvariable == inputtedvariable:
                    print("you got it! your score is:" + str(score))
                    count = count + 1
                    k = k - 1
                    break
                else:
                    whilecount = whilecount + 1
                    print("try again goofy")
                    score = score - 10
                    if score == 0:
                        print("you lost the level")
                        break
                    continue
            print("level " + str((count)) + " is done!")
            totalscore = totalscore + score
            score = k*10
            print("total score is " + str(totalscore) )

        if (count == 10):
            print("the game ended , your score is " + str(totalscore))



j = input("wanna play? y/n")
if j == "y":
    game()
else:
    print("thanks for playing")