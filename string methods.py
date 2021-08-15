#STRING METHODS
'
#captialize()
x="this is jacob"
y=x.capitalize()
print(y)

#casefold()
txt="MASTER"
y=txt.casefold()
print(y)

#center()
x="jacob raja"
txt=x.center(20)
print(txt)

#count()
txt=["vijay","senthil","vijay","siva","vijay"]
x=txt.count("vijay")
print(x)

#endswith()
txt="Hello world!"
x=txt.endswith(".")
print(x)

#encode()
x="jacob"
txt=x.encode()
print(txt)

#expandtabs()
txt="j\ta\tc\to\tb"
x=txt.expandtabs(0)
print(x)

#find()
s="python is a programming language"
y=s.find("programming")
print(y)

#isalpha()
txt="jacobraja"
x=txt.isalpha()
print(x)

#isalnum()
x="45864"
txt=x.isalnum()
print(txt)

#index()
n="python is a programming language"
y=n.index("is")
print(y)

#isdigit()
txt="45862"
y=txt.isdigit()
print(y)

#isdecimal
num="\u0030"
x=num.isdecimal()
print(x)

#isidentifier()
txt="python"
y="java script"
print(txt.isidentifier())
print(y.isidentifier())

#isnumeric()
num="89562"
print(num.isnumeric())

#isprintable()
txt="Hi, How are you?"
print(txt.isprintable())

#isspace()
x="    "
y=" mycaptain   "
print(x.isspace())
print(y.isspace())

#istitle()
txt="Lets Code"
x="PYTHON"
print(txt.istitle())
print(x.istitle())

#isupper()
z="TESLA"
print(z.isupper())

#join()
l1=("Tesla","Audi","GTR")
print("/".join(l1))

#lower)
txt="BUGATI"
print(txt.lower())

#upper()
x="bugati"
print(x.upper())

#ljust()
txt="apple"
x=txt.ljust(10)
print("This",x,"was soo delicious")

#lstip()
x="apple    "
print(x.lstrip())




