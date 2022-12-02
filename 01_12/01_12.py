def read_input(input):
    with open(input, "r") as file:
        calories_per_elf = {}
        elfID = 1
        for line in file.readlines():
            if line != "\n":
                try:
                    calories_per_elf[elfID].append(int(line))
                except:
                    calories_per_elf[elfID] = []
                    calories_per_elf[elfID].append(int(line))
            else:
                elfID += 1
    return calories_per_elf

def find_biggest_calories(calories_per_elf):
    current_most_caloric = [0, 0]
    for i, j in calories_per_elf.items():
        total_calories = 0
        for calories in j:
            total_calories += calories
        if total_calories > current_most_caloric[1]:
            current_most_caloric = [i, total_calories]

    return current_most_caloric

def find_three_biggest_calories(calories_per_elf):
    calorie_track = []
    for elf, cal_per_elf in calories_per_elf.items():
        total_calories = 0
        for calories in cal_per_elf:
            total_calories += calories
        calorie_track.append((total_calories))
    calorie_track.sort(reverse=True)
    print(calorie_track)
    return calorie_track

def sum_of_three(current_most_caloric):
    sum=current_most_caloric[0]+current_most_caloric[1]+current_most_caloric[2]
    return sum

biggest_calories=find_biggest_calories(read_input("input.txt"))
print (biggest_calories)
three_biggest_calories=find_three_biggest_calories(read_input("input.txt"))
print (three_biggest_calories)
sum=sum_of_three(three_biggest_calories)
print(sum)
