# ISS_Class_Activity_12_03_25
Almost every line had syntactic and logical errors. Changed them and added comments related to changes made.
old code:
def is_narc(n) 
    """Check if a number is narc."""
    num_str == str(n)
    num_digits == len(num_str)
    
    sum_of_powers = sum(int(digit) *** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start end)
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1)
        if is_narcissistic(num)
            print(num)

print_narc_numbers(1000, 5000)
changes:
colon added in line 4,13,15
== to = in line 6,7
comma between parameters in line 13
function names fixed in lines 16,19
== num condition added in line 16
*** changed to ** in line 9
