#bmi = weight/(height)^2;
height = float(input("Hey bro what is your height"));
weight = float(input("Hey bro what is your weight"));
bmi = weight/((height**2));
if (bmi > 18.5):
    if (bmi > 25):
        if(bmi>30):
            if (bmi>35):
                print(f"You are clinically obese {bmi}");
            else:
                print(f"You are Obese {bmi}");
        else:
            print(f"you are overweight {bmi}");

    else:
        print(f"you are normal {bmi}")


else:
    print("Under Weight");
