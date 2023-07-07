import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  pattern_phone = r'(\+7|8|7)?\s?\(?(\d{3,4})\)?(\s|[- ])?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s?\(?(доб. )?(\d{4})?'
  util = r'\s\s?$'
  new_contacts_list = []
  for inf in contacts_list[1:]:
    fio = ' '.join([inf[0],inf[1],inf[2]])
    fio = fio.split()
    loc_w = inf[3]
    position = inf[4]
    phone = inf[5]
    email = inf[6]
    if phone != '':
      repl = r'+7(\g<2>)\g<4>-\g<5>-\g<6> доб.\g<8>'
      phone = re.sub(pattern_phone, repl, phone)
    else:
      phone = ''
    inf = [fio, loc_w, position, phone, email]
    new_contacts_list.append(inf)
  new_contacts_list = sorted(new_contacts_list)
  for ind in range(1, len(new_contacts_list)-2):
    if new_contacts_list[ind][0][0] == new_contacts_list[ind-1][0][0]:
      if len(new_contacts_list[ind][0]) == 2:
            new_contacts_list[ind][0] = new_contacts_list[ind-1][0]
      for index in range(0, len(new_contacts_list[ind])):
        if new_contacts_list[ind][index] == '':
          new_contacts_list[ind][index] = new_contacts_list[ind-1][index]
      new_contacts_list.pop(ind-1)
with open("phonebook.csv", "w", encoding='utf-8') as f1:
  datawriter = csv.writer(f1, delimiter=',')
  datawriter.writerows(new_contacts_list)
