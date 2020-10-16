# Read the contents of the given file. Assumes the file 
# in a comma-separated format, with 6 elements in each entry:
# 0. Name (string),
# 1. Gender (string)
# 2. Age (int)
# 3. Division (int),
# 4. Country (string),
# 5. Overall time (float)   
#

import matplotlib.pyplot as plt

data = {
    'name': [],
    'gender': [],
    'age': [],
    'division': [],
    'country': [],
    'time': []
}

with open('bm_results2012.txt') as f:

    lines = f.readlines()
    
    print(type(lines))
    print(lines[0])
    print(len(lines))

    lnr = 0
    
    for line in lines:
        lnr += 1
        split = line.split(',')
        if lnr == 1:
            print(split)
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(int(split[2]))
        data['division'].append(int(split[3]))
        data['country'].append(split[4]) 
        data['time'].append(float(split[5]))


plt.hist(data['time'], 20, edgecolor='black')
plt.title('2012 Boston Marathon')
plt.xlabel('Minutes to Complete Race')
plt.ylabel('Number of Runners')
plt.show()