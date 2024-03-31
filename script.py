import re
def number_one():
    list_number = [] 
    with open('C:/Users/user/Desktop/Projects/Samples/File_operations/numbers_1.txt', 'r') as file: 
        print('Содержимое файла numbers.txt') 
        for i_line in file: 
            i_line = i_line.strip() 
            q = sum([int(i_line) for i_line in str.split(i_line) if i_line.isdigit()])
            list_number.append(q)
            filtered_words = list(filter(None, list_number))

    print(filtered_words)
    print('Сумма:',q)

def number_two():
    list_number = [] 
    with open('C:/Users/user/Desktop/Projects/Samples/File_operations/numbers_2.txt', 'r') as file: 
        print('Содержимое файла numbers.txt') 
        for i_line in file: 
            i_line = i_line.strip()
            num = [int(i_line) for i_line in str.split(i_line) if i_line.lstrip("-").isdigit()]
            list_number.append(num)
            filtered_words = list(filter(None, list_number))

    print(filtered_words)
    print('Сумма:',sum(num))

list_number = [] 
with open('C:/Users/user/Desktop/Projects/Samples/File_operations/numbers_3.txt', 'r') as file:
    string = file.read()
    regex = "\d+"
    gr = re.findall(regex, string)
    print(gr)
    # print('Содержимое файла numbers.txt')
    # i = [] 
    # for i_line in file: 
    #     i_line = i_line.strip()
    #     i_lines = i_line.strip()
    #     i_l = i_lines.strip()
    #     i.append(i_l)
    #     num = [int(i_line) for i_line in str.split(i_line) if i_line.lstrip("-").isdigit()]
    #     list_number.append(num)
    #     filtered_words = list(filter(None, list_number))
    #     print(list_number)
