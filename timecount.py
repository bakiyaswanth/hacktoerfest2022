import time
start= time.time()
file = open('try.txt', 'r')
count = 0
for lines in file:
    if lines!='\n':
        count+=1
file.close()
print(count)
end= time.time()
print('The time required to run this program: ',end-start)
