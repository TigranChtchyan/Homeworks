a = [0,1,2,3,4,5,6,7,8,9,10]
the_number = 8

def binary_search(start, end):
    guess = (start + end)//2
    if guess == the_number:
        return guess
    elif guess < the_number:
        start = guess
    else:
        end = guess
    return binary_search(start, end)

print(binary_search(0, len(a)-1))