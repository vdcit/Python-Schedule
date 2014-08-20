import schedule
import time
import subprocess
import sys
import datetime

"""Thay doi cau lenh va duong dan o day"""
command = raw_input('Nhap vao cau lenh hoac file shell can chay ')
directory = raw_input('Nhap vao duong dan luu file log ')
data = {2: 'monday',
        3: 'tuesday',
        4: 'wednesday',
        5: 'thursday',
        6: 'friday',
        7: 'saturday',
        8: 'subday'}


def job():
    today = datetime.datetime.now()
    """sstrftime("%Y-%m-%d %H:%M")"""
    subprocess.Popen(['/bin/bash', '-c', '%s >> %s/"%s"-kq.txt' % (command, directory, today.strftime("%d%m%Y-%H%M%S"))])


def nhapthoigian():
    while True:
        gio = int(raw_input('Nhap vao gio: '))
        if 24 < gio:
            print 'Nhap sai so gio : '
            pass
        phut = int(raw_input('Nhap vao phut: '))
        if phut > 59:
            print 'Nhap sai so phut: '
            pass
        else:
            break
    return (gio, phut)

while True:
    print '============================   Menu    ================================'
    print ' 1. Thoi gian lap lai chuong trinh tinh bang ngay :'
    print ' 2. Thoi gian lap lai chuong trinh tinh bang ngay co dinh hang tuan (monday, sunday ....)'
    print ' 3. Thoi gian lap lai chuong trinh tinh bang gio'
    print ' 4. Thoi gian lap lai chuong trinh tinh bang phut'
    print ' 5. Thoi gian lap lai chuong trinh tinh bang giay'

    choose = raw_input('Hay chon theo nhu cau cua ban: ')
    if choose == '1':
        print 'Ban chon lap lai chuong trinh hang ngay'
        choose1 = raw_input('Ban co muon chon thoi diem de chay truong trinh khong? y/n :')
        if choose1 == 'y' or choose1 == 'yes':
            gio, phut = nhapthoigian()
            print 'chuong trinh se duoc thuc thi vao luc %s:%s hang ngay !' % (gio, phut)
            schedule.every().days.at("%s:%s" % (gio, phut)).do(job)
            break
        elif choose1 == 'n' or choose1 == 'no':
            print 'Chuong trinh se thuc thi vao luc 00:00 hang ngay'
            schedule.every().days.do(job)
            break
        else:
            print 'Chon sai lua chon y/n:'
            pass

    elif choose == '2':
        print '2. Thu hai - Monday'
        print '3. Thu ba - Tuesday'
        print '4. Thu tu - Wednesday'
        print '5. Thu nam - Thursday'
        print '6. Thu sau - Friday'
        print '7. Thu bay - Saturday'
        print '8. Chu nhat - Sunday'
        choose2 = int(raw_input('Nhap vao ngay ban muon thuc thi truong trinh : '))

        if choose2 == 2:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 2 luc %s:%s' % (gio1, phut1)
            schedule.every().monday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 3:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 3 luc %s:%s' % (gio1, phut1)
            schedule.every().tuesday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 4:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 4 luc %s:%s' % (gio1, phut1)
            schedule.every().wednesday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 5:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 5 luc %s:%s' % (gio1, phut1)
            schedule.every().thursday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 6:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 6 luc %s:%s' % (gio1, phut1)
            schedule.every().friday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 7:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi thu 7 luc %s:%s' % (gio1, phut1)
            schedule.every().saturday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        elif choose2 == 8:
            gio1, phut1 = nhapthoigian()
            print 'Ban chon Thuc thi chuong trinh vao moi chu nhat luc %s:%s' % (gio1, phut1)
            schedule.every().sunday.at("%s:%s" % (gio1, phut1)).do(job)
            break
        else:
            print 'Nhap sai lua chon'
            pass

    elif choose == '3':
        s1 = int(raw_input('Nhap vao so gio muon thuc thi lai: '))
        print 'Chuong trinh se duoc thuc thi %s gio mot lan !' % s1
        schedule.every(s1).hours.do(job)
        break
    elif choose == '4':
        m2 = int(raw_input('Nhap vao so giay muon thuc thi lai: '))
        print 'Chuong trinh se duoc thuc thi %s phut mot lan !' % s1
        schedule.every(m2).minutes.do(job)
        break
    elif choose == '5':
        s1 = int(raw_input('Nhap vao so giay muon thuc thi lai: '))
        print 'Chuong trinh se duoc thuc thi %s giay mot lan !' % s1
        schedule.every(s1).seconds.do(job)
        break
    else:
        print 'Nhap sai lua chon . chon lai !'
        pass

"""Thu thi chuong trinh 15 giay mot lan"""
#print 'Thu thi chuong trinh 15 giay mot lan'
#print 'An to hop CTL + C de thoat'
# schedule.every(15).seconds.do(job)

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

