'''
10.0.0.1 11.199.88.254 1000.43.59.96
10.0.0.1 11.199.88.254 10.43.59.96
10.0.0.1 11.199.88.254 111.19.12.154
Example output

InValid
InRange
OutRange
'''

def checkIfValid(num):
    num_parts = num.split('.');
    if len(num_parts) != 4: 
        return False; 
    for part in num_parts: 
        if (int(part) > 255 or int(part) < 0): 
            return False; 
    return True; 

def convertToBin(inputStrNum): 
    return ''.join([bin(int(x)+256)[3:] for x in inputStrNum.split('.')])
    

f = open("data2.txt")
data = f.readlines()

input_IPs = []  

for d in data:
    # parse input, assign values to variables
    input_IPs.append(d.split()); 

for completeSet in input_IPs:
    if (not(checkIfValid(completeSet[2]))): 
        print 'InValid' 
    else:
        firstNumBin = convertToBin(completeSet[0])
        secondNumBin = convertToBin(completeSet[1])
        thirdNumBin = convertToBin(completeSet[2])
        if (thirdNumBin >= firstNumBin and thirdNumBin <= secondNumBin): 
            print 'InRange'
        else: 
            print 'OutRange'