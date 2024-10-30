def fetch_score () :
    try:
        with open ("my_score.txt", "r") as doc:
            score_data = doc.read()
    except FileNotFoundError:
        score_data = 0

    return int(score_data)