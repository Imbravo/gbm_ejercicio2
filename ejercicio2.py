#Author: Jesús Ponte
# 12/09/2023

# Problema 2

def calc_points(race_list, score_system, k):
    dict = {}
    for race in race_list:
        for i, pilot in enumerate(race[:k]):
            #print(pilot)
            if str(pilot) in dict.keys():
                dict[str(pilot)] += score_system[i]
            else:
                dict[str(pilot)] = score_system[i]
            print(dict)
    max_val = [key for key, value in dict.items() if value == max(dict.values())]
    return max_val




with open('unit_test_1.txt')as f:

    while True:
        race_results = []
        g, p = map(int, f.readline().split(' ')) #First line contains G and P
        if g== 0 or p == 0:
            break

        # For loop which helps us get the lines that contain race results
        for i in range(g):
            race_results.append(list(map(int, f.readline().replace('\n', '').split(' '))))  #Second line contains

        #the next line after races is the number of lines containing point systems
        s = int(f.readline().replace('\n', '')) # scoring systems

        # For loop which helps us get the lines that are scoring systems
        for i in range(s):
            k, scoring_system = f.readline().replace('\n', '').split(' ', 1)
            scoring_system = list(map(int, scoring_system.split(' ')))
            k = int(k)
            # we call the function calc_points which prints the winner of the grand prix for each scoring system.

            file_name = 'unit_test_1_result'
            with open(file_name, 'a') as f2:
                f2.write(str(calc_points(race_results, scoring_system, k))+'\n')
