def binary_gap(number):
    binary_values = bin(number)[2:]
    current_gap = 0
    maximum_gap = 0
    for binary_value in binary_values:
        if binary_value == "0":
            current_gap += 1
        else:
            if current_gap > maximum_gap:
                maximum_gap = current_gap
            current_gap = 0
    print(f"maximum gap is {maximum_gap}")
    return maximum_gap
binary_gap(529)