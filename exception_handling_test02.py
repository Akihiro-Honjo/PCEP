def division(x, y):
    """
    x ÷ y を計算して返す関数を実装してください。
    ただし、y が 0 の場合は 'ゼロで除算できません' という文字列を返すようにしてください。
    また、TypeError が発生した場合は '数値以外は計算できません' という文字列を返すようにしてください。
    """
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'ゼロで除算できません'
    except TypeError:
        return '数値以外は計算できません'