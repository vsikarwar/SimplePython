'''
Created on Feb 10, 2015

@author: sikarwv
'''
total_records = 3000000
fields = [20, 17, 4, 10, 3, 32, 15, 4000, 38, 15, 12, 1, 2, 64, 4000, 256, 64, 64, 64,12, 256, 256, 256, 8, 8, 8, 256, 8, 4,
          256, 256, 1, 2, 32, 64, 32]

for i in range(len(fields)): fields[i] = fields[i] * 2 #2 bytes for each char
for i in range(len(fields)) : fields[i] = fields[i] + 16 #16 bytes for book keeping

sum = 0
for i in fields : sum += i
mem = total_records * sum

print("Memory Usage :")
print(str(mem) + " bytes")
print(str(mem/1024) + " kb")
print(str(mem/(1024*1024)) + " mb")
print(str(mem/(1024*1024*1024)) + " gb")