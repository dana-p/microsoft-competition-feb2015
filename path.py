'''
SNICKERDOODLE
SNICKE
NRCRDO
IEKODS
CRDOLE
Example output

SNI...
..C...
.EKOD.
.RDOLE
'''


f = open("data4.txt")
data = f.readlines()

word = data[0].strip();  
word_part = word.strip(); 

print word
dataPath = data[1:]
path = []; 

for d in dataPath:
    path.append(list(d.strip())); 

total_paths = []

line_path = []
Xpos = 0; 
Ypos = 0; 
bad_paths = []

doneletters = []

for letter in word_part: 
    
    if letter == path[Ypos][Xpos]: #flip? 
        line_path.append([Ypos, Xpos])
        doneletters.append(letter); 

    