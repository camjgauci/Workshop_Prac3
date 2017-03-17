
# score = float(input("Enter score: "))
# if  0 > score > 100:
#     print("Invalid score")
# elif 50 > score > 90:
#     print("Passable")
# elif score > 90:
#     print("Excellent")
# else:
#       print("Bad")


def score_result():
    score = float(input("Enter Score:"))
    if 0 < score > 100:
        return "Invalid Score"
    elif 50 < score < 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


print(score_result())
