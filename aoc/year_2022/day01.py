def part1(calories):
    """
    Big O: O(n) / Time complexity: O(n)
    :param calories: A list of the Elf calories
    :return: Returns the highest Elf's calories
    """
    if not calories:
        return None

    return get_summend_calories_of_each_elf(calories)[0]


def part2(calories):
    """
    Big O: O(n) / Time complexity: O(n)
    :param calories: A list of the Elf calories
    :return: Returns the sum of the top three highest Elf calories
    """
    if not calories:
        return None

    return sum(get_summend_calories_of_each_elf(calories)[:3])


def get_summend_calories_of_each_elf(calories):
    summed_calorie_list = []
    sum = 0
    for index, calorie in enumerate(calories):
        if calorie:
            sum += int(calorie)

        if not calorie or index == len(calories) - 1:
            summed_calorie_list.append(sum)
            sum = 0

    summed_calorie_list.sort(reverse=True)

    return summed_calorie_list
