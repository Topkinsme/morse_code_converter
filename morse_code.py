#code by top

def numone():
    inpute=str(input("INPUT PLS  \n"))
    count=0
    length=len(inpute)
    output=""
    while count<length:
        if inpute[count] == "a":
            morse=".-"
        elif inpute[count] =="b":
            morse="-..."
        elif inpute[count] =="c":
            morse="-.-."
        elif inpute[count] =="d":
            morse="-.."
        elif inpute[count] =="e":
            morse="."
        elif inpute[count] =="f":
            morse="..-."
        elif inpute[count] =="g":
            morse="--."
        elif inpute[count] =="h":
            morse="...."
        elif inpute[count] =="i":
            morse=".."
        elif inpute[count] =="j":
            morse=".---"
        elif inpute[count] =="k":
            morse="-.-"
        elif inpute[count] =="l":
            morse=".-.."
        elif inpute[count] =="m":
            morse="--"
        elif inpute[count] =="n":
            morse="-."
        elif inpute[count] =="o":
            morse="---"
        elif inpute[count] =="p":
            morse=".--."
        elif inpute[count] =="q":
            morse="--.-"
        elif inpute[count] =="r":
            morse=".-."
        elif inpute[count] =="s":
            morse="..."
        elif inpute[count] =="t":
            morse="-"
        elif inpute[count] =="u":
            morse="..-"
        elif inpute[count] =="v":
            morse="...-"
        elif inpute[count] =="w":
            morse=".--"
        elif inpute[count] =="x":
            morse="-..-"
        elif inpute[count] =="y":
            morse="-.--"
        elif inpute[count] =="z":
            morse="--.."
        elif inpute[count] =="1":
            morse=".----"
        elif inpute[count] =="2":
            morse="..---"
        elif inpute[count] =="3":
            morse="...--"
        elif inpute[count] =="4":
            morse="....-"
        elif inpute[count] =="5":
            morse="....."
        elif inpute[count] =="6":
            morse="-...."
        elif inpute[count] =="7":
            morse="--..."
        elif inpute[count] =="8":
            morse="---.."
        elif inpute[count] =="9":
            morse="----."
        elif inpute[count] =="0":
            morse="-----"
        elif inpute[count] ==" ":
            morse="/"
        else:
            morse="?"
        output+=" "
        output+= morse
        count+=1
    print(output)
    y=input()

def numtwo():
    inpute=str(input("INPUT CODE PLS  \n"))
    length=len(inpute)
    count=0
    partinput=""
    output=""
    inpute+=" "
    while count<length:
        if inpute[count+1]!=" ":
            partinput+=inpute[count]
            count=count+1
        else:
            partinput+=inpute[count]
            if partinput == ".-":
                text="a"
            elif partinput =="-...":
                text="b"
            elif partinput =="-.-.":
                text="c"
            elif partinput =="-..":
                text="d"
            elif partinput ==".":
                text="e"
            elif partinput =="..-.":
                text="f"
            elif partinput =="--.":
                text="g"
            elif partinput =="....":
                text="h"
            elif partinput =="..":
                text="i"
            elif partinput ==".---":
                text="j"
            elif partinput =="-.-":
                text="k"
            elif partinput ==".-..":
                text="l"
            elif partinput =="--":
                text="m"
            elif partinput =="-.":
                text="n"
            elif partinput =="---":
                text="o"
            elif partinput ==".--.":
                text="p"
            elif partinput =="--.-":
                text="q"
            elif partinput ==".-.":
                text="r"
            elif partinput =="...":
                text="s"
            elif partinput =="-":
                text="t"
            elif partinput =="..-":
                text="u"
            elif partinput =="...-":
                text="v"
            elif partinput ==".--":
                text="w"
            elif partinput =="-..-":
                text="x"
            elif partinput =="-.--":
                text="y"
            elif partinput =="--..":
                text="z"
            elif partinput ==".----":
                text="1"
            elif partinput =="..---":
                text="2"
            elif partinput =="...--":
                text="3"
            elif partinput =="....-":
                text="4"
            elif partinput ==".....":
                text="5"
            elif partinput =="-....":
                text="6"
            elif partinput =="--...":
                text="7"
            elif partinput =="---..":
                text="8"
            elif partinput =="----.":
                text="9"
            elif partinput =="-----":
                text="0"
            elif partinput=="/":
                text=" "
            else:
                text=" "
            partinput=""
            output+=text
            count+=2
    print("\n")
    print(output)
    y=input()

    
print("Only input lower case letters. Leave one space gap between each letter and a ( / ) unit between each word. Don't input punctuation or dots along the text.All these things if not followed can cause errors \n \n")
print("Input 1 for text to morse and input 2 for morse to text :- ")
tempchoice=int(input())
if tempchoice==1:
    numone()
else:
    numtwo()
