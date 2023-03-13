def remove_duplicates(dataset):

    duplicates = set()

    results = []

    for rec in dataset:
        id = rec[0]
        appendResult = True

        if id not in duplicates:
            duplicates.add(id)
        else:
            appendResult = False
        
        if appendResult:
            results.append(rec)

    return results