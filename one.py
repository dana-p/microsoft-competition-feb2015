'''
Example input

55 5 1 5
0 0 5
1 5 56
2 5 56
3 57 55
4 56 57
Example output

STOPPED: 3 4
TIME: 13
PATH: 0 1 4 3
'''

class escalator:
    def __init__(self, ID, start, end, escalator_time):
        self.ID = ID; 
        self.start = start; 
        self.end = end; 
        self.escalator_time = escalator_time
    
    def direction(self): #true means going up
        if (self.start < self.end): 
            return True
        return False
    
    def time(self, escalator_time, walking_speed):
        walking = (abs(self.start - self.end)) * walking_speed; 
        if  (walking < escalator_time): 
            return walking; 
        return escalator_time; 
    
    def includes_floor(self, floor):
        if (self.direction):
            if (floor <= self.end and floor >= self.start): 
                return True; 
        else: 
            if (floor >= self.end and floor <= self.start):
                return True; 
        return False; 
    
    def ends_at(self, floor):
        if (floor == self.end):
            return True; 
        return False; 
    
f = open("data.txt")
data = f.readlines()

input_str = "";  

for d in data:
    # parse input, assign values to variables
    input_str = input_str + d; 

input_parsed = input_str.split(); 

targetFloor    = int(input_parsed[0]); 
escalator_time = int(input_parsed[1]); 
walking_speed  = int(input_parsed[2]); 
num_escalators = int(input_parsed[3]); 

escalators = []; 
S = 4; 

for i in range(num_escalators):
    escalators.append(escalator(int(input_parsed[S]), int(input_parsed[S+1]), int(input_parsed[S+2]), escalator_time)); 
    S = S + 3; 

escalator_ends = []; 



for esc in escalators: 
    if (esc.ends_at(targetFloor)): 
        escalator_ends.append(esc); 
        

