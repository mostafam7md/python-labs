#1
print("hello world")

#2
while True:
    binary_num = input("Enter binary number : ").strip()
    if binary_num.isdigit():
        if not binary_num:
            print("Input cannot be empty")
            continue
        if not all(c in '01' for c in binary_num):
            print("Input must be binary number")
            continue
    dicmal_num = int(binary_num, 2)
    print(dicmal_num)
    break

#3 
def fizzBuzzProblem(num):
    if not num.is_integer():
        print("Input must be number")
        return
    if num %3 ==0 and num%5 !=0 :
        print("fizz")
    elif num %5 == 0 and num % 3 != 0 :
        print("Buzz")
    elif num %3 ==0 and num%5 == 0 :
        print("FizzBuzz")

while True:
    nums = input("Enter a number for fizzBuzz : ").strip()
    if not nums:
        print("Input cannot be empty")
        continue
    if not nums.isdigit():
        print("Input must be number")
        continue
    num = int(nums)
    fizzBuzzProblem(num)
    break

#4 
while True:
    radius = input("Enter radius of circle : ").strip()
    if not radius:
        print("Input cannot be empty. Please try again.")
        continue
    if not radius.isdigit():
        print("Radius must be positive number")
        continue
    circle_radius = int(radius)
    if circle_radius <= 0:
        print("Radius must be greater than zero ")
        continue
    break
PI = 3.14
print("the area of circle is ", PI * circle_radius ** 2)
print("the area of circumference is ", 2 * PI * circle_radius)
#5
while True:
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty")
        continue
    if name.isdigit():
        print("Name cannot be number")
        continue
    print(f" ur name : {name}")
    break

email = input("Enter your email: ").strip()
print(f"ur name is: {name}\n ur email is : {email}")

#6 
def findITI(word):

    if not isinstance(word, str) :
        print("Input cannot be emty and must be string")
        return
    count = word.lower().count('iti')
    print(count)

findITI("aasgITIdsalkITImvbbITI") 