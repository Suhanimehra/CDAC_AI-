def grade():
    
    score=int(input("Enter Scores : "))

    
    x=[score+10 for score in score if score<50 or score+5 for score in score if score>50 ]
    
    print(x)
grade()



# def grade():
#     scores = [int(x) for x in input("Enter Scores: ").split()]

#     curved = [min(100, score + 10 if score < 50 else score + 5) for score in scores]

#     print("Original:", scores)
#     print("Curved:", curved)


# grade()
