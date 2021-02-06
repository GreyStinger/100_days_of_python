pre_format_name = str(input("Please input your first and last name: ")).split(" ")

first_division = pre_format_name[0]
second_division = pre_format_name[1]


def format_name(f_name, l_name):
    f_name_formatted = f_name.title()
    l_name_formatted = l_name.title()
    # control = 0
    # for letter in f_name:
    #     if control > 0:
    #         f_name_formatted += letter.lower()
    #     else:
    #         f_name_formatted += letter.upper()
    #         control = 1
    # for letter in l_name:
    #     if control < 1:
    #         l_name_formatted += letter.lower()
    #     else:
    #         l_name_formatted += letter.upper()
    #         control = 0
    return str(f"{f_name_formatted} {l_name_formatted}")


print(format_name(f_name=first_division, l_name=second_division))
