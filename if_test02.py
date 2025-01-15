'''
国語の点数と数学の点数の合計が140点以上で合格と表示するプログラムを作成しました。
このプログラムに、「どちらかの点数が60点未満の場合は合計が140点以上であっても不合格と表示する」機能を追加してください。

kokugo = 40
sugaku = 100

if kokugo + sugaku >= 140: # この行は書き換えないでください
    print('合格')
else:
    print('不合格')

'''

kokugo = 40
sugaku = 100

if kokugo < 60 or sugaku < 60:
    print('不合格')
if kokugo > 60 and sugaku > 60:
    if kokugo + sugaku >= 140: # この行は書き換えないでください
        print('合格')
    else:
        print('不合格')
