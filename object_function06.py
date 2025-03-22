###デコレータ


###デコレータを使わないパターン
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'関数：{func.__name__}の実行します')
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{end_time - start_time:.2f}秒かかりました")
        return result
    print(f"関数{func.__name__}を受け取りました。")
    return wrapper

def total_function(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

total_func_decorated = timer_decorator(total_function)
result = total_func_decorated(1000000)
print(result)


###デコレータを使ったパターン
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'関数：{func.__name__}の実行します')
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{end_time - start_time:.2f}秒かかりました")
        return result
    print(f"関数{func.__name__}を受け取りました。")
    return wrapper

@timer_decorator
def total_function(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# total_func_decorated = timer_decorator(total_function)
# result = total_func_decorated(1000000)

result = total_function(1000000)
print(result)