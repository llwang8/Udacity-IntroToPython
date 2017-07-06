# Udacity
# Intro to Python

# Lesson 2

# Code with Branches I
# Points  Prize
# 0 - 50  wooden rabbit
# 51 - 150    No prize
# 151 - 180   wafer-thin mint
# 181 - 200   penguin

def which_prize(points):
    prize = 'No prize'
    text = "Oh dear, no prize this time."
    if points < 51:
        prize = 'wooden rabbit'
    elif points < 151:
        prize = 'No prize'
    elif points < 181:
        prize = 'wafer-thin mint'
    elif points < 201:
        prize = 'penguin'
    if prize != 'No prize':
        text = "Congratulations! You have won a {}!".format(prize)

    print(text)

which_prize(12)


# 9. Code with Branches III
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    top_area = 3.14 * radius ** 2
    if has_top_and_bottom:
        return side_area + 2 * top_area
    else:
        return side_area

cylinder_surface_area(10, 5, False)


# 10. Code with Branches IV
def which_prize(points):
    prize = None
    if points < 51:
        prize = 'wooden rabbit'
    elif (points > 150) and (points < 181):
        prize = 'wafer-thin mint'
    elif (points > 180) and (points < 201):
        prize = 'penguin'

    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."

print(which_prize(194))


# Scores To Rating Function Design
# write a function that takes as input five scores and aggregates
# them to output a single rating.  Because the highest and lowest
#scores might be outliers and skew the results, we will take the
# three middle scores out of the five, discarding the highest and
# lowest.  Then we will take the average (mean) of those three
# middle scores.
# Average Score   Rating
# 0 <= score < 1  Terrible
# 1 <= score < 2  Bad
# 2 <= score < 3  OK
# 3 <= score < 4  Good
# 4 <= score <= 5 Excellent

def convert_to_numeric(score):
    """
    Convert score to float
    """
    return float(score)

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Sum of middle 3 scores
    """
    scores = [score1, score2, score3, score4, score5]
    sumOfAll = sum(scores)
    sumOfMiddle3 = sumOfAll - max(scores) - min(scores)
    return sumOfMiddle3

def score_to_rating_string(avgScore):
    if avgScore < 1:
        return "Terrible"
    elif avgScore < 2:
        return "Bad"
    elif avgScore < 3:
        return "OK"
    elif avgScore < 4:
        return "Good"
    elif avgScore <= 5:
        return "Excellent"

def scores_to_rating(score1, score2, score3, score4, score5):
    # convert scores to numeric
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # Get average of middle 3 scores
    avgScore = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # Get rating string
    rating = score_to_rating_string(avgScore)

    return rating






