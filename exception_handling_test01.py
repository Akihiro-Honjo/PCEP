def add_10(value):
    """
    以下の2つの値を返す関数を実装してください。
    1. 引数 value に10を加算した値
    2. 成功・失敗に応じたメッセージ


    加算処理に成功したら、加算した値と '成功しました' という文字列を返す。
    例外が発生したら、0 と '失敗しました' という文字列を返す。
    """
    try:
        result = value + 10
        return result, "成功しました"
    except TypeError:
        return 0, "失敗しました"


# 成功パターン
result1 = add_10(10)
print(result1)  # (20, "成功しました")

# 失敗パターン
result2 = add_10("10")
print(result2)  # (0, "失敗しました")