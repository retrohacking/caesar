import sys
import string

if len(sys.argv)!=4:
	sys.exit ("Usage\n\t"+ sys.argv[0]+" <add/sub> <index> <string>\n")

op=sys.argv[1]

if sys.argv[2].isnumeric():
	index=int(sys.argv[2])
else:
	sys.exit("Usage\n\t"+ sys.argv[0]+" <add/sub> <index> <string>\n\tUse a numeric index\n")

text=sys.argv[3]

def add():
	new_string=""
	for char in text:
		if char not in string.ascii_lowercase and char not in string.ascii_uppercase and not char.isnumeric():
			new_string+=char
			continue
		if char.isnumeric():
			new_string+=str((int(char)+index)%10)
		if char in string.ascii_lowercase:
			if string.ascii_lowercase.index(char)+index%26>25:
				new_string+=string.ascii_lowercase[string.ascii_lowercase.index(char)+index%26-26]
			else: new_string+=string.ascii_lowercase[string.ascii_lowercase.index(char)+index%26]
		if char in string.ascii_uppercase:
			if string.ascii_uppercase.index(char)+index%26>25:
				new_string+=string.ascii_uppercase[string.ascii_uppercase.index(char)-26+index%26]
			else: new_string+=string.ascii_uppercase[string.ascii_uppercase.index(char)+index%26]
	sys.exit(new_string)


def sub():
	new_string=""
	for char in text:
		if char not in string.ascii_lowercase and char not in string.ascii_uppercase and not char.isnumeric():
			new_string+=char
			continue
		if char.isnumeric():
			if int(char)-(index%10)<0:
				new_string+=str(int(char)+10-(index%10))
			else: new_string+=str((int(char)-(index%10)))
		if char in string.ascii_lowercase:
			if string.ascii_lowercase.index(char)-index%26<0:
				new_string+=string.ascii_lowercase[string.ascii_lowercase.index(char)-index%26+26]
			else: new_string+=string.ascii_lowercase[string.ascii_lowercase.index(char)-index%26]
		if char in string.ascii_uppercase:
			if string.ascii_uppercase.index(char)-index%26<0:
				new_string+=string.ascii_uppercase[string.ascii_uppercase.index(char)-index%26+26]
			else: new_string+=string.ascii_uppercase[string.ascii_uppercase.index(char)-index%26]
	sys.exit(new_string)

if (sys.argv[1]=="add"):
	add()

if (sys.argv[1]=="sub"):
	sub()

sys.exit ("Usage\n\t"+ sys.argv[0]+" <add/sub> <index> <string>\n")


