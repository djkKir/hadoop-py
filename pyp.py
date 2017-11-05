import sys

# s = {"1448713968	user2	https://ru.wikipedia.org/",
#         "448764519	user10	https://stepic.org/",
#          "1448713968	user5	http://google.com/",
#          "1448773411	user10	https://stepic.org/explore/courses",
#           "1448709864	user3	http://vk.com/"}

#rFunction1 select where
# for line in s:
#  jj = line.strip().split("\t")
#  if jj[1] == "user10":
#   print(line)

#rFunction2 select
# for line in s:
#  jj = line.strip().split("\t")
#  print(jj[2])

f = ["1	A",
     "2	A",
     "2	B",
     "3	B"]

#(lastkey, s) = (None, 0)

#RF3 join
# for line in f:
#  (key, value) = line.strip().split('\t')
#  if lastkey  != key:
#   print (key)
#   (lastkey, s) = (key, value)

#RF4 join in
# for line in f:
#  (key, val) = line.strip().split('\t')
#  if lastkey != key:
#   (lastkey, s ) = (key, 1)
#  else:
#   (lastkey,s) = (key, s + 1)
#   print(lastkey)

#RF5 B - A
# simple output: 1
(lastkey, val) = (None, None)
(bkey, b) = (None, None)

for line in f:
 (key, value) = line.strip().split('\t')
 if key != lastkey:
     (lastkey,val) =(key,value)
     print(val + ' : ' + lastkey)
 elif lastkey ==key and value == 'A':
     print(value)









