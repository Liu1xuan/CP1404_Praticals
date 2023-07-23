def main():
    score = float(input("Your score is "))
    print(score_level(score))


def score_level(score):
   if score < 0 or score > 100:
    return "Invalid score"
   elif score >= 90:
    return "Excellent"
   elif score >= 50:
    return "Passable"
   else:
    return "Bad"

main()
