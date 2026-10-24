
a = int(input("what is your number:"))

# if the student has number 4
if a == 3:
    a = a + 1
    print("student number: " ,a)

    b = 20
    b -= 5
    print(f"your point is: {b}")

    num1 = a
    grade1 = b
    print(f"student number: {num1} ,your point is: {grade1} ,that means you passed")

# if student failed
else:
    c = 8
    print(f"your point is: {c}")
    
    num2 = a
    grade2 = c
    print(f"student number: {num2} ,your point is: {grade2} ,that means you failed")
