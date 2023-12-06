def read():
    name = str(input("Enter employee's name: "))
    code = int(input("Enter employee's code: "))
    bp = int(input("Enter the Basic Pay: "))
    
    return bp,code,name

def calculation(bp):
    if bp < 10000:
        da = bp*(5/100)
        hra = bp*(2.5/100)
        ma = 20
        pt = 20
        pf = bp*(8/100)
        it = 0

        gross_salary = bp+da+hra+ma
        deduction = pt+pf+it
        net_salary = gross_salary-deduction

        return net_salary
    
    elif bp>10000 and bp<30000:
        da = bp*(7.5/100)
        hra = bp*(5/100)
        ma = 2500
        pt = 60
        pf = bp*(8/100)
        it = 0

        gross_salary = bp+da+hra+ma
        deduction = pt+pf+it
        net_salary = gross_salary-deduction

        return net_salary

    elif bp>30000 and bp<50000:
        da = bp*(11/100)
        hra = bp*(7.5/100)
        ma = 5000
        pt = 60
        pf = bp*(11/100)
        it = bp*(11/100)

        gross_salary = bp+da+hra+ma
        deduction = pt+pf+it
        net_salary = gross_salary-deduction

        return net_salary

    else:
        da = bp*(25/100)
        hra = bp*(11/100)
        ma = 7000
        pt = 80
        pf = bp*(12/100)
        it = bp*(20/100)

        gross_salary = bp+da+hra+ma
        deduction = pt+pf+it
        net_salary = gross_salary-deduction

        return net_salary
    
def payslip(name,code,bp,net_salary):
    print(name)
    print(code)
    print(net_salary)

bp,code,name = read()
net_salary = calculation(bp)
payslip(name, code, bp, net_salary)