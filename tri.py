import sys,string,md5
print("Please enter your full name ")
line = sys.stdin.readline()
line = line.rstrip()
md5_object = md5.new()
md5_object.update(line)
print (md5_object.hexdigest())
exit