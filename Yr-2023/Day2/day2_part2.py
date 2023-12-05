###### Solution for day 2 pt 2 puzzle
part2_sum = 0
input = open('/Users/gayathriviswanathan/Documents/Input/day2/input.txt', 'r')
lines = input.readlines()
for line in lines:
#string = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
# Use the split() method to split the string into 
    A = line.split(':')
    Game_id = A[0].split('Game ')[1]
    #print(Game_id)
    Game_cubes = A[1].split(';')
    cnt_b = 0
    cnt_r = 0
    cnt_g = 0
    max_b = 0
    max_g = 0
    max_r = 0
    part2 = 0
    impossible = False
    for games in Game_cubes:
        
        g1=(games.split(','))
        for g in g1:
            cnt, color = g.split()
            match color:
                case 'blue':
                    cnt_b = int(cnt)
                    if cnt_b > max_b:
                        max_b = cnt_b
                case 'green':
                    cnt_g = int(cnt)
                    if cnt_g > max_g:
                        max_g = cnt_g
                case 'red':
                    cnt_r = int(cnt)
                    if cnt_r > max_r:
                        max_r = cnt_r
    #print("{} , {}, {}".format(max_b,max_g,max_r))
    part2 = max_r * max_g * max_b
    #print(part2)
    part2_sum += part2
    print("{} :{}".format(Game_id,part2_sum))

print(part2_sum)


