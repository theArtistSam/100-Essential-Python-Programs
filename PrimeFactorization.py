# Prompt the user to enter an integer
num = eval(input("Enter an integer: "))

# Initialize counters and list for factors
# Python Prime Factorization

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
factors = []

# Perform prime factorization until the number becomes 1
while num != 1:
    # Check if the number is divisible by 2
    if num % 2 == 0:
        num /= 2
        factors.append(2)  # Append 2 to the list of factors
        counter1 += 1

        # Check if the number is divisible by 3
        if num % 3 == 0:
            num /= 3
            factors.append(3)  # Append 3 to the list of factors
            counter2 += 1

            # Check if the number is divisible by 5
            if num % 5 == 0:
                num /= 5
                factors.append(5)  # Append 5 to the list of factors
                counter3 += 1

                # Check if the number is divisible by 7
                if num % 7 == 0:
                    num /= 7
                    factors.append(7)  # Append 7 to the list of factors
                    counter4 += 1

# Print the list of prime factors
print(factors)
