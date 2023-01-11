H, W, N = map(int, input().split())

input_data_dict = {}

# 「この行（列）にあるカードは何番目ですよ」という情報をためる
row_ordinal_dict = {}
column_ordinal_dict = {}

row_set = set()
column_set = set()

for i in range(N):
    A, B = map(int, input().split())

    input_data_dict[i + 1] = [A, B]
    row_set.add(A)
    column_set.add(B)

row_sorted_list = sorted(list(row_set))
column_sorted_list = sorted(list(column_set))

for i in range(len(row_sorted_list)):
    row_ordinal_dict[row_sorted_list[i]] = i + 1

for i in range(len(column_sorted_list)):
    column_ordinal_dict[column_sorted_list[i]] = i + 1

for i in range(1, N + 1):
    A = input_data_dict[i][0]
    B = input_data_dict[i][1]

    ans_A = row_ordinal_dict[A]
    ans_B = column_ordinal_dict[B]

    print(ans_A, ans_B)

# print(input_data_dict)
