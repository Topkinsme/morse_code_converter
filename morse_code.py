#code by top

def numone():
    a=str(input("INPUT PLS  \n"))
    b=0
    c=len(a)
    e=""
    while b<c:
        if a[b] == "a":
            d=".-"
        elif a[b] =="b":
            d="-..."
        elif a[b] =="c":
            d="-.-."
        elif a[b] =="d":
            d="-.."
        elif a[b] =="e":
            d="."
        elif a[b] =="f":
            d="..-."
        elif a[b] =="g":
            d="--."
        elif a[b] =="h":
            d="...."
        elif a[b] =="i":
            d=".."
        elif a[b] =="j":
            d=".---"
        elif a[b] =="k":
            d="-.-"
        elif a[b] =="l":
            d=".-.."
        elif a[b] =="m":
            d="--"
        elif a[b] =="n":
            d="-."
        elif a[b] =="o":
            d="---"
        elif a[b] =="p":
            d=".--."
        elif a[b] =="q":
            d="--.-"
        elif a[b] =="r":
            d=".-."
        elif a[b] =="s":
            d="..."
        elif a[b] =="t":
            d="-"
        elif a[b] =="u":
            d="..-"
        elif a[b] =="v":
            d="...-"
        elif a[b] =="w":
            d=".--"
        elif a[b] =="x":
            d="-..-"
        elif a[b] =="y":
            d="-.--"
        elif a[b] =="z":
            d="--.."
        elif a[b] ==" ":
            d="/"
        else:
            d="/"
        e+=" "
        e+= d
        b+=1
    print(e)
    y=input()

def numtwo():
    a=str(input("INPUT CODE PLS  \n"))
    b=len(a)
    c=0
    d=""
    e=""
    a+=" "
    while c<b:
        if a[c+1]!=" ":
            d+=a[c]
            c=c+1
        else:
            d+=a[c]
            if d == ".-":
                f="a"
            elif d =="-...":
                f="b"
            elif d =="-.-.":
                f="c"
            elif d =="-..":
                f="d"
            elif d ==".":
                f="e"
            elif d =="..-.":
                f="f"
            elif d =="--.":
                f="g"
            elif d =="....":
                f="h"
            elif d =="..":
                f="i"
            elif d ==".---":
                f="j"
            elif d =="-.-":
                f="k"
            elif d ==".-..":
                f="l"
            elif d =="--":
                f="m"
            elif d =="-.":
                f="n"
            elif d =="---":
                f="o"
            elif d ==".--.":
                f="p"
            elif d =="--.-":
                f="q"
            elif d ==".-.":
                f="r"
            elif d =="...":
                f="s"
            elif d =="-":
                f="t"
            elif d =="..-":
                f="u"
            elif d =="...-":
                f="v"
            elif d ==".--":
                f="w"
            elif d =="-..-":
                f="x"
            elif d =="-.--":
                f="y"
            elif d =="--..":
                f="z"
            elif d=="/":
                f=" "
            else:
                f=" "
            d=""
            e+=f
            c+=2
    print("\n")
    print(e)
    y=input()


print("Only input lower case letters. Leave one space gap between each letter and a ( / ) unit between each word. Don't input punctuation or dots along the text.All these things if not followed can cause errors \n \n")
print("Input 1 for text to morse and input 2 for morse to text :- ")
z=int(input())
if z==1:
    numone()
else:
    numtwo()

