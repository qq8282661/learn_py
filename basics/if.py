bmi = input('weight:')
if int(bmi) < 18.5:
    print("过轻")
elif int(bmi) < 25:
    print("正常")
elif int(bmi) < 28:
    print("过重")
elif int(bmi) < 32:
    print("肥胖")
else:
    print("严重肥胖")
