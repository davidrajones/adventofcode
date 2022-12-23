import argparse
import re




parser = argparse.ArgumentParser(description='Beacon Exclusion Zone')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
datapoints = list()
with open(args.infile) as input:
    for line in input.readlines():
        sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line.strip()))
        datapoints.append(((sx, sy), (bx, by)))

sensor_list = set([s for s,b in datapoints])
beacon_list = set([b for s,b in datapoints])
distances = {s: abs(s[0]-b[0])+abs(s[1]-b[1]) for  s,b in datapoints}
print(distances)

min_x = min(sensor[0]-dist for sensor, dist in distances.items())
max_x = max(sensor[0]+dist for sensor, dist in distances.items())

y = 2000000
total = 0
for thisx in range(min_x,max_x+1):
    if (thisx, y) in beacon_list:
        continue
    for s in sensor_list:
        this_dist = abs(thisx - s[0])+abs(y - s[1])
        max_dist = distances[s]
        if this_dist <= max_dist:
            total += 1
            break

print (f"Part 1 {total}")


def is_good_loc_check(x, y, max):
    if 0 <= x <= max and 0 <= y <= max:
        if all(abs(x - sensor[0]) + abs(y - sensor[1]) > distances[sensor] for sensor in sensor_list):
            print (f"Part 2 {4000000 * x + y}")
            exit(0)

# Part 2
max_xy = 4000000
# Iterate through every sensor and its distance
for (snesx,sensy), dist in distances.items():
    dist+=1 # Go one outside the distance from this sensor
    #Iterate through the edges if the distance to see if there's a free space
    # Look below sensor (-)
    for i, x in enumerate(range(snesx-dist, snesx)):
        for y in (sensy+i, sensy-i):
            is_good_loc_check(x, y, max_xy)
    # Look above sensor (+)
    for i, x in enumerate(range(snesx, snesx+dist+1)):
        for y in ((sensy+dist)-i, (sensy-dist)+i):
            is_good_loc_check(x, y ,max_xy) 
