'''
myth

Greek mythology is the body of myths and teachings that belong to the ancient Greeks, concerning their gods and heroes, the nature of the world, and the origins and significance of their own cult and ritual practices. It was a part of the religion in ancient Greece. Modern scholars refer to and study the myths in an attempt to throw light on the religious and political institutions of Ancient Greece and its civilization, and to gain understanding of the nature of myth itself.
Example output

1;4;mythology
'''

import re

with open ("data3.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

f = open("data3.txt")


input_term = ((f.readline()).strip()).lower()
sample_sentence = " ".join(re.findall("[a-zA-Z]+", data))




sentence_parts = sample_sentence.split(' ');  

completeTokens = 0; 
partialTokens = 0;
ignoreFirst = False;  
firstMatch = ""; 

for s_part in sentence_parts:  
    if ((s_part.lower()).startswith(str(input_term))):
        
        if ignoreFirst == True:
            if firstMatch == "" and ignoreFirst: 
                firstMatch = s_part; 
            
            partialTokens = partialTokens + 1; 
            
            if (s_part.lower() == input_term):  
                completeTokens = completeTokens + 1; 
        
        ignoreFirst = True; 
            
print str(completeTokens) + ';' + str(partialTokens) + ';' + firstMatch; 
