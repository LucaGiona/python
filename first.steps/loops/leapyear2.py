
year = int(input("Year: "))
initial_year = year

while True:
    
    if year %4 == 0 and year %100 != 0 or year %400 == 0:
        leapyear = year + 4
        if leapyear %100 == 0 and leapyear %400 !=0:
            leapyear += 4
        print(f"The next leap year after {initial_year} is {leapyear}") 
        break
    else:
        year +=1
        if year %4 == 0 and year %100 != 0 or year %400 == 0:
            print(f"The next leap year after {initial_year} is {year}")
            break
    