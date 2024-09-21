""" 53.キーワード引数の辞書化
*args: 可変長位置引数を受け取ります。これにより、関数に複数の引数が渡された場合、それらがタプルとして渡されます。
**kwargs: キーワード引数を複数受け取ります。これにより、関数に名前付きの引数が渡された場合、それらが辞書として渡されます。
*の一つと2つがある場合、必ず2つを後
"""

p


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


d = {"entree": "beef", "drink": "ice coffee", "dessert": "ice"}
menu("banana", "apple", "beef", **d)

""" 57.デコレーター
このPythonコードでは、デコレータを使って関数の挙動を拡張しています。特に、@print_info を使うことで、関数の実行前後に追加の処理を挿入する方法を示しています。

1. print_info 関数
print_info 関数は、デコレータとして機能するための関数です。デコレータは、ある関数の前後に処理を追加するために使われます。
引数 func: デコレータが適用される関数（後述の add_num 関数）がこの引数に渡されます。
wraapper 関数: func をラップする内部関数。*args と **kwargs で、元の関数に渡されるすべての引数をキャプチャしています。
print('start'): 元の関数の前に「start」を出力します。
result = func(*args, **kwargs): 元の関数（add_num）を実行し、その結果を result に格納します。
print('end'): 元の関数の後に「end」を出力します。
戻り値 result: 元の関数の戻り値を返します。

2. デコレータの適用：@print_info
この部分で、@print_info というデコレータが add_num 関数に適用されています。これによって、add_num 関数は自動的に print_info のラップ処理を通るようになります。具体的には、add_num 関数が呼び出されるたびに、print_info 内の wraapper 関数が呼ばれ、前後に「start」と「end」が出力されます。

3. 関数の実行
ここで、add_num(10, 20) が実行されます。この呼び出しにより、実際には wraapper(10, 20) が実行されます。wraapper 関数は次のような処理を行います。

print('start') が呼ばれ、"start" が出力されます。
元の add_num(10, 20) が実行され、結果は 30 です。
print('end') が呼ばれ、"end" が出力されます。
最後に、結果の 30 が r に代入されます。
"""


def print_info(func):
    def wraapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wraapper


@print_info
def add_num(a, b):
    return a + b


r = add_num(10, 20)
# f = print_info(add_num)
# r = f(10,20)
# print(r)


"""58.ラムダ
Pythonのラムダ関数（lambda）は、無名関数（名前を持たない関数）を簡潔に定義するための構文です。通常の関数を def を使って定義するのに対し、lambda を使うと、短く簡潔な一行の関数を定義することができます。

基本構文
lambda 引数1, 引数2, ... : 式
lambda: キーワード。これで無名関数を定義します。
引数1, 引数2, ...: カンマ区切りで複数の引数を指定します（引数はゼロでもOK）。
式: 関数が返す値。式は1つで、計算や処理をここで行います。

# 通常の関数
def add(x, y):
    return x + y

# ラムダ関数で定義
add_lambda = lambda x, y: x + y

# 両方同じ結果
print(add(2, 3))         # 5
print(add_lambda(2, 3))  # 5

"""

"""59.ジェネレーター
ジェネレーター（generator）は、Pythonで大きなデータを効率的に処理するために使用される特殊な関数です。ジェネレーターは一度に1つの値を生成し、次に進む際にその状態を保持できるため、メモリを効率的に使用します。

ジェネレーターは、普通の関数と似ていますが、return の代わりに yield を使って値を返します。この yield によって、ジェネレーターは一時停止し、再び呼び出されると前回の状態から再開されます。

例：シンプルなジェネレーター
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
この例では、simple_generator は yield によって 1, 2, 3 を順に返します。next 関数を使うと、ジェネレーターの次の値を取得できます。最後まで行くと、StopIteration 例外が発生します。

ジェネレーターの利点
メモリ効率: 全ての値を一度にメモリに格納する必要がないため、巨大なデータセットや無限のシーケンスを扱う際に便利です。
遅延評価: 必要になったときにだけ値を生成するため、不要な計算を避けられます。
無限ジェネレーターの例
ジェネレーターは無限のシーケンスを扱うのにも適しています。

def infinite_generator():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_generator()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# 以降、無限に続く
この infinite_generator は、n を増やし続ける無限のジェネレーターです。next で呼び出すたびに次の値を生成し、無限に続きます。

for ループとジェネレーター
通常、ジェネレーターは next を手動で呼び出すのではなく、for ループで繰り返し処理します。

def count_up_to(max_value):
    n = 1
    while n <= max_value:
        yield n
        n += 1

for number in count_up_to(5):
    print(number)
この例では、count_up_to ジェネレーターが 1 から max_value までの数値を生成し、for ループで順番に処理しています。

ジェネレーター式
ジェネレーターは、リスト内包表記のようにジェネレーター式としても定義できます。こちらは一行で簡潔にジェネレーターを作成する方法です。

gen_exp = (x * 2 for x in range(5))
print(next(gen_exp))  # 0
print(next(gen_exp))  # 2
print(next(gen_exp))  # 4
この例では、(x * 2 for x in range(5)) がジェネレーター式で、リスト内包表記の代わりに、必要なときに値を生成します。

ジェネレーターの活用例
1. 大量のデータを処理する
たとえば、ファイルの行を1行ずつ読み込む場合、すべての行を一度に読み込むとメモリを消費しますが、ジェネレーターを使うと1行ずつ処理できます。

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

for line in read_large_file('large_text_file.txt'):
    process(line)  # 行を1行ずつ処理
2. シーケンス処理
ジェネレーターを使って、動的な数列を作ることも可能です。例えば、フィボナッチ数列を作るジェネレーターは以下のようになります。

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _ in range(10):
    print(next(fib))  # 最初の10個のフィボナッチ数を出力
まとめ
ジェネレーターは、メモリ効率が高く、必要なときに値を生成するための関数です。
yield を使って値を返し、一時停止した状態で次の呼び出し時に再開します。
巨大なデータセットや無限シーケンスを扱うのに最適です。
"""

"""import
*読み込みは推奨されない
"""

from lesson_package import utils

r = utils.say_twice("hello")
print(r)

from lesson_package.talk import *

animal.sing()

x = {"aaaa", "aaa"}
