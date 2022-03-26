# Find the string with max occurance, return string and it's occurance

lines=["1.1.1.1","1.1.1.1","1.1.1.1","1.1.1.2","1.2.1.2","2.1.1.2","1.1.1.2"]
info={}

for line in lines:
    if line in info:
        # If elem is already present increment val by one
        info.update({line: info[line]+1})
    else:
        # If elem is inserted for the first time
        info.update({line: 1})

max_number=0,0  # 0=>elem,0=>count
for k,v in info.items():
    if v > max_number[-1]:
        max_number=k,v

print(max_number)

