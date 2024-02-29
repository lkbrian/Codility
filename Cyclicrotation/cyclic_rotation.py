def cyclic_rotation(Array,K):
    for _ in range(K):
        number = Array.pop()
        Array.insert(0, number)
    print(Array)


cyclic_rotation([1, 2, 3, 4, 5], 3)
