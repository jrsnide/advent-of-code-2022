elf_calories = []
with open ("challenge_1_input", 'r') as calorie_input:
    calories = calorie_input.readlines()

    calorie_sum = 0
    for i in range(0, len(calories)):
        calorie_stripped = calories[i].strip()
        try:
            calorie_sum += int(calorie_stripped)
            if i == len(calories) - 1:
                elf_calories.append(calorie_sum)
        except ValueError as e:
            elf_calories.append(calorie_sum)
            calorie_sum = 0


elf_calories.sort(reverse=True)
print("The elf carrying the most calories: %d" % elf_calories[0])


top_elf_count = input("Please provide the top X elves for their sum of calories: (e.g. X = 3 for Top 3 elves): ")
sum_top_3_elves = 0
for i in range(int(top_elf_count)):
    sum_top_3_elves += elf_calories[i]

print("The sum of calories carried by the top %s elves: %d" % (top_elf_count, sum_top_3_elves))
