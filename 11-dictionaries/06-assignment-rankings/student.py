def rankings(participants):
    ranking_dict = {}
    rank = 1
    for participant in participants:
        ranking_dict[participant] = rank
        rank += 1
    return ranking_dict
