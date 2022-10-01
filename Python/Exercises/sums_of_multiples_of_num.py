# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).

def sum_of_multiples(limit):
    
    divide_by_5 = limit // 5
    divide_by_3 = limit // 3
    result = 0

    for i in range (1, divide_by_3 +1):
        if i <= divide_by_5:
            result += i * 5
        result += i * 3
    return result


limit = int(input("limit: "))
print (f"The sum equals: {sum_of_multiples(limit)}")
