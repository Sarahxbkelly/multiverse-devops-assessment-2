def validate_field(dataset):

    results = []

    for idx,rec in enumerate(dataset):

        if idx == 0 or (rec[5].isnumeric() and int(rec[5])>0 and int(rec[5])<=10):
            results.append(rec)

    return results

