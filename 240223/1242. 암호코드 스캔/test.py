hex_num = "1DB176C588D26EC"

dec_num = int(hex_num, 16)
print(dec_num)  # 10진수 출력

bin_num = bin(dec_num)[2:]
print(bin_num)  # 2진수 출력

while 1:
    if bin_num[-1] == '0':
        bin_num = bin_num[0:-1]
    else:
        break

print(bin_num)

print(len(bin_num) // 56)
print(57 // 56)

if len(bin_num) % 56 != 0:
    pre_str = '0' * (((len(bin_num) // 56)+1) * 56 - len(bin_num))
    new_bin_num = pre_str + bin_num

print(new_bin_num)