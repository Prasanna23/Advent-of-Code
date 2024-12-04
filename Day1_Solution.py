### The idea is to read the input file and parse it into two lists after striping blank spaces
### Sort the lists, do an absolute difference between the list elements to create difference list, sum on the list will give you the total for part 1
### sequence through sorted list 1 and find the occuenrences in sorted list 2 to create similarity score list for part 2 puzzle.
with open('day1_inp.txt') as f:
    lines = f.readlines()
    f.close()
my_dict = {}
l1 = []
l2 = []
diff_lst = []
sim_score = []
for line in lines:
    line = line.split()
    line = [i.strip() for i in line]
    l1.append(int(line[0]))
    l2.append(int(line[1])) 
l1_srt = sorted(l1)
l2_srt = sorted(l2)
for num1, num2 in zip(l1_srt, l2_srt):
    diff = abs(num1 - num2)
    diff_lst.append(diff)
### Part 1 of the puzzle
print(sum(diff_lst))
##### Part 2 
##### Use the sorted list to find the number of occurences on other one and create similarity score list
for num1 in l1_srt:
    occ = l2_srt.count(num1)
    sim_score.append((occ*num1))
#print(sim_score)
print('Similarity Score')
print(sum(sim_score))
