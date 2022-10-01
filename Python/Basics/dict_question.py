# Change Numbers to Written numbers (1 -> one)

dict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}

def num_to_written(digits):
    output = ""
    for num in digits:
        output += dict.get(num, "doesn't exist yet.") + " "
        # output += dict[num] + " "
    return output



digits = input("Phone number: ")


print (num_to_written(digits))