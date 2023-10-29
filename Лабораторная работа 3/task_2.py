# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=','):
    first_group = participants_first_group.split(separator)
    second_group = participants_second_group.split(separator)
    common_participants = sorted(list(set(first_group) & set(second_group)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(result)


# TODO Провеьте работу функции с разделителем отличным от запятой
