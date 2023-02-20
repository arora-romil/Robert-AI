import matplotlib.pyplot as plt
import numpy as np


def sine(x, y):
    # Data for plotting
    r = float(input("The number you want to multiply 'x' in sin(x) is "))
    t = np.arange(x, y, 0.01)
    # Sine Plot
    s = np.sin(r*t)
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='Sin(x)',
           title='Sine Plot')
    ax.grid()
    plt.show()


def cos(x, y):
    # Cosine Plot
    r = int(input("The number you want to multiply 'x' in cos(x) is "))
    t = np.arange(x, y, 0.01)
    s = np.cos(r*t)
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='(cosx)',
           title='Cosine Plot')
    ax.grid()
    plt.show()


def tan(x, y):
    # Tangent Plot
    r = int(input("The number you want to multiply 'x' in tan(x) is "))
    t = np.arange(x, y, 0.01)
    # t = np.arange(0.0, 1, 0.1)
    s = np.tan(r*t)
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='tan(x)',
           title='Tangent Plot')
    ax.grid()
    plt.show()


def cosec(x, y):
    # Data for plotting
    r = float(input("The number you want to multiply 'x' in cosec(x) is "))
    t = np.arange(x, y, 0.01)
    # Sine Plot
    s = 1 / (np.sin(r*t))
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='Cosec(x)',
           title='Cosec Plot')
    ax.grid()
    plt.show()


def secant(x, y):
    # Cosine Plot
    r = int(input("The number you want to multiply 'x' in sec(x) is "))
    t = np.arange(x, y, 0.01)
    s = 1 / (np.cos(r*t))
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='(sec(x))',
           title='Secant Plot')
    ax.grid()
    plt.show()


def cotangent(x, y):
    # Tangent Plot
    r = int(input("The number you want to multiply 'x' in cot(x) is "))
    t = np.arange(x, y, 0.01)
    # t = np.arange(0.0, 1, 0.1)
    s = 1 / (np.tan(r*t))
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='radians', ylabel='cot(x)',
           title='Cotangent Plot')
    ax.grid()
    plt.show()


print("\nWelcome to the trigonometric graphs printer-\n*******************************************")
while True:
    print("Type 1 for Sine Graph\nType 2 for Cosine Graph\nType 3 for Tangent graph\nType 4 for Cosecant graph\nType 5 for Secant graph\nType 6 for Cotangent graph\n")
    e = (input("Select from [1,2,3,4,5,6] = "))
    l = ['1','2','3','4','5','6'] 
    if e not in l:
        print("ERROR !! You have entered a wrong selection code, Please Retry!!\n")
        continue
    print("")
    if (e == '1'):
        print("You have selected Sin Graph")
    elif (e == '2'):
        print("You have selected Cos Graph")
    elif (e == '3'):
        print("You have selected Tan Graph")
    elif (e == '4'):
        print("You have selected Cosec Graph")
    elif (e == '5'):
        print("You have selected Secant Graph")
    elif (e == '6'):
        print("You have selected Cot Graph")
    
    print("\n[If you are selecting Tangent\\Cosecant\\Secant\\Cotangent],Then you have to keep in mind that your interval should not contain - Infinity or Negative infinity\n")
    l = list(map(float, input(
        "Interval (in radian) in which you want to plot graph (e.g. [1,2] will be written as 1 2) = ").split()))
    x = l[0]
    y = l[1]

    if (x > y):
        print("You have entered the wrong interval, the interval should be like (lower limit, upper limit), Please Retry!!\n")
        continue
    if (e == '1'):
        sine(x, y)
    elif (e == '2'):
        cos(x, y)
    elif (e == '3'):
        tan(x, y)
    elif (e == '4'):
        cosec(x, y)
    elif (e == '5'):
        secant(x, y)
    elif (e == '6'):
        cotangent(x, y)

    print("Do you want another graph?")
    again = input("Yes | No: ").strip().lower().capitalize()
    # If yes, then go back to the function
    if again == "Yes":
        print("\n", end="")
        continue
        # If no, then say goodbye and exit
    elif again == "No":
        print("Thank you for using !")
        exit()
    else:
        print('"ERROR 404"')
        exit()
