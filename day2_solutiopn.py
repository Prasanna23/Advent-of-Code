with open('day2_inp.txt') as f:
    lines = f.readlines()
    f.close()
unsafe_count_pt1 = 0
unsafe_count_pt2 = 0
for index,line in enumerate(lines):
    line = line.split()
    line = [int(i.strip()) for i in line]
    ## Identify trend
    if line[0] > line[1]:
        trend = 'D'
    else:
        trend = 'I'
    #print(trend)
    level_safe = 'Y'
    skip_lvl = 0
    for j in range(1,len(line)):
        diff = line[j] - line[j - 1]
        if (trend == 'D' and (diff >= 0 or diff < -3)) or (trend == 'I' and (diff <= 0 or diff > 3)):
           #print('Level #', index + 1 ,'is unsafe')
           level_safe  = 'N'
           #unsafe_count_pt1 = unsafe_count_pt1  + 1
           if skip_lvl == 0:
                if j < len(line) - 1:
                    diff1 = line[ j + 1] - line[j - 1]
                    if (trend == 'D' and (-3 <= diff1 < 0)) or (trend == 'I' and (0 <= diff1 < 3)):
                        skip_lvl = skip_lvl + 1 
                        level_safe  = 'Y'
                        j = j + 1                
                    else:
                        unsafe_count_pt2 = unsafe_count_pt2  + 1  
                        print(line)
                        break     
    
    
#### Part 1    
print('total levels',len(lines))
print('safe levels',len(lines) - unsafe_count_pt1)        
print('unsafe levels',unsafe_count_pt1)
print('total levels',len(lines))
print('safe levels',len(lines) - unsafe_count_pt2)        
print('unsafe levels',unsafe_count_pt2)        
