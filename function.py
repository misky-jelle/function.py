def hello():
  print("hello Misky")
hello()

def hello(name,age):
  year=2022-age
  return(f"Hello {name} you were born in {year}")

def my_country(country="Kenya"):
   return (f"my country is {country}") 

def greet(name):
  print(f"Hello {name}")
  return

def greet(*names):
  for name in names:
   print(f"Hello {names}")

def sum(*num,num2):
  sum=num+num2
  return

def sum(*numbers):
  total=0
  for x in numbers:
    total +=x
    return total

def multiply(*numbers):
  product = 1
  for x in numbers:
    product*=x
  return product

def greet_multiply(**kwarys):
  keys=kwarys.keys()
  values=kwarys.values()
  print(keys)
  print (values)


def greet_multiply(**kwargs):
  keys=kwargs.keys()
  if "country" in keys:
   return (f"Hello {kwargs['name']} from {kwargs['country']}")

  elif "age" in keys:
    year=2022-kwargs["age"]
    return f"Hello{kwargs['name']} you were born in{year}"

  elif "name" in keys:
    return f"Hello {kwargs}"

  else :
    return f"Hello Anonymous"


def sum_and_greet(*args,**kwargs):
    print(args)
    print(kwargs)


def multiply_and_greet(*args,**kwargs):
  total=1
  for num in args:
    total*=num
  print(f"Hello {kwargs['name']} from {kwargs['country']}")
  


  
   
   

   



