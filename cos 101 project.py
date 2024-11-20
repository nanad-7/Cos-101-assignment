def a():
    velocity = int(input("enter velocity"))
    time = int(input("enter time"))
    # acceleration = velocity*time
    output = str(velocity*time)
    print(output +"m/s^2")

def b():
    work = int(input("enter work:"))
    time= int(input("enter time:"))
    # power = work*change in time
    output = str(work / time)
    print(output + "W")

def c():
    force= int(input("enter force :"))
    length= int(input("enter length:"))
    # surface tension = force/length
    output = str(force/length)
    print(output + "N/m")

def d():
    mass= int(input("enter mass:"))
    volume= int(input("enter volume:"))
    # surface tension = mass/volume
    output = str(mass/volume)
    print(output + "pa")


def e():
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    # power = a^b
    output = str(a**b)
    print(output)

def main():
        user_choice = input("enter choice (a for acceleration) , (b for power),(c for surface tension,d(d for pressure),e(raise to power):")
        if user_choice == "a":a()
        elif user_choice == "b":b()
        elif user_choice == "c":c()
        elif user_choice == "d":d()
        elif user_choice == "e":e()
if __name__ == '__main__':
    main()