'''Raw data set'''
a = open("/home/null/Desktop/Python_program_Warehouse/IDS project/testset.csv","r")

'''Randomly generated numbers using an online number generator'''
b = open("/home/null/Desktop/Python_program_Warehouse/IDS project/numbers.txt", "r")

'''Final data set'''
c = open("/home/null/Desktop/Python_program_Warehouse/IDS project/temp.csv", "w")

'''Creating a list for the numbers and retireving the numbers from it's file'''
sample = list()
line = b.readline()
for word in line.split(" "):
    sample.append(int(word))
lines = a.readlines()

'''Generating the new dataset and adding it to the new csv file'''
for x in range(100992):
    if x in sample:
        data = lines[x].strip()
        print(data, file=c)
