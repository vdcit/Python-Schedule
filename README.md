Sử Dụng Python để tự động chạy tác vụ trên linux
================================================

#I. Giới thiệu#
  Thư viện schedule của python có thể giúp ta dẽ dàng chạy một tác vụ nào đó hằng ngày hoặc vào bất kỳ một thời gian cụ thể nào . Nó sử dụng đơn giản hơn crontab của linux .

#II. Chuẩn bị #
### Để cài đặt schedule ta cần cài nhưng gói sau ###
  1. Cài đặt`python-pip` <br>
    - trên ubuntu, debian : `sudo apt-get install python-pip` <br>
    - trên Fedora, redhat, centos : `sudo yum install python-pip` <br>
  2. Cài đặt module `schedule` <br>
    - `sudo pip install schedule` <br>

#III. Bắt đầu sử dụng
  ```
  git clone https://github.com/vdcit/Python-Schedule/ <br> 
  cd Python-Schedule <br>
  python auto.py <br> ```



 
