def remove_empty_records(dataset):

    results = []

    for rec in dataset:
        if all(rec): #
            results.append(rec)

    return results

