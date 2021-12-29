# time: 0(n^2) | space: 0(1)
def two_number_sum(array, target_sum):
    # create for loop to get the first index
    for i in range(len(array) - 1):
        firstNumber = array[i]
        # create for loop to get the second index
        for j in range(i + 1, len(array)):
            secondNumber = array[j]
            # limited in checking the first and second number but the summation
            # equal target
            if firstNumber + secondNumber == target_sum:
                return [firstNumber, secondNumber]
    return []

print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))


