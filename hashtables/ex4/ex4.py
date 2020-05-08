def has_negatives(a):
    ht = {}
    result = []

    # iterate over each number
    for i in a:
        ht[i] = None
    for i in a:
        if i > 0:
            # positive * negative = negative
            if i * -1 in ht:
                # pass the value onto the results list
                result.append(i)


   
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))

