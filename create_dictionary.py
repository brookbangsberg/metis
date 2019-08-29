def create_dictionary(lower, upper):
    result = {'even' : [], 'odd' : []}
    i = lower
    while True:
        if i > upper:
            break
        if i % 2 == 0:
            result['even'].append(i)
        else:
            result['odd'].append(i)
        i += i
    return result
