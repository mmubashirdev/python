# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
  
#     result = num1 / num2
#     print("Result:", result)
    
# except ZeroDivisionError:
#     print("Oops! You can't divide by zero.")

# except ValueError:
#     print("Please enter valid numbers only!")

# except Exception as e:
#     print("Something went wrong:", e)

# finally:
#     print("Done")


#try:
 # file = open("File.txt",'r')
#except FileNotFoundError:
 # print("Where is the file brother??")
 
# try:
#    num = int(input("Enter a number"))
#    x = 10/num
# except ValueError:
#   print("Enter a valid number")

# except ZeroDivisionError:
#   print("Cannot divide by zero")
# else:
#   print("Division: ",x )
  
# finally:
#   print("End Program")
  
# class UnderAgeError(Exception):
#     pass
# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#       raise UnderAgeError("you must be older than 18")
#     print("Access granted")
# except UnderAgeError as e:
#     print(e)
    
try:
  list = [1,2,3,4]
  print(list[10])
except IndexError:
  print("Index not found")
try:  
  obj = {
    'name': 'AB',
    'rollNo': 1
  }
  print(obj['abc'])
except KeyError as e:
  print("Key not found")

try:
  x = 'abc'
  y = 123
  z = x + y
  print(x+y)
except TypeError:
  print("cannot concate a number and a string")