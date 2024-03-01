def solution(Array):
    occurence = set()
    [
        occurence.remove(element) if element in occurence else occurence.add(element)
        for element in Array
    ]
    unpaired = occurence.pop()
    #you can also get a set of all unpaired values
    print(unpaired)
    return unpaired


solution([9, 1, 7, 5, 9, 7, 5, 3, 11])
