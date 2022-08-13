letters = []
ststrgf = open("ststrgf.txt", "a")

brain_fuck_words = [
    "++++++++++[>+++++++++<-]>+++++++.<++++++++++[>---------<-]>-------<", #A-0
    "+++++++++[>+++++++++++<-]>-.<+++++++++[>-----------<-]>+", #B-1
    "+++++++++[>++++++++++<-]>+++++++++.<+++++++++[>----------<-]>---------<", #C-2
    "++++++++++[>++++++++++<-]>.<++++++++++[>----------<-]<", #D-3
    "++++++++++[>++++++++++<-]>+.<++++++++++[>----------<-]>-<", #E-4
    "++++++++++[>++++++++++<-]>++.<++++++++++[>----------<-]>--<", #F-5
    "++++++++++[>++++++++++<-]>+++.<++++++++++[>----------<-]>---<", #G-6
    "++++++++++[>++++++++++<-]>++++.<++++++++++[>----------<-]>----<", #H-7
    "++++++++++[>++++++++++<-]>+++++.<++++++++++[>----------<-]>-----<", #I-8
    "++++++++++[>++++++++++<-]>++++++.<++++++++++[>----------<-]>------<" ,#J-9
    "++++++++++[>++++++++++<-]>+++++++.<++++++++++[>----------<-]>-------<" ,#K-10
    "++++++++++[>++++++++++<-]>++++++++.<++++++++++[>----------<-]>--------<" ,#L-11
    "++++++++++[>++++++++++<-]>+++++++++.<++++++++++[>----------<-]>---------<" ,#M-12
    "++++++++++[>+++++++++++<-]>.<++++++++++[>-----------<-]<" ,#N-13
    "++++++++++[>+++++++++++<-]>+.<++++++++++[>-----------<-]>-<" ,#O-14
    "++++++++++[>+++++++++++<-]>++.<++++++++++[>-----------<-]>--<" ,#P-15
    "++++++++++[>+++++++++++<-]>+++.<++++++++++[>-----------<-]>---<" ,#Q-16
    "+++++++++++[>++++++++++<-]>++++.<+++++++++++[>----------<-]>----<" ,#R-17
    "+++++++++++[>++++++++++<-]>+++++.<+++++++++++[>----------<-]>-----<" ,#S-18
    "+++++++++++[>++++++++++<-]>++++++.<+++++++++++[>----------<-]>------<" ,#T-19
    "+++++++++++[>++++++++++<-]>+++++++.<+++++++++++[>----------<-]>-------<" ,#U-20
    "+++++++++++[>++++++++++<-]>++++++++.<+++++++++++[>----------<-]>--------<" ,#V-21
    "+++++++++++[>++++++++++<-]>+++++++++.<+++++++++++[>----------<-]>---------<" ,#W-22
    "++++++++++[>++++++++++++<-]>.<++++++++++[>------------<-]><" ,#X-23
    "++++++++++[>++++++++++++<-]>+.<++++++++++[>------------<-]>-<" ,#Y-24
    "++++++++++[>++++++++++++<-]>++.<++++++++++[>------------<-]>--<" #Z-25
]

word = input("enter the word: ")
word.lower()
for i in word:
    letters.append(i)
for letter in letters:
    if letter == "a":
        ststrgf.write(brain_fuck_words[0]+"\n")
    if letter == "b":
        ststrgf.write(brain_fuck_words[1]+"\n")
    if letter == "c":
        ststrgf.write(brain_fuck_words[2]+"\n")
    if letter == "d":
        ststrgf.write(brain_fuck_words[3]+"\n")
    if letter == "e":
        ststrgf.write(brain_fuck_words[4]+"\n")
    if letter == "f":
        ststrgf.write(brain_fuck_words[5]+"\n")
    if letter == "g":
        ststrgf.write(brain_fuck_words[6]+"\n")
    if letter == "h":
        ststrgf.write(brain_fuck_words[7]+"\n")
    if letter == "i":
        ststrgf.write(brain_fuck_words[8]+"\n")
    if letter == "j":
        ststrgf.write(brain_fuck_words[9]+"\n")
    if letter == "k":
        ststrgf.write(brain_fuck_words[10]+"\n")
    if letter == "l":
        ststrgf.write(brain_fuck_words[11]+"\n")
    if letter == "m":
        ststrgf.write(brain_fuck_words[12]+"\n")
    if letter == "n":
        ststrgf.write(brain_fuck_words[13]+"\n")
    if letter == "o":
        ststrgf.write(brain_fuck_words[14]+"\n")
    if letter == "p":
        ststrgf.write(brain_fuck_words[15]+"\n")
    if letter == "q":
        ststrgf.write(brain_fuck_words[16]+"\n")
    if letter == "r":
        ststrgf.write(brain_fuck_words[17]+"\n")
    if letter == "s":
        ststrgf.write(brain_fuck_words[18]+"\n")
    if letter == "t":
        ststrgf.write(brain_fuck_words[19]+"\n")
    if letter == "u":
        ststrgf.write(brain_fuck_words[20]+"\n")
    if letter == "v":
        ststrgf.write(brain_fuck_words[21]+"\n")
    if letter == "w":
        ststrgf.write(brain_fuck_words[22]+"\n")
    if letter == "x":
        ststrgf.write(brain_fuck_words[23]+"\n")
    if letter == "y":
        ststrgf.write(brain_fuck_words[24]+"\n")
    if letter == "z":
        ststrgf.write(brain_fuck_words[25]+"\n")

ststrgf.close()

f = open('ststrgf.txt', "r")
f_contents = f.read()
print("\n","\n",f_contents)
f.close()

f = open('ststrgf.txt', 'r+')
f.truncate(0)
