aa=[11,333,1,44]
max_num=0
sec_max_num=0

for val in aa:
    if val > max_num:
        max_num = sec_max_num
        sec_max_num = val
    elif val > sec_max_num:
        sec_max_num = val

print(max_num, sec_max_num)