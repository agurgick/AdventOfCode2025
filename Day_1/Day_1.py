

#create dial
dial = []

for num in range(100):
    dial.append(num)
#print(dial)

position = int(input("What is the starting number of the dial? ")) + 1
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
for code in codes:
    st_code = str(code)
    if st_code[0] == "R":
        #print("This is Rigth")
        num_code = int(st_code[1:])
        if num_code < position:
            position = position - num_code

        print(num_code)
        print(position)
    elif st_code[0] == "L":
        print("This is Left")
    else:
        print("This is not left or right")