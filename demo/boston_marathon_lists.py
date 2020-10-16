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

name = []
gender = []
age = []
division = []
country = []
time = []

with open('bm_results2012.txt') as f:

    lines = f.readlines()

    lnr = 0
    
    for line in lines:
        lnr += 1
        split = line.split(',')

        name.append(split[0])
        gender.append(split[1])
        age.append(int(split[2]))
        division.append(int(split[3]))
        country.append(split[4]) 
        time.append(float(split[5]))


plt.hist(time, 20, edgecolor='black')
plt.title('2012 Boston Marathon')
plt.xlabel('Minutes to Complete Race')
plt.ylabel('Number of Runners')
plt.show()