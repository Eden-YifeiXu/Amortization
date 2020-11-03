import prettytable as ptb

# Get User Input
while True:
    principal = float(input("Please input a principal: "))
    if principal < 0:
        print("Principal must be a float and no less than 0. Please try again.")
    else:
        break

while True:
    interest_rate = float(input("Please input an interest rate: "))
    monthly_interest_rate = interest_rate / 12
    if interest_rate < 0:
        print("Interest rate must be a float and no less than 0. Please try again.")
    else:
        break

while True:
    min_payment = float(input("Please input a minimum expected payment: "))
    if min_payment < 0:
        print("Minimum payment must be a float and no less than 0. Please try again.")
    elif min_payment <= principal*monthly_interest_rate:
        print("Minimum payment must exceed the initial interest. Please try again.")
    else:
        break

while True:
    extra_pay = float(input("Please input an extra payment:"))
    if extra_pay < 0:
        print("Extra payment must be a float and no less than 0. Please try again.")
    elif min_payment + extra_pay - principal*monthly_interest_rate > principal:
        print("Do not overpay orz. Please enter a lower extra pay.")
    else:
        break


# Compute and Print the schedule
month = 1
month_list = [month]
begin_p = []
payment = []
interest = []
extra_payment = []
p_applied = []
end_p = []

while True:
    begin_p.append(float('%.2f'% principal))
    payment.append(float('%.2f'% min_payment))
    interest.append(float('%.2f'% (principal * monthly_interest_rate)))
    extra_payment.append(float('%.2f'% extra_pay))
    p_applied.append(float('%.2f'% (payment[-1] - interest[-1] + extra_payment[-1])))
    end_p.append(float('%.2f'% (principal - p_applied[-1])))

    month += 1
    principal = end_p[-1]
    month_list.append(month)

    if min_payment + extra_pay >= principal + principal*monthly_interest_rate:
        if min_payment >= principal + principal*monthly_interest_rate:
            begin_p.append(principal)
            payment.append(float('%.2f'% (principal + principal*monthly_interest_rate)))
            interest.append(float('%.2f'% (principal*monthly_interest_rate)))
            extra_payment.append(0)
            p_applied.append(principal)
            end_p.append(0)
            break
        if min_payment < principal + principal*monthly_interest_rate:
            begin_p.append(principal)
            payment.append(min_payment)
            interest.append(float('%.2f'% (principal * monthly_interest_rate)))
            extra_payment.append(float( '%.2f'% (principal + principal * monthly_interest_rate - min_payment)))
            p_applied.append(principal)
            end_p.append(0)
            break


# Compute and print other indexes
total_pay = '%.2f'% sum(payment)
total_interest = '%.2f'% sum(interest)
total_pa = '%.2f'% sum(p_applied)

begin_p.append('')
payment.append(total_pay)
interest.append(total_interest)
extra_payment.append('')
p_applied.append(total_pa)
end_p.append('')
month_list.append('Total')

table = ptb.PrettyTable()
table.add_column("Month", month_list)
table.add_column("Begin P", begin_p)
table.add_column("Payment", payment)
table.add_column("Interest", interest)
table.add_column("Extra Payment", extra_payment)
table.add_column("P Applied", p_applied)
table.add_column("End P",end_p)
print(table)


# Compute and print year
year = int(month_list[-2])//12
month_p = int(month_list[-2]) % 12
print("Total Required Peroid: ", year,"years, and", month_p, "months.")