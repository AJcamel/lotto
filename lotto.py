'''匯入套件(模組)'''
import random, math

# 放置第一選號區 6 個號碼的變數
set_01 = set()

# 放置第二選號區的 1 個號碼的變數
num_02 = None

# 取得 1 ~ x 之間的值
def get_random_num(x):
    return math.floor(random.random() * x) + 1

# 暴力法
while True:
    # 先取得第一選號區的六個號碼
    num_01 = random.randint(1, 49)

    # 如果第一選號區不足六個號碼，同時號碼也不曾在第一選號區出現過，則加入 set
    if len(set_01) < 6:
        set_01.add(num_01)
    else:
        # 為第二選號區加入一個號碼
        num_02 = random.randint(1, 8)

        # 離開 while 迴圈
        break

print("第一選號區: ", sorted(set_01, reverse=False))
print("第二選號區: ", num_02)

