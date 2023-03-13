def remove_duplicates(dataset):

    duplicates = set() #create set as cannot have multiple occurrences of the same element

    results = []

    for rec in dataset: #iterate over list 
        id = rec[0]
        appendResult = True

        if id not in duplicates: #only add unique values
            duplicates.add(id)
        else:
            appendResult = False
        
        if appendResult:
            results.append(rec) #add to list

    return results