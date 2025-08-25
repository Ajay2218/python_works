
"""
EMI = (P * r * (1 + r)^n) / ((1 + r)^n - 1)

p = loan amount

r = interest rate(annual_rate/(12*100))

n =loan tenure in month(month*12)

"""

loan_amount = int(input("enter the loan amount = "))

interest_rate = int(input("enter the interest rate = "))

loan_tenure = int(input("enter the installment year = "))

p = loan_amount

r =interest_rate/(12*100)

n = loan_tenure * 12

emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)

print("emi = ",round(emi,2))

total_payable_amount = emi * n

print("total payable amount = ",round(total_payable_amount,2))

total_interest = total_payable_amount - loan_amount

print("total interest = ",round(total_interest,2))


