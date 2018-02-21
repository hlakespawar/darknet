import sys

filename = "logfile.txt"


with open(filename, 'r') as file:
	lines = file.read().splitlines()

objects = {}

for i in range(0, len(lines)):
	entry = lines[i].split(' ')[3:5]

	if not (entry[1] in objects):
		objects[entry[1]] = {} #create new dictionary associated with the key "class"

	objects[entry[1]][int(entry[0])] = True #add entry if it exists


# decide if there is a class to filter on
if len(sys.argv) == 1:
	# just print the frames for default list
	l = ['person', 'car']
	print "Using the default list: ",l,"\n"
else:
	l = sys.argv[1:]
	print "Filtering on: ",l,"\n"


frames = []
for k in l:
	if k in objects:
		frames += objects[k].keys()
		
	else:
		print "Didn't get any "+k,"\n"

eframes = sorted(set().union(frames))
print eframes

for f in range(0,len(eframes)):
	if f == 0:
		select = "select=e(n\\,"+str(eframes[f])+")"
	else:
		select += "+e(n\\,"+str(eframes[f])+")"

#cmd = """ffmpeg -i %s -vf "%s" -vframes 1 %s""" % (video, select, results)

