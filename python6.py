# 1. Student Marks Management
# Problem: Create a dictionary containing student names and marks using two lists

names = ["Ravi", "Priya", "John", "Sneha"]
marks = [85, 90, 65, 95]

students = {names[i]: marks[i] for i in range(len(names))}

print(students)

# 2. Product Price Discount
# Problem: An online shopping store provides a 10% discount on all products. Create a new dictionary containing discounted prices.

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 2000,
    "Keyboard": 1500
}

discount = {item: price * 0.9 for item, price in products.items()}

print(discount)

# 3. Employee Salary Filter
# Problem: A company wants to display only employees whose salary is greater than ₹30,000.

employees = {
    "Arun": 25000,
    "Kiran": 40000,
    "Priya": 35000,
    "Ravi": 28000
}

high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary > 30000
}

print(high_salary)

# 4. Word Length Calculator
# Problem: Create a dictionary containing words as keys and their lengths as values

words = ["Python", "Java", "Embedded", "Electronics"]

word_length = {word: len(word) for word in words}

print(word_length)

# 5. Temperature Converter
# Problem: A weather application stores temperatures in Celsius. Convert all temperatures into Fahrenheit

temperatures = {
    "Bengaluru": 25,
    "Hubli": 30,
    "Mysuru": 28,
    "Delhi": 35
}

fahrenheit = {
    city: (temp * 9/5) + 32
    for city, temp in temperatures.items()
}

print(fahrenheit)