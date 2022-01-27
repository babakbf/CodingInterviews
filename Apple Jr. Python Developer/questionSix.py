import sys


def solution(actual_price, given_price):
    if given_price < actual_price:
        print("ERROR")
        return
    elif given_price == actual_price:
        print("ZERO")
        return
    else:
        price_to_return = given_price - actual_price
        results = set([])

        for value in values:
            while price_to_return >= value:
                results.add(value)
                price_to_return = price_to_return - value

        results = list(results)
        results = [name2value[result] for result in results]

        results = sorted(results)
        print(",".join(results))
        return


name2value = {.01: 'PENNY', .05: 'NICKEL', .10: 'DIME', .25: 'QUARTER', .50: 'HALF DOLLAR', 1.00: 'ONE', 2.00: 'TWO',
              5.00: 'FIVE', 10.00: 'TEN', 20.00: 'TWENTY', 50.00: 'FIFTY'}

values = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

for line in sys.stdin:
    purchase_price, cash = line.split(";")
    purchase_price, cash = float(purchase_price), float(cash)
    solution(purchase_price, cash)

    """ my solution is here 

"""
'PENNY': .01,  'NICKEL': .05,  'DIME': .10,  'QUARTER': .25,  'HALF DOLLAR': .50,  'ONE': 1.00,  'TWO': 2.00,  'FIVE': 5.00,  'TEN': 10.00,  'TWENTY': 20.00,  'FIFTY': 50.00,  'ONE HUNDRED': 100.00  

Test 1
Test Input : 15.94;16.00
Expected Output : NICKEL,PENNY
Test 2
Test Input : Input17;16
Expected Output : ERROR  

Test 3
Test Input : 35;35
Expected Output : ZERO  

Test 4
Test Input : 45;50
Expected Output : FIVE
"""
# 60 3 20 , 50 ,10 
def return_money(expence,moneypaid):
    arr = []
    dict = {}
    banks = { .01 : 'PENNY', .05: 'NICKEL', .10:'DIME',  .25:'QUARTER',  .50:'HALF DOLLAR',   1.00:'ONE', 
    2.00:'TWO',5.00:'FIVE',   10.00:'TEN', 20.00:'TWENTY',50.00:  'FIFTY', 100.00:  'ONE HUNDRED'  }
    values = [100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]
    if expence > moneypaid:
        print("ERROR")
    elif expence == moneypaid:
        print("ZERO")
    else:
        diff = moneypaid - expence #189.89
        for value in values:
            if diff>=value:
                dict[banks[value]]=diff//value 
                diff = diff % value 
        #print(tuple(dict))
        print(",".join(i for i in dict))
    #print(arr)
return_money(45,50)
print("-"*50)
return_money(17,16)
print("-"*50)
return_money(15.94,16.00)
print("-"*50)
return_money(35,35)
print("-"*50)     
return_money(200,500)
   """
