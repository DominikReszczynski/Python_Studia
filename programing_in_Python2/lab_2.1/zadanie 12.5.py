def BMI(mass, height):
    try:
        bmi=mass/(height * height)
        return bmi
    except:
        print("coś wpisałeś nie tak")
mass=int(input("podaj swoją masę ciała (w kg): "))
height=int(input("podaj swój wzrost (w metrach): "))
BMI=BMI(mass,height)
try:
    if BMI<=18.5:
        print("masz niedowagę")
    elif BMI>18.5 and BMI<=24.99:
        print("Twoja waga jest prawidłowa")
    else:
        print("masz nadwagę!!!")
except:
    pass
