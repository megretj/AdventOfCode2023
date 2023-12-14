# let t be the time of the race, 
# r the current record,
# distance travelled is d,
# time with button pressed is x.
# d = (t-x)*x = t*x - x^2
# So we must find all x, such that d = t*x - x^2 > r.
# For that, we can simply solve the equation x^2 - t*x + r = 0 (x = (t+-sqrt(t^2-4*r))/2)
# to extract the pressing times that equate the record. Then every integer between x_0 and x_1 will beat the record.
import re
import math

def findRange(t, r):
    if t**2-4*r < 0:
        print("big problem, shouldn't do this")
        return 0
    delta = math.sqrt(t**2-4*r)
    x0 = (t+delta)/2
    x1 = (t-delta)/2
    print(x0,x1)

    tolerance = 0.001
    print("tolerance = "+str(tolerance))
    if abs(x0-int(x0))<tolerance:
        x0 = int(x0) - 1
    else:
        x0 = math.floor(x0)

    if abs(x1-int(x1)) < tolerance:
        x1 = int(x1)+1
    else:
        x1 = math.ceil(x1)


    print(x0,x1,x0-x1+1)
    return x0-x1+1

def part2():
    total = 1
    with open('inputs/day6.txt') as f:
        times = [int(time) for time in re.findall('\d+',f.readline().replace(" ",""))]
        records = [int(record) for record in re.findall('\d+',f.readline().replace(" ",""))]
        print(times)
        print(records)
        for i, time in enumerate(times):
            total *= findRange(time,records[i])
    return total

def part1():
    total = 1
    with open('inputs/day6.txt') as f:
        times = [int(time) for time in re.findall('\d+',f.readline())]
        records = [int(record) for record in re.findall('\d+',f.readline())]
        print(times)
        print(records)
        for i, time in enumerate(times):
            total *= findRange(time,records[i])
    return total

# print(part1())
print(part2())