import random

p1 = 0
c = 0
while True:
    i1 = random.randint(0, 9)
    p1 = input("Guess the number between 0 to 9 or Enter exit to END\n")
    print("Another number is : %s" % i1)
    if p1 == "exit":
        break
    elif 0 < int(p1) < i1:
        c += 1
        print("Your Number is Somehow Lower")
    elif i1 < int(p1) < 9:
        c += 1
        print("Your Number is Somehow Higher")
    elif int(p1) == i1:
        c += 1
        print("!! Gotcha !!")
        print("You only took %s tries" % c)
    else:
        print(" What's That Kiddo !! Enter between 0 and 9")