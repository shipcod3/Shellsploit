data = open("test.py", "r")
for x in data.readlines():
	if "#define" in x.strip():
		x = x.strip().replace("#define	SYS_", "").split("\t")
		#print x[0],x[]
		if x[1] == "":
			print '"%s":"%s",' % (x[0],x[2])
		else:
			print '"%s":"%s",' % (x[0].replace("__", ""),x[1].replace("__", ""))

