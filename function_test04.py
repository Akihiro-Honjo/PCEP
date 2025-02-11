
def double_an_odd_number(int_list):
    """
    与えられた整数のリストの要素のうち、奇数だけを2倍にして、その合計を返す関数を作成してください。
    偶数は合計に含めません。
    """
    total = 0
    for num in int_list:
        if num % 2 != 0:  # 奇数かどうかを判定
            total += num * 2
    return total
int_list = list(range(1,10))
result = double_an_odd_number(int_list)
print(result)