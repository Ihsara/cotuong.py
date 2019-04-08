# cotuong.py - Thư viện dành cho cờ tướng

[![Build Status](https://travis-ci.org/Ihsara/cotuong.py.svg?branch=master)](https://travis-ci.org/Ihsara/cotuong.py)

Đây là một thư viện cho cờ tướng nhằm đơn giản và thúc đẩy khi dùng python để tương tác với cờ tướng

# Cài đặt
cotuong.py dùng python 3.7.x và [pipenv](https://github.com/pypa/pipenv) để thiết đặt môi trường 

```sh
cd cotuong.py 
pipenv install
pipenv shell
py.test tests/
```

# Sử dụng

## Tạo ván cờ mới

```python
from cotuong import GameState

chesspiece_pos = {'A': [104, 106], 'C': [82, 88], 'E': [103, 107], 'G': [105], 'H': [102, 108], 'P': [71, 73, 75, 77, 79], 'R': [101, 109], 'a': [14, 16], 'c': [32, 38], 'e': [13, 17], 'g': [15], 'h': [12, 18], 'p': [41, 43, 45, 47, 49], 'r': [11, 19]}

FEN_starting_pos = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR w 1"

new_game = GameState() #Ván mới hoàn toàn. Quân cờ ở vị trí khai cuộc mở màn
new_game_2 = GameState(load= FEN_starting_pos) #Khởi tạo ván cờ từ dãy FEN. TBD
new_game_3 = GameState(load=chesspiece_pos) #Khởi tạo ván cờ từ từ điển. TBD
```

## Kiểm tra nước cờ hợp lệ hay không

```python 
from verify import Advisor #Quân cờ nào cần kiểm tra 
``` 

# Cần phải làm 

- [ ] Kiểm nước cờ hợp lệ
- [ ] Tạo ván cờ từ FEN 
- [ ] Tạo ván cờ từ điển
- [ ] Phỏng đoán thế cờ
- [ ] Đánh giá thế cờ hiện tại
- [ ] Cập nhật jupyter-notebook cho cách sử dụng
- [ ] Đọc nguyên ván cờ từ file json
- [ ] Đánh giá hiệu năng khi xử lý số lượng lớn
- [ ] Tìm hiểu thêm tính năng cần thiết khác


