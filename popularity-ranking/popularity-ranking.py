def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    ratings = []
    
    for movie in items:
        rate = movie[0]
        votes = movie[1]

        ratings.append(votes * rate / (votes + min_votes) + min_votes * global_mean / (votes + min_votes))

    
    return ratings