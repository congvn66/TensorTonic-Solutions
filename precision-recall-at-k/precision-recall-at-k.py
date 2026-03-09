def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    relevant_num = len(relevant)
    hit = 0
    for i in range(k):
        for r in relevant:
            if recommended[i] == r:
                hit += 1
                break
    return [hit / k, hit/relevant_num]    