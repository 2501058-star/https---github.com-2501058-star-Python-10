choi = { 'korean' : 94, 'english': 91, 'mathematics': 89, 'science': 83}

high_scores = {key: value for key, value in choi.items() if value >= 90}

for subject in high_scores.keys():
    print(subject)