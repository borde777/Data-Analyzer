import csv
import re
from operator import itemgetter


def display(reader):
    test_num_input = raw_input("Please enter test number: ")
    with open(reader, 'rb') as f_reader:
        csv_read = csv.reader(f_reader)
        final_number_list=[]
        final_alpha_list=[]
        final_alpha_list.append(['test_number','result','Count'])
        final_number_list.append(['test_number','result','Count'])

        for row in csv_read:
            if row[0] == str(test_num_input):
                numbers_list = []
                alpha_list = []
                for j in row:
                    match = re.match(r"^-?[0-9]\d*(\.\d+)?$", str(j), re.I)
                    if match:
                        numbers_list.append(float(j))
                    else:
                        alpha_list.append(row[0])
                        alpha_list.append(row[1])
                        alpha_list.append(row[2])

                if len(alpha_list) == 3:
                    final_alpha_list.append(alpha_list)


                if len(numbers_list) < 3:
                    pass
                else:
                    final_number_list.append(numbers_list)

        choice = input("please choose one option:\n 1. Number \n 2. Alpha:\n ")

        if choice == 1:
            add=0
            tem_lst=[]
            test=0
            res=0
            # result_check_list=[]
            # for i in final_number_list:
            #     if str(i[1]) not in result_check_list:
            #         result_check_list.append(i[1])
            # result_check_list.remove('result')
            for i in final_number_list:
                # for j in result_check_list:
                if str(i[1]) == "444.0":
                    print str(i)
                    add += float(i[2])
                    test = float(i[0])
                    res = float(i[1])
                    final_number_list.remove(i)
            tem_lst.append(test)
            tem_lst.append(res)
            tem_lst.append(add)
            final_number_list.append(tem_lst)
            display_list = sorted(final_number_list, key=itemgetter(2), reverse=True)

            for disp in display_list:
                print disp
        elif choice ==2:
            for i in final_alpha_list:
                print str(i)

        else:
            print ("Wrong Input")


display("C:\Users\Eliezer\Desktop\office\Result_Values_result_cnt_1476122692574.csv")