import math
import sys
import argparse  
  
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="Type of monthly payment")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

credit = args.principal
count = args.periods
interest = args.interest
payment = args.payment
lst = [credit, count, interest, payment]

counter = 0

for item in lst:
    if item == None or item < 0:
        counter +=1
    

if counter > 1:
    print("Incorrect parameters.")
    
else:
    i = interest / (12 * 100)
    if args.type == "annuity" :
        if payment == None:
            A = math.ceil((credit * i * (1 + i) ** count) / ((1 + i) ** count - 1))
            overpayment = int(A * count - credit)
            print("Your annuity payment =", A)
            print("Overpayment =", overpayment)
            
        elif credit == None:
            value = (i * (1 + i) ** count) / (((1 + i) ** count) - 1)
            P = int(payment / value)
            print("Your credit principal =", P)
            overpayment = int(payment * count - P)
            print("Overpayment =", overpayment)
            
        elif count == None:
            count = math.ceil(math.log(payment / (payment - i * credit), 1 + i))
            years = int(count // 12)
            months = count % 12
            if months > 11.5:
                years += 1
                months = 0
            months = math.ceil(months)
            if years == 0:
                print("You need", months, "months to repay this credit!")
            elif months == 0:
                print("You need", years, "years to repay this credit!")
            else:
                print("You need", years, "years and", months, "months to repay this credit!")
            overpayment = int(payment * count - credit)
            print("Overpayment =", overpayment)
            
    elif args.type == "diff":
        installments = []
        total = 0
        for m in range(1,count+1):
            D = math.ceil(credit / count + i * (credit - (credit * (m - 1))/count))
            installments.append(D)
            print("Month", m, ": paid out", D)
            total += D
        overpayment = int(total - credit)
        print()
        print("Overpayment =", overpayment)
    
