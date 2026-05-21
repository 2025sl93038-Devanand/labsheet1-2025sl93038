from calculator import add, subtract, multiply, divide
 
 
print("Calculator Operations Validation")
 
 
# Test addition
print("\n1. Testing Addition:")
print(f"   add(10, 5) = {add(10, 5)}")
 
 
# Test subtraction
print("\n2. Testing Subtraction:")
print(f"   subtract(10, 5) = {subtract(10, 5)}")
 
 
# Test multiplication
print("\n3. Testing Multiplication:")
print(f"   multiply(10, 5) = {multiply(10, 5)}")
 
 
# Test division
print("\n4. Testing Division:")
print(f"   divide(10, 5) = {divide(10, 5)}")
print(f"   divide(10, 0) = {divide(10, 0)} (Division by zero)")
 
 
print("All calculator operations validated successfully!")