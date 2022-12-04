#Basic Calculator

def add(){
  sum=a+b
  print(sum)
}

def subtract(){
  diff=a-b
  print(diff)
}

def multiply{
  product=a*b
  print(product)
}

a=int(input("Enter first digit:"))
b=int(input("Enter second digit:"))
operation=input("Enter operation-add,subtract,multiply:")
if operation=="add":
  add(a,b)
elif operation=='subtract':
    subtract(a,b)
elif operation=='multiply':
      product(a,b)
