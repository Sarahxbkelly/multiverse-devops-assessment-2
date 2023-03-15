def remove_empty_records(dataset):

    results = []

    for rec in dataset:
<<<<<<< HEAD
        if all(rec):
=======
        if all(rec): #
>>>>>>> develop
            results.append(rec)

    return results