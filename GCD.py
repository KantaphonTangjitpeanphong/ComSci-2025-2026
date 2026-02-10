

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

factor_num1 = []
factor_num2 = []
for i in range(1, num1):

    if num1 % i == 0:
        factor_num1.append(i)

print(factor_num1)

for j in range(1, num2):
    if num2 % j == 0:
        factor_num2.append(j)

print(factor_num2)

common_factors = []
for factor in factor_num1:
    if factor in factor_num2:
        common_factors.append(factor)
        

print(common_factors)
gcd = max(common_factors)
print(f"The GCD of {num1} and {num2} is: {gcd}")