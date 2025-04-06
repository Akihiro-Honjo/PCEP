###例外処理
#1.構文エラー 文法上誤りがある
#2.実行時エラー エラーがあるとプログラムが強制終了する
#3.論理エラー プログラムは実行されるが、意図した結果にならない

##例外処理は最終手段として使用する。if文などできるだけ回避する


try:
    num = int(input("数値を入力してください:\n"))
    result =  10 / num
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError as e:
    print(f"0で割ることはできません{e}")
except KeyboardInterrupt:
    print("処理を中断しました。")
else:
    print(result)
finally:
    print("終了します")
    

