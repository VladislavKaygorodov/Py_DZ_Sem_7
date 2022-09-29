import model as mod
import temporary_files as tp

def choice_function(take):
    if take == '+':
        mod.input_contact(tp.name, tp.surname, tp.first_number)
        repeat =  input('Желаете добавить дополнительные данные? ("1" да, "2" нет): ' )
        if repeat == "1":
            mod.additional_items_for_contact(tp.second_number, tp.other)
        else:
            mod.add_empty_items_for_contact(tp.second_number, tp.other)

        mod.save_contact(tp.name, tp.surname, tp.first_number, tp.second_number, tp.other)
        print("Данные о контакте занесены в файл 'Numbers.txt' ")

    elif take == '++':
        mod.print_numbers("Numbers.txt")
        choice = input("Введите id контакта: ")
        print("Данные занесены в файл 'Contact.txt'")
        mod.add_choice_contact(choice, "Numbers.txt")

