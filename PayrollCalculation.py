# Python Payroll Calculation program

# Receive user input for name, hours, pay rate, federal tax rate, and state tax rate
name = input("Enter the name: ")
hours = eval(input("Enter number of hours: "))
pay_rate = float(input("Enter pay rate: "))
federal_tax = eval(input("Enter federal tax rate: "))
state_tax = eval(input("Enter state tax rate: "))

# Calculate federal withholding, state withholding, total deduction, gross pay, and net pay
federal_withholding = (hours * pay_rate) * (federal_tax / 100)
state_withholding = (hours * pay_rate) * (state_tax / 100)
total_deduction = federal_withholding + state_withholding
gross_pay = hours * pay_rate
net_pay = gross_pay - total_deduction

# Print the employee's name, pay rate, gross pay, deductions, total deduction, and net pay
print()
print("Employee's Name:", name)
print("Pay Rate: $", pay_rate)
print("Gross Pay: $", gross_pay)
print("Deductions:")
print("  Federal Withholding ({}%): ${}".format(federal_tax, federal_withholding))
print("  State Withholding ({}%): ${}".format(state_tax, state_withholding))
print("  Total Deduction: ${}".format(total_deduction))
print("Net Pay: $", net_pay)