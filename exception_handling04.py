def sum_numbers(num_list):
    try:
        return sum(num_list)
    except TypeError as e:
        #例外の連鎖
        raise ValueError("リストに数値以外の要素が含まれています") from e
    
nums = [1, 2, 'three']
try:
    print(sum_numbers(nums))
except ValueError as e:
    print(e)
    print(e.__cause__) #__ cause属性を使って元の例外を取得
    
    
    
    def convert_to_int(s):
        try:
            return int(s)
        except ValueError as e:
            raise ValueError("整数に変換できない文字列が入力されました") from e

try:
    convert_to_int("Not a number")
except ValueError as e:
    print(e)
    print(e.__cause__)
    
#例外の詳細を隠蔽
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        raise ValueError("0で割ることはできません") from None
    return result
try:
    result = divide(5, 0)
except ValueError as e:
    print(e)
    print(e.__cause__)