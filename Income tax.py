Ded_std=150000
Ded_80c = int(input("deduction under 80c: "))
Ded_80cc = int(input("deduction under 80cc: "))
Ded_hra = int (input("deduction under HRA: "))
Ded_med = int(input("deduction under Medical: "))
Ded_tot = (Ded_std + Ded_80c + Ded_80cc + Ded_hra + Ded_med)
Gross_Income = int(input("gross income: "))
Tax_Income= Gross_Income - Ded_tot

if Tax_Income>=0:
    if(Gross_Income<=500000):
        Income_Tax=(tax_Income * .1)
    if(Gross_Income <=1000000)and(Gross_Income > 500000):
        Income_Tax=25000+((Gross_Income - 500000)*.2)
    if(Gross_Income > 1000000):
        Income_Tax=75000 + ((Gross_Income - 1000000)*.3)
    print("gross income: ",Gross_Income)
    print("total deduction: ",Ded_tot)
    print("income tax: ",Income_Tax)
else:
    print("hurry..no income tax")