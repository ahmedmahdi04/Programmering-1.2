def easy_quiz():
    score = 0
    print("Welcome to the easy quiz.")
    ans1 = input("vilken färg är dina ögon?").lower()
    if ans1 == ("brun"):
        print ("helt rätt")
        score +=5

    else: print("tyvärr fel")

    return score


def hard_quiz():
    score = 0
    print("Welcome to the hard quiz.")
    ans1 = input("Vad är sveriges huvudstad?").lower()
    if ans1 == ("stockholm"):
        print("helt rätt")
        score +=5

    else: print("tyvärr fel")

    return score


def superhard_quiz():
    score =0
    ans1 = input("Vad finns i centrala Paris?").lower()
    if ans1 == ("r"):
        print ("helt rätt")
        score +=5
    else: print("tyvärr fel")

    ans2 = input("Om det finns ett blått hus till höger om dig och ett rött hus till vänster, var är det vita huset?").lower()
    if ans2 == ("i washington"):
        print ("helt rätt")
        score +=5
    else: print("tyvärr fel.")

    return score

    
    


namn = input("Namn: ")
score = 0

while True:
    difficulty = input("Easy, hard or superhard?").lower()

    if difficulty == "easy":
        score += easy_quiz() 

    elif difficulty == "hard":
        score = hard_quiz()

    elif difficulty == "superhard":
        score = superhard_quiz()

    elif difficulty == "q":
        break

    poäng = input("vill du se dina poäng?").lower()
    if poäng == ("ja"):

        print ("Hej", "score")
        
        print(f"Quiz over, you got {score} points.")