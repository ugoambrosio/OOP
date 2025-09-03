print('hello, welcome to Harvest\n')
prinloan = int(input('Write your principal loan\n'))
rateint2 = int(input('Write your rate of interest\n'))
durationloan = int(input('Write the duration of the loan\n'))
rateint = rateint2/(12*100)
emi = prinloan * rateint * ((1+rateint)**durationloan)/((1+rateint)**durationloan-1)

for i in range(durationloan,0,-1):
    balance = prinloan - emi
    print('Your actual Balance is:',balance)
    print('You have ',durationloan,'months of loan yet')
    print('-------------')


