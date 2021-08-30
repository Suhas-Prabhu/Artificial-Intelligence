import numpy as np
from tqdm import tqdm
import math

# calculating simple interest
def simple_interest(p,r,t):
    print('Principal Amount :',p)
    print('Rate of interest :',r)
    print('Time period :',t)
    si = (p*t*r)/100
    a = p+si
    print('final amount :',a)
    print('simple interest',si)

#calculating compound interest
def compound_interest(p,r,t):
    print('Principal Amount :',p)
    print('Rate of interest :',r)
    print('Time period :',t)
    a = p*((1+r/100)**t)
    ci = a-p
    print("final amount :",a)
    print("compound interest :",ci)
    
# purchasing power (Inflation)
def pur_power(p,r,t):
   print('Principal Amount :',p)
   print('Rate of interest :',r)
   print('Time period :',t)
   a = p*((100/(100+r))**t)
   print('after ',t,' years, the final amount is ',a)

# compound annual growth rate
def CAGR(p,a,t):
   print('Initial amount :',p)
   print('Final amount :',a)
   print('Time period :',t)
   t_inv = 1/t
   cagr_rate = (((a/p)**t_inv)-1)*100
   print('compound annual growth rate :',cagr_rate)

# monthly EMI calculation
def EMI(p,r,n):
    print("Total Loan Amount: ",p)
    print("Rate of Interest: ",r)
    print("Number of installments: ",n)
    r_mon = r/(12*100)
    emi = p*r_mon*((1+r_mon)**n)/((1+r_mon)**n -1)
    print("EMI for ",n," months :",emi)

# double time calculation
def inv_double(r):
    print("rate of interest :",r)
    t= math.log(2)/math.log(1+(r/100))
    print("time taken in years to double money at ",r," percent PA : ",t)

# weighted average
ratio=[0.20, 0.25, 0.35,0.10, 0.10]
rates=[7.5, 8.5, 8, 5, 6]
def weighted_average(ratio,rates):
    wa=0
    for i in range(len(ratio)):
        wa= wa+ ratio[i]*rates[i]
    print("Weighted Average returns: ",wa)

