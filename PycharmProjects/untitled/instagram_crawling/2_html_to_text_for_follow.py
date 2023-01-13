from bs4 import BeautifulSoup as bs
import os
import configparser as parser
import shutil
from openpyxl import Workbook

properties = parser.ConfigParser()

path = os.getcwd()
properties.read(path + '/config.ini')
image_del = properties['ETC']['image_del']
date = properties['ETC']['date']

if image_del == 'Y':
    for e in os.listdir(path):
        if '_files' in e:
            print(f'{path}/{e}')
            shutil.rmtree(f'{path}/{e}')

file_list = [f'{date}_followers.html', f'{date}_following.html']
Res = [[], []]
idx = 0
for file_name in file_list:
    # file_name_aft = file_name.split('.')[0] + '.txt'
    # fw = open(file_name_aft, 'w', encoding='utf-8')
    page = open(f'{path}/{file_name}', 'r', encoding='utf-8').read()
    # page = open('folloing.txt','r',encoding='utf-8').read()
    # page = open('follwer.txt','r',encoding='utf-8').read()
    soup = bs(page, "html.parser")
    elements = soup.select('div._aano > div > div > div > div > div > div > div')
    print(len(elements))
    for i in elements:
        Res[idx].append(i.text.replace("·팔로우", "").replace("인증됨", ""))
        # fw.write(f'{i.text.replace("·팔로우", "").replace("인증됨", "")}\n')
        # print(idx, i.text.replace("·팔로우", "").replace("인증됨", ""))
    idx += 1

Res.append(list(set(Res[0]) - set(Res[1])))
Res.append(list(set(Res[1]) - set(Res[0])))

write_wb = Workbook()
write_ws = write_wb.active
write_ws['B1'] = f'팔로워  {len(Res[0])}'
write_ws['C1'] = f'팔로잉  {len(Res[1])}'
write_ws['D1'] = f'내가 팔로우 안함  {len(Res[2])}'
write_ws['E1'] = f'상대가 팔로우 안함  {len(Res[3])}'
write_ws.column_dimensions['B'].width = 24
write_ws.column_dimensions['C'].width = 24
write_ws.column_dimensions['D'].width = 24
write_ws.column_dimensions['E'].width = 24
for i in range(4):
    for j in range(len(Res[i])):
        write_ws.cell(j + 2, i+2, Res[i][j])

write_wb.save(f'{path}/{date}.xlsx')