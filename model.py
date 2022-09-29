def input_contact(name, surname, first_number):
    name.append(input(f'Введите имя контакта:'))
    surname.append(input(f'Введите фамилию контакта:'))
    first_number.append(input(f'Введите номер контакта:'))

def col_lines(name_file):
    lines= 0
    with open (name_file, 'r', encoding="utf-8") as file:
        for line in file:
            lines+=1
    return lines

def save_contact(name, surname, first_number, second_number, other):
    lines = col_lines("Numbers.txt")
    if lines == 0:
        id = str(col_lines("Numbers.txt")+1)
        with open ("Numbers.txt", "a", encoding="utf-8") as write:
                write.write(id + '\t')
                write.write(name[0] + '\t')
                write.write(surname[0] + '\t')
                write.write(first_number[0] + '\t')
                write.write(second_number[0] + '\t')
                write.write(other[0] + '\t')
    else:
        id = str(col_lines("Numbers.txt")+1)
        with open ("Numbers.txt", "a", encoding="utf-8") as write:
                write.write('\n' + id + '\t')
                write.write(name[0] + '\t')
                write.write(surname[0] + '\t')
                write.write(first_number[0] + '\t')
                write.write(second_number[0] + '\t')
                write.write(other[0] + '\t')

def additional_items_for_contact(second_number, other):
    key = set(input("Какие данные необходимо добавить?(дополнительный номер(1), примечания(2))"))
    output_set = set()
    output = ""
    for i in key:
        if i == "1":
            output_set.add("1")
        if i == "2":
            output_set.add("2")
    if len(output_set) == 2:
                second_number.append(input(f'Введите дополнительный номер контакта:'))
                other.append(input(f'Введите примечания к контакту:'))
    else:
        for i in output_set:
            if i == "1":
                second_number.append(input(f'Введите дополнительный номер контакта:'))
                other.append("Примечания отсутствуют")
            if i == "2":
                other.append(input(f'Введите примечания к контакту:'))
                second_number.append("Доп.номер отсутствует")

def add_empty_items_for_contact(second_number, other):
    second_number.append("Доп.номер отсутствует")
    other.append("Примечания отсутствуют")

def print_numbers(name_file):
    with open (name_file, 'r', encoding="utf-8") as file:
        for line in file:
            print(line)

def add_choice_contact(id, name_file):
    find_choice = []
    with open (name_file, 'r', encoding="utf-8") as file:
        for line in file:
            find_choice = line.split('\t')
            if find_choice[0] == id:
                with open ('Contact.txt', 'w', encoding="utf-8") as contact:
                    contact.write(f"id: {find_choice[0]}" + '\n')
                    contact.write(f"Имя: {find_choice[1]}" + '\n')
                    contact.write(f"Фамилия: {find_choice[2]}" + '\n')
                    contact.write(f"Основной номер телефона: {find_choice[3]}" + '\n')
                    contact.write(f"Дополнительный номер телефона: {find_choice[4]}" + '\n')
                    contact.write(f"Примечания: {find_choice[5]}")

