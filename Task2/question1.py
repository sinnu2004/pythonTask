# In-Hand Salary Calculator
# Write a Python program to calculate monthly in-hand salary after deductions from CTC.
# Deductions: HRA 10%, DA 5%, PF 3%.
# Tax slabs: Below 5L=0%, 5-10L=10%, 10-20L=20%, Above 20L=30%.

def month_salary(s):
    HRA = (s)* 10/100
    DA = (s)*5/100
    PF = (s)*3/100
    salary = s - HRA - DA - PF
    if(s<5):
        return salary
    elif(s>=5 and s<10):
        tax = (s) * 10/100
        return salary - tax
    elif(s>=10 and s<=20):
        tax = (s) * 20/100
        return salary - tax
    elif(s>20):
        tax = (s)*30/100
        return salary - tax

n = int(input("Enter the montly in-hand salary in Lakh :"))

print(month_salary(n))