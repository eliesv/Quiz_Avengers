def maxkey(dictionary):
    maxv = max(dictionary.values())
    maxk = ''
    for key in dictionary:
        if dictionary[key] == maxv:
            maxk = key
            break
    return maxk
