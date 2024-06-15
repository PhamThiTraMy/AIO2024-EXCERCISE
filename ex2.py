def count_letters(word):
    letter_count = {}  # Khởi tạo dictionary để lưu số lần xuất hiện của từng chữ cái
    
    # Duyệt qua từng ký tự trong từ
    for char in word:
        # Kiểm tra nếu ký tự là chữ cái
        if char.isalpha():
            # Nếu ký tự đã có trong dictionary, tăng giá trị lên 1
            if char in letter_count:
                letter_count[char] += 1
            # Nếu ký tự chưa có trong dictionary, thêm mới với giá trị là 1
            else:
                letter_count[char] = 1
    
    return letter_count

# Ví dụ sử dụng hàm count_letters
word = "Happiness"
result = count_letters(word)
print("Dictionary đếm số lượng chữ cái trong từ '{}':".format(word))
print(result)