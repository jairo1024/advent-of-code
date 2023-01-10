def part1(calories):
    """
    Big O/Time complexity
    :param calories: A list of the Elf calories
    :return: Returns the highest Elf's calories
    """

    if not calories:
        return None

    highest_calories = 0
    sum = 0
    for index, calorie in enumerate(calories):
        if calorie:
            sum += int(calorie)

        if not calorie or index == len(calories)-1:
            if sum >= highest_calories:
                highest_calories = sum
            sum = 0

    return highest_calories
