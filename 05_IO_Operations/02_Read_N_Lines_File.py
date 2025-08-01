# Program 2: Read first n lines from a text file

filename = input("Enter the filename: ")
n = int(input("Enter number of lines to read: "))

with open(filename, 'r') as file:
   for i in range(n):
      line = file.readline()
      if line == '':
            break
      print("Line",(i+1),":",(line.strip()))
      # print(f"Line {i+1}: {line.strip()}")
