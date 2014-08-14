import schedule
import time
import subprocess
import sys
import datetime

"""command = raw_input('Nhap vao cau lenh muon chay: ')
directory = raw_input('duong dan muon luu file log: ')"""

def job():
    today = datetime.datetime.now()
    """sstrftime("%Y-%m-%d %H:%M")"""

    """ Sua cau lenh va duong dan o day"""
    subprocess.Popen(['/bin/bash', '-c','/home/cherry/Documents/test.sh >> /home/cherry/Documents/"%s".txt'% today])

"""def job1():
    today = datetime.datetime.now()
    subprocess.Popen(['/bin/bash', '-c','%s >> %s/"%s".txt'% (command, directory, today)])"""

"""Sau 15 giay chay ham job mot lan"""
schedule.every(15).seconds.do(job)

"""Sau moi tieng chay ham job mot lan"""
schedule.every().hour.do(job)

"""Chay ham job hang ngay vao luc 10h30p"""
schedule.every().day.at("10:30").do(job)

"""Moi thu hai chay ham mot lan"""
schedule.every().monday.do(job)

"""chay ham job vao moi thu 3 luc 13h15p"""
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

