prompt = "Enter filename: "
titles = "char       count\n----       -----"
itemfmt = "{0:5s}{1:10d}"
totalfmt = "total{0:10d}"
whiteSpace = {' ':'space', '\t':'tab', '\n':'nline', '\r':'crtn'}


def letterFrequency (text):
    text= text.lower()
    lcount={}
    whitespace={}
    for ch in text:
        if ch == "\t" :
            whitespace [ch]= whitespace.get(ch,0)+1
        if ch == "\n":
            whitespace [ch]= whitespace.get(ch,0)+1
        if ch == " ":
            whitespace [ch]= whitespace.get(ch,0)+1
        else:
            ch = ch
            text.split()
            lcount[ch]= lcount.get(ch,0)+1
            
    wlistc= list(whitespace)
    wlistc.sort()
    for item in wlistc:
        ccount= whitespace[item]
        print (itemfmt.format(whiteSpace[item], ccount))

    if "\t" in lcount:
        del lcount["\t"]

    if "\n" in lcount:
        del lcount["\n"]
        
    listc= list(lcount)
    listc.sort()
    for item in listc:
        print (itemfmt.format(item,lcount[item]))
        

def totalChars(text):
    chars= 0
    for line in text:
        w= line.split()
        chars+= len(line)
    
    print (totalfmt.format(chars))

      

import urllib.request
file= input (prompt)
file
filename= str(file)
print(titles)

if 'http' in filename[0:4]:
    page= urllib.request.urlopen(filename)
    readfile= page.read().decode("utf-8")
else:
    page= open(filename, 'r')
    readfile= page.read()

ch= letterFrequency(readfile)

if 'http' in filename[0:4]:
    page= urllib.request.urlopen(filename)
    readfile= page.read().decode("utf-8")
        
else:
    page= open(filename, 'r')
    readfile= page.read()
    
total= totalChars(readfile)
    
page.close()
    
