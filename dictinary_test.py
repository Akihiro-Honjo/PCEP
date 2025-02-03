# 1 で指定されたキーと値を持つ辞書を作成
my_dict =dict(name="John", age=25, job="Engineer")
print(my_dict)  # 指定された辞書を定義し、表示させる

# 2 'job' の値を取得
job = my_dict.get("job")
print(job)  # Engineer と表示させる

# 3 キーが'salary'、バリューが 50000 というペアを追加
my_dict["salary"] = 50000
print(my_dict["salary"])  # 50000 と表示させる