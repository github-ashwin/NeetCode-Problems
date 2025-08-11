def hcf(num1,num2):
    a , b = num1 , num2
    while num2>0:
        num1 , num2 = num2 , num1%num2
    hcf = num1

    lcm = (a*b)//hcf

    return hcf, lcm