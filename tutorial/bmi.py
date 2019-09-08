# -*- coding: utf-8 -*-
while True :
    name = input("Your name : ")
    h = input("Your Height (m) : ")
    w = input("Your Weight (kg) : ")
    Height = float(h)
    Weight = float(w)
    bmi = Weight / (Height*Height)
    if bmi < 18.5:
        print("Your are too light(name = %s , BMI = %d) !" % (name, bmi))
    elif bmi >= 18.5 and bmi < 25:
        print("Congratulation you are health(name = %s , BMI = %d)!" % (name, bmi))
    elif bmi >= 25 and bmi < 32:
        print("You are Heavy , Please pay a attension(name = %s, BMI = %d)!" % (name, bmi))
    else:
        print("You are too Heavy , you must get your weight down(name = %s, BMI = %d)!" % (
            name, bmi))
    q = input("Press any key to continue , <q> to quit ......")
    if q == 'q':
        break






    
