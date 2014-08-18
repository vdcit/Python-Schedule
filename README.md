Sử Dụng Python để tự động chạy tác vụ trên linux
================================================

# I. Giới thiệu#
  Thư viện schedule của python có thể giúp ta dẽ dàng chạy một tác vụ nào đó hằng ngày hoặc vào bất kỳ một thời gian cụ thể nào . Nó sử dụng đơn giản hơn crontab của linux .

# II. Chuẩn bị #
## Script được viết cho python 2.6.x trở lên nhưng không dùng cho python 3.x.x ##
### Để cài đặt schedule ta cần cài nhưng gói sau ###
  1. Cài đặt`python-pip` <br>
    - trên ubuntu, debian : `sudo apt-get install python-pip` <br>
    - trên Fedora, redhat, centos : `sudo yum install python-pip` <br>
  2. Cài đặt module `schedule` <br>
    - `sudo pip install schedule` <br>

# III. Bắt đầu sử dụng
  ```
  git clone https://github.com/vdcit/Python-Schedule/
  cd Python-Schedule 
  ```
<br>  
### Sửa file auto.py theo ý muốn  ###
 - gán biến `command` = câu lệnh ta cần chạy ,
 
 - gán biến `directory` bằng đường dẫn ta muốn lưư file log.

 - Câu lệnh `schedule.every(15).seconds.do(job)` tức là mỗi 15 giây chạy hàm `job` 1 lần . ta có thể thay `second` bằng `minute` , `hour` , `day` hoặc bất kỳ ngày ào đó trong tuần ví dụ như `monday` hoặc `sunday`
 - Ta có thể chỉ định chính xác lúc ngày giờ nào nó sẽ chạy hàm `job` bằng câu lệnh 
```
schedule.every().wednesday.at("13:15").do(job)
```
thay `wednesday` bằng ngày và `13.15` bằng thời gian cần chạy
 - file log sẽ có dạng `năm-tháng-ngày giờ-phút-giây.txt`<br>

**sửa file xong rồi bắt đầu chạy thôi :**<br>

- Trong file auto.py sử dụng mặc định lệnh `schedule.every(15).seconds.do(job)`, các lệnh khác đã được comment, nếu bạn muốn sử dụng thì un-comment theo từng thời gian mong muốn.

```
  python auto.py
```
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
**để ngừng chạy ta dùng `Ctrl + C`**

