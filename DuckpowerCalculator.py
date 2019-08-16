#Duck Power calculator
print("Duckpower calculator")
calc = int(input("How much horsepower? "))

#1 hp = 300 dp

dp = 300

def main(calc):
    result = (calc * dp)
    print(calc, "horsepower is equal to" , result, "Duckpower")

main(calc)    
