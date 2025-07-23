def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_digits = []
    
    # Outer loop: process the number until it becomes 0
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num = decimal_num // 2
    
    # Inner loop: reverse the digits (optional - could use [::-1] instead)
    binary_str = ""
    for i in range(len(binary_digits)-1, -1, -1):
        binary_str += binary_digits[i]
    
    return binary_str

# Example usage
number = int(input("Enter a decimal number: "))
binary = decimal_to_binary(number)
print(f"The binary representation is: {binary}")