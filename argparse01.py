import argparse

parser = argparse.ArgumentParser(description="このスクリプトの説明")
parser.add_argument('arg1', help='位置引数1です', type=int)
parser.add_argument('arg2', help='位置引数2です')

if __name__ == "__main__":
    args = parser.parse_args()
    print(f"arg1={args.arg1}", type(args.arg1))
    print(f"arg2={args.arg2}", type(args.arg2))

#print(type(args), args)

