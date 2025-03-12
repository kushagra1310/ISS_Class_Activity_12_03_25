def is_narc(n): #colon
    """Check if a number is narc."""
    num_str = str(n) #== changed to =
    num_digits = len(num_str) #== changed to =
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) #*** changed to **
    
    return sum_of_powers   #removed faulty =n

def print_narcis_numbers(start,end): #colon added, comma between parameters
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #colon missing
        if is_narc(num)==num: #wrong function called, colon missing, ==num condition added
            print(num)

print_narcis_numbers(1000, 5000) #function name of called function was wrong