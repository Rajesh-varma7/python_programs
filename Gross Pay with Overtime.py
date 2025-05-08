Hours = int(input("Enter Hours"))
Rate = int(input("Enter Rate"))
Overtime = Hours - 40
Worked = Hours - Overtime
#Extra_Rate = 1.5
if Hours > 40:
  print("Pay:",(Worked*rate)+Overtime*Rate*1.5)
else:
  print("Pay:",Hours*Rate)
