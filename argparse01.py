import argparse

def total(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value}は整数ではありません")
    return int(value) + int(value)

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"私の名前は{self.name}です。"

parser = argparse.ArgumentParser(description="このスクリプトの説明")
parser.add_argument('arg1', help='位置引数1です', type=int)
parser.add_argument('arg2', help='位置引数2です')
parser.add_argument('-o', '--output__path', help='出力先のパスを設定', required=True)
parser.add_argument('-n', '--num', help='数値を指定', type=int, default=1)
parser.add_argument('-t', '--total',type=total, help='合計値を出力する')
parser.add_argument('-p', '--person', help='nameを指定', type=Person, default=Person("山田"), action='store', dest='person')
parser.add_argument('-b', '--bool', type=bool, help='フラグを設定する')
parser.add_argument('-m', '--mode', choices=['a', 'b', 'c'], help='モードを指定')

if __name__ == "__main__":
    args = parser.parse_args()
    print(f"arg1={args.arg1}", type(args.arg1))
    print(f"arg2={args.arg2}", type(args.arg2))
    print(f"output_path={args.output__path}")
    print(f"num={args.num}")
    print(f"total={args.total}")
    print(f"person={args.person}")
    print(f"bool={args.bool}") #boolは基本使わない。文字をすべてTrueになるため
    print(f"mode={args.mode}")

#print(type(args), args)

