#BMI fomula = Weight(kg) / Height(m)^2
W = input('Please key-in your weight(kg) ＝')
H = input('Please key-in your height(m) =')
W = float(W)
H = float(H)
B = W / (H ** 2)
B = float(B)
print('Your BMI is ', round(B, 3))
if B < 18.5 : 
    print('You are underwhight.')
elif B >= 18.5 and B < 24 : 
    print('You are typical weight.')
elif B >= 24 and B < 27 :
    print('You are overweight.')
elif B >= 27 and B < 30 :
    print('You are a little overweight.')
elif B >= 30 and B < 35 :
    print('you are medium overweight.')
else :
    print('You are overweight too much!!!!') 