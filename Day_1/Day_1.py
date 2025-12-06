

#create dial
dial = []

for num in range(100):
    dial.append(num)
#print(dial)

position = int(input("What is the starting position")) + 1
#print(position)

codes = []

#import and read each link for Day_1code.txt and turn codes into a dic
try:
    with open("Day_1_codes.txt", "r") as file:
        for line in file:
            codes.append(line.strip())
        #codes = file.readlines()
        print(codes)
except FileNotFoundError:
    print("Error: The file 'ay_1_codes.txt' was not found.")

    #for each item in dictionary remove + or - and turn dial 
