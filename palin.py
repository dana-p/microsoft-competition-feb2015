import re

def is_pal(s):
    return s == s[::-1]
 
def flp(s, orig_s):
    start = 0; 
    length = 0; 
    longest, len_longest  = '', 0
    for i in range(len(s)):
        for j in range(2,len(s[i:])):
            sub_s = s[i:i+j+1]
            if is_pal(sub_s) and len(sub_s) > len_longest:
                longest, len_longest = sub_s, j+1
                start = i;
                length = len_longest; 
    return (longest, start, length + start)

f = open("data5.txt").readlines()

sentences= []
orig_sentences = [];
sentences_nospace = [];
sentences_reversed = []; 

for d in f:
    mystr = ("".join(re.findall("[a-zA-Z]+", d))).lower();
    sentences.append(mystr)
    sentences_reversed.append((mystr)[::-1])
    orig_sentences.append(d); 

for k in range(len(sentences)): 
    pal, i, j = flp(sentences[k], orig_sentences[k])
    print pal, i , j
    
    o_split = list(orig_sentences[k])
    
    counter = 0; 
    mybool = False; 
    mysentence = ""; 
    for l in range(len(o_split)): 
        if o_split[l].isalpha():
            if mybool: 
                for o in range(l,l+j):
                    print o_split[o]
                    mysentence = mysentence + o_split[o]; 
            counter = counter + 1; 
            if (counter == i): 
                mybool = True; 

    print mysentence
