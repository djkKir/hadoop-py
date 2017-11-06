f = ["1	A",
     "1	B",
     "2	A",
     "2	B"
     ]

#RF6 B simetric diff A
# simple output:    1
#                   3
#                   4
#                   5
(lastkey, val) = (None, None)
count = 0
#print(f)

for line in f:
 (key, value) = line.strip().split('\t')
 if lastkey and lastkey != key:
     if count < 2:
         print(lastkey)

     (lastkey,val) = (key,value)
     count=1

 else:
     (lastkey, val) = (key, value)
     count = count + 1
if val and count < 2:
    print(lastkey)