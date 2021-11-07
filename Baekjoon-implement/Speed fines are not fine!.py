limit = int(input())
speed = int(input())
diff = speed - limit
 
if diff <= 0:
    print("Congratulations, you are within the speed limit!")
elif diff >= 1 and diff <= 20:
    print("You are speeding and your fine is ${}.".format(100))
elif diff >= 21 and diff <= 30:
    print("You are speeding and your fine is ${}.".format(270))
elif diff >= 31:
    print("You are speeding and your fine is ${}.".format(500))
