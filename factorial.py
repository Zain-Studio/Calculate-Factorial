#Program For Calculating Factorial:

def factorial(number):
    if number == 0 or number ==1:
        return 1
    else:
        return number* factorial(number-1)
    


def factorialTrailingZeros(number):
    count = 0 
    i = 5
    #100! = 100// + 100//5*5
    while(number//i !=0):
        count += int(number/i)
        i = i*5
        return count
    
    
if __name__=='__main__':
    number = int(input("Enter number to find a factorial: \n"))
    fac = factorial(number)
    print(f"Given number factotial is: {fac}")
    print(factorialTrailingZeros(number))