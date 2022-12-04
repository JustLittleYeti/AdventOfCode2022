from string import ascii_uppercase
from string import ascii_lowercase


def read_input(input):
    with open(input, "r") as file:
        all_rucksacks=[]
        for line in file.readlines():
            line=line.strip()
            rucksack=[]
            items=len(line)
            middle=items//2
            CompartmentA=line[:(middle)]
            CompartmentB=line[(middle):]
            rucksack.append(CompartmentA)
            rucksack.append(CompartmentB)
            all_rucksacks.append(rucksack)
    return all_rucksacks


def sort(line):
    better_table1 = []
    better_table2 = []
    for i in line:
        if i.islower():
            better_table1.append(i)
        elif i.isupper():
            better_table2.append(i)
        else:
            print("something is wrong", i)
    proper_table= better_table1 + better_table2
    return proper_table


def find_duplicated(tab):
    lower=dict(zip(ascii_lowercase, range(1,27)))
    upper=dict(zip(ascii_uppercase, range(27,53)))
    sum=0
    for obj in tab:
        for i in obj[0]:
            if i in obj[1]:
                if i.islower():
                    sum+=lower[i]
                else:
                    sum+=upper[i]
                break
    return sum


def look_for_badges(tab):
    badges=[]
    tab=merge_backpacks(tab)
    for i in range (0, len(tab),3):
        for element in tab[i]:
            if element in tab[i+1] and element in tab[i+2]:
                badges.append(element)
                break
    return badges


def count_badges(tab):
    lower = dict(zip(ascii_lowercase, range(1, 27)))
    upper = dict(zip(ascii_uppercase, range(27, 53)))
    sum = 0
    for obj in tab:
        if obj.islower():
            sum += lower[obj]
        else:
            sum += upper[obj]
    return sum


def merge_backpacks(tab):
    merged=[]
    for element in tab:
        merged.append(element[0]+element[1])
    return merged


all_rucksacks=read_input("input.txt")
print("Score is: ",find_duplicated(all_rucksacks))
badges=look_for_badges(all_rucksacks)
print ("Sum of badges: ", count_badges(badges))