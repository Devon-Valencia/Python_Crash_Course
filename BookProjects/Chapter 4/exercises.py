# pizzas = ["pepperoni", "cheese", "jalapeno"]
# for pizza in pizzas:
#     print(pizza)

# pizzas = ["pepperoni", "cheese", "jalapeno"]
# for pizza in pizzas:
#     print(f"I really love {pizza.title()} pizza!")
# print("\nI really love Pizza!")

# animals = ["dog", "cat", "parrot"]
# for animal in animals:
#     print(f"A {animal.title()} would make a great pet!")
# print("\nAny of these animals would make great pets.")

# numbers = []
# for value in range(1, 1000000):
#     print(value)

# numbers = [1, 1000000]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# numbers = []
# for value in range(1, 21, 3):
#     print(value)

# mutiples = []
# for value in range(3, 31, 3):
#     print(value)

# cubed = []
# for value in range(1, 10):
#     cubed.append(value**3)
# print(cubed)

cubed = [value**3 for value in range(1, 10)]
print(cubed)