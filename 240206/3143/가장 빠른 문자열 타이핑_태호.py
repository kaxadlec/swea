T = int(input())
for test_case in range(T):
    A, B = input().split()

    len_a = len(A)  # a의 길이
    len_b = len(B)  # b의 길이
    b_num_in_a = A.count(B)  # b가 a안에 몇개 들어잇나 확인

    answer = len_a - len_b * b_num_in_a + b_num_in_a  # a의 길이 - b의개수*b의 길이 + b의 개수

    print(f'#{test_case + 1} {answer}')