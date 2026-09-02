feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}


def compile_feedback(ratings_dict):

    result = {}

    for course, ratings in ratings_dict.items():

        valid_ratings = []

        for rating in ratings:
            try:
                valid_ratings.append(float(rating))
            except (ValueError, TypeError):
                print(f"Warning: Invalid rating value '{rating}' in course '{course}' skipped.")

        try:
            average = sum(valid_ratings) / len(valid_ratings)
            result[course] = round(average, 2)

        except ZeroDivisionError:
            print(f"Warning: No valid ratings found for course '{course}'. Rating set to 0.0.")
            result[course] = 0.0

    return result


result=compile_feedback(feedback_data)
print(result)