from collections import deque

def max_sliding_window(num_list, k):
    # Kiểm tra input hợp lệ
    if not num_list or k <= 0:
        return []
    
    # Khởi tạo deque để lưu index của các phần tử trong cửa sổ
    deque_window = deque()
    result = []
    
    # Duyệt qua từng phần tử trong num_list
    for i in range(len(num_list)):
        # Loại bỏ phần tử ra khỏi cửa sổ nếu nó không còn nằm trong cửa sổ
        if deque_window and deque_window[0] < i - k + 1:
            deque_window.popleft()
        
        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại vì chúng không thể là số lớn nhất trong cửa sổ
        while deque_window and num_list[deque_window[-1]] < num_list[i]:
            deque_window.pop()
        
        # Thêm index của phần tử hiện tại vào deque
        deque_window.append(i)
        
        # Bắt đầu lấy kết quả sau khi đủ k phần tử trong cửa sổ
        if i >= k - 1:
            result.append(num_list[deque_window[0]])
    
    return result

# Ví dụ sử dụng hàm max_sliding_window
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
print("Số lớn nhất trong từng sliding window có kích thước", k, ":")
print(max_sliding_window(num_list, k))