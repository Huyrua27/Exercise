def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    
    for i in range(size):
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4*size-3, '-'))
    
    print('\n'.join(lines[::-1] + lines[1:]))

# Nhập kích thước từ bàn phím
n = int(input("Nhập kích thước rangoli: "))
print_rangoli(n)