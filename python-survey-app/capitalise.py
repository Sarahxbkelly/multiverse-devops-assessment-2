def capitalise(dataset):

    for idx,rec in enumerate(dataset):

        if idx == 0:
            continue

        rec[1] = rec[1].capitalize()
        rec[2] = rec[2].capitalize()

    return dataset