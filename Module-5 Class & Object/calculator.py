class Calculator:
    brand = "Casio 100 MS"

    # additon method
    def add(self, num1, num2):
        return num1 + num2
    
    # deduct method
    def deduct(self, num1, num2):
        return num1 - num2
    
    # multiply method
    def multiply(self, num1, num2):
        return num1 * num2

    # devison method
    def devision(self , num1, num2):
        return num1 / num2
    

num1, num2 = map(int, input().split())
math = Calculator()
print(type(math))
sum = math.add(num1,num2)
print(sum)

sub = math.deduct(num1,num2)
print(sub)

mult = math.multiply(num1, num2)
print(mult)

div = math.devision(num1, num2)
print(div)