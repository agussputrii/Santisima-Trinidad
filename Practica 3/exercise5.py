actual_year = int(input("Enter the actual year: "))
another_year = int(input("Enter another year: "))

if actual_year == another_year:
    print("Both years are the same!")
elif actual_year > another_year:
    years_diference = actual_year - another_year
    print(f"Since year '{actual_year}', have passed '{years_diference}' years.")
else:
    years_diference = another_year - actual_year
    print(f"to get to the year {another_year}, missing '{years_diference}' years.")