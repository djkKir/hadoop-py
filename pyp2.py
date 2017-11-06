f = ["1	A",
     "2	A",
     "2	B",
     "3	B",
     "4	A",
     "5	B",
     ]

#RF5 B - A
# simple output: 1
(lastkey, val) = (None, None)
#print(f)

for line in f:
 (key, value) = line.strip().split('\t')
 if lastkey and lastkey != key:
     if value =='A':
             if  val and val == value:
                 print(lastkey)

     (lastkey,val) = (key,value)

 else:
     (lastkey, val) = (key, value)
if val and val=='A':
    print(lastkey)


