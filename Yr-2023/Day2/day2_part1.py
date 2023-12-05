game_sum = 0
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
    part2 = 0
    impossible = False
    for games in Game_cubes:
        
        g1=(games.split(','))
        for g in g1:
            cnt, color = g.split()
            match color:
                case 'blue':
                    cnt_b = int(cnt)
                case 'green':
                    cnt_g = int(cnt)
                case 'red':
                    cnt_r = int(cnt)
        ##### part1 impossible plays calculation.
            if cnt_b > 14:
                impossible = True
                break
            if cnt_g > 13:
                impossible = True
                break
            if cnt_r > 12:
                impossible = True
                break
    #print("{} , {}, {}".format(max_b,max_g,max_r))
    if impossible == False :
        game_sum = game_sum + int(Game_id)
        #print(Game_id)

print(game_sum)