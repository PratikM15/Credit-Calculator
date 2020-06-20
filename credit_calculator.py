import math
print("What do you want to calculate?")
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "d" - for differential monthly payment,')
print('type "p" - for credit principal')
choice = input()

if choice == "n":
    print("Enter the credit principal:")
    credit = float(input())
    print("Enter monthly payment:")
    payment = float(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    count = math.ceil(math.log(payment / (payment - i * credit), 1 + i))
    years = int(count // 12)
    months = count % 12
    print()
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
    
elif choice == "a":
    print("Enter the credit principal:")
    credit = float(input())
    print("Enter count of periods:")
    count = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    A = math.ceil((credit * i * (1 + i) ** count) / ((1 + i) ** count - 1))
    overpayment = int(A * count - credit)
    print()
    print("Your annuity payment =", A)
    print("Overpayment =", overpayment)

elif choice == "d":
    print("Enter the credit principal:")
    credit = float(input())
    print("Enter count of periods:")
    count = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    installments = []
    total = 0
    print()
    for m in range(1,count+1):
        D = math.ceil(credit / count + i * (credit - (credit * (m - 1))/count))
        installments.append(D)
        print("Month", m, ": paid out", D)
        total += D
    overpayment = int(total - credit)
    print()
    print("Overpayment =", overpayment)

elif choice == "p":
    print("Enter monthly payment:")
    payment = float(input())
    print("Enter count of periods:")
    count = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    value = (i * (1 + i) ** count) / (((1 + i) ** count) - 1)
    P = int(payment / value)
    print()
    print("Your credit principal =", P)
    overpayment = int(payment * count - P)
    print("Overpayment =", overpayment)

else:
    print("Enter valid choice.")

