
points = int(input("Enter your current points: "))
print(f"your point is {points}")

a = points + 50
print(a)

if a >= 100:
    print(f"your point is {a}")
    print("Great! You leveled up to the next level!")

else:
    print(f"your point is {a}")
    print("Points added, but you need more to level up")
