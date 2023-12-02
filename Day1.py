import re

def getNumber(line):
 number = "0"
 twoNumbers = re.search('(\d).*(\d)\D*$',line)
 if twoNumbers:
   number=twoNumbers.group(1)+twoNumbers.group(2)
 else:
   oneNumber = re.search('(\d)',line)
   if oneNumber:
     number = oneNumber.group(1)+oneNumber.group(1)
 return int(number)
 
def replaceNumbers(line):
 numbers = ['one','two','three','four','five','six','seven','eight','nine',"oneight", "twone", "eightwo",'eighthree','nineight','fiveight','threeight','sevenine']
 numberss = [1,2,3,4,5,6,7,8,9,18,21,82,83,98,58,38,79]
 numberToReplace = 0
 currentIndex = 1000
 while numberToReplace > -1:
   numberToReplace = -1
   currentIndex = 1000
   for i, n in enumerate(numbers):
     index = line.find(n)
     if index > -1 and index <= currentIndex:
       currentIndex = index
       numberToReplace = i
   if numberToReplace > -1:
     line = line.replace(numbers[numberToReplace],"{}".format(numberss[numberToReplace]),1)
 return line
  
total = 0
with open('input.txt') as f:
  for line in f:
    # For part 1, comment out this line
    line = replaceNumbers(line)
    total += getNumber(line)
print(total)
