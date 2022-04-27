def sum_self_made(list_of_numbers):

    if (isinstance(list_of_numbers, tuple)
            or isinstance(list_of_numbers, list)):
        sum = 0
        for i in list_of_numbers:
            sum += i

        return sum