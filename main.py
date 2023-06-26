from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pattern1 = r'([^\s]+)'
    pattern2 = r'\s([^\s]+)'
    pattern3 = r'\w{2,10}(вич|вна)'
    pattern_phone = r'(\+7|8|7)?\s?\(?(\d{3,4})\)?(\s|[- ])?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s?\(?(доб. )?(\d{4})?'
    future_str = {}
    control = []
    res = []
    for i in contacts_list[1:]:
        info = " ".join(i)
        lastname = re.search(pattern1, info).group(0)
        firstname = re.search(pattern2, info).group(0)
        if i[2] != '':
            surname = re.search(pattern3, info).group(0)
        else:
            surname = ''
        if i[5] != '':
            repl = r'+7(\g<2>)\g<4>-\g<5>-\g<6> доб.\g<8>'
            phone = re.sub(pattern_phone, repl, i[5])
        else:
            phone = ''
        future_str['lastname'] = lastname
        future_str['firstname'] = firstname
        future_str['surname'] = surname
        future_str['organization'] = i[3]
        future_str['position'] = i[4]
        future_str['phone'] = phone
        future_str['email'] = i[6]
        control.append(future_str)  # исправить проблему того, что записывается только последняя итерация. КАК???
    control1 = control.copy()
    for i in range(1, len(control)):
        if control[i - 1]['lastname'] == control[i]['lastname']:
            for key, value in control[i].items():
                control[i][key] = value if value else control[i - 1][key]
            control1.remove(control[i - 1])
    for cont in control1:
        res.append(
            f'{cont["lastname"]}, {cont["firstname"]}, {cont["surname"]}, {cont["organization"]}, {cont["position"]}, {cont["phone"]}, {cont["email"]}')
with open("phonebook.csv", "w", encoding='utf-8') as f1:
    datawriter = csv.writer(f1, delimiter=',')
    datawriter.writerows(res)
