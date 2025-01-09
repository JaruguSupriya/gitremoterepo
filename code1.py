
m = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(m):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
even_numbers = [num for num in numbers if num % 2 == 0]
sum_of_even_numbers = sum(even_numbers)
print("\nOriginal List:", numbers)
print("Even Numbers:", even_numbers)
print("Sum of Even Numbers:", sum_of_even_numbers)
#hai this is my devops program
#thanku