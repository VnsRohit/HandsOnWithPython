# BMI Calculator
height=float(input('Enter your height in m: '))
weight=float(input('Enter your weight in kg: '))
bmi=round(weight/(height**2),0)
print(f'Your BMI is'{int(bmi)})
