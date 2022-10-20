is_leap_year = False
   
input_year = int(input())

if(input_year % 400 == 0) or ((input_year % 100 != 0) and (input_year % 4 == 0)):   
    print(input_year,'- leap year')  
else:  
    is_leap_year = True
    print(input_year,'- not a leap year')  