def minion_game(string):
    vowels = 'AEIOU'
    minh_score = 0
    an_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            minh_score += length - i
        else:
            an_score += length - i

    if minh_score > an_score:
        print("Minh", minh_score)
    elif an_score > minh_score:
        print("An", an_score)
    else:
        print("Draw")

# Nhập chuỗi từ bàn phím
s = input().strip()

# Gọi hàm minion_game với chuỗi đã nhập
minion_game(s)
