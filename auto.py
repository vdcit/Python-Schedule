import schedule
import time
import subprocess
import sys
import datetime

"""Thay doi cau lenh va duong dan o day"""
command = '/home/cherry/Documents/test.sh'
directory = '/home/cherry/Documents'

"""Ham chay lenh"""
def job():
    today = datetime.datetime.now()
    """sstrftime("%Y-%m-%d %H:%M")"""
    subprocess.Popen(['/bin/bash', '-c','%s >> %s/"%s"-kq.txt'% (command, directory, today.strftime("%d%m%Y-%H%M%S"))])

"""Thu thi chuong trinh 15 giay mot lan"""
print 'Thu thi chuong trinh 15 giay mot lan'
print 'An to hop CTL + C de thoat'
schedule.every(15).seconds.do(job)

"""Sau moi tieng chay ham job mot lan"""
# print 'Thu thi chuong trinh 1 lan / 1 gio'
# schedule.every().hour.do(job)

"""Thuc thi chuong trinh vao luc 10h30 phut hang ngay"""
# print 'Thuc thi chuong trinh vao luc 10h30 phut hang ngay'
# schedule.every().day.at("10:30").do(job)

"""Thu thi chuong trinh vao thu 2 hang tuan"""
# print 'Thu thi chuong trinh vao thu 2 hang tuan'
# schedule.every().monday.do(job)

"""Thu thi chuong trinh vao thu 3 hang tuan, luc 13h15phut"""
# print 'Thu thi chuong trinh vao thu 3 hang tuan, luc 13h15phut'
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

