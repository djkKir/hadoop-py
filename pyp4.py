#union stdin
#  Sample Input:
# user1	query:гугл
# user1	url:google.ru
# user2	query:стэпик
# user2	query:стэпик курсы
# user2	url:stepic.org
# user2	url:stepic.org/explore/courses
# user3	query:вконтакте
#
# Sample Output:
# user1	гугл	google.ru
# user2	стэпик	stepic.org
# user2	стэпик	stepic.org/explore/courses
# user2	стэпик курсы	stepic.org
# user2	стэпик курсы	stepic.org/explore/courses

f=["user1	query:гугл",
   "user1	url:google.ru",
   "user2	query:стэпик",
   "user2	query:стэпик курсы",
   "user2	url:stepic.org",
   "user2	url:stepic.org/explore/courses",
   "user3	query:вконтакте"]

k = None
qer = list()
urls = list()
for line in f:
    (key, vk) = line.strip().split('\t')
    if k and k != key:
        #print(qer)
        #print(urls)
        #print(k)
        for q in qer:
            for u in urls:
                print(k + "\t" + q + "\t" + u)

        qer.clear()
        urls.clear()

        k = key
        (k1, v1) = vk.strip().split(":")
        if k1 == 'query':
            qer.append(v1)
        elif k1 == 'url':
            urls.append(v1)
    else:
        k=key
        (k1, v1) = vk.strip().split(":")
        if k1 == 'query':
            qer.append(v1)
        elif k1 == 'url':
           urls.append(v1)
for q in qer:
            for u in urls:
                print(k + "\t" + q + "\t" + u)