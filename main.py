#Comprehension
def odd(number):
    return "Odd" if number %2 == 1 else "Even"

x = [12,45,7,89,63,78,65]


y = [odd(i) for i in x]

y.append(45)

print(x)
print(y)