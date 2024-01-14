#Q1
def int_bin(num):
    if num == 0:
        return '0'
    binary_representation = ''

    while num > 0:
        binary_representation = str(num % 2) + binary_representation
        num //= 2

    return binary_representation

num = int(input("Enter positive integer: "))
result_binary = int_bin(num)
print("Binary representation:", result_binary)

#Q2
def int_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

testing_num = int(input("Enter an integer: "))
Factors = int_factors(testing_num)
print("Factors of", testing_num, ":", Factors)


#Q3
def check_prime(num):
    if num <= 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1

Testing_num = int(input("Enter a num: "))
if check_prime(Testing_num):
    print(Testing_num, "a prime number.")
else:
    print(Testing_num, "not a prime number.")
    
    
#Q4
def simple_encryption(message):
    encrypted_message = list(message)
    encrypted_message.reverse()
    encrypted_message = ''.join(encrypted_message)
    
    return encrypted_message

original_message = input("Enter a message: ")
encrypted_result = simple_encryption(original_message)
print("Encrypted message:", encrypted_result)