import re
import random
text = """キリンは大昔から _複数名詞_ の興味の対象でした。キリン
は _複数名詞_ の中で一番背が高いですが、科学者たちはそのような
長い _体の一部_ をどうやって獲得したのか説明できません。キリン
の身長は _数値_ _単位_ 近くあり、その高さのほとんどは脚と _体の一部_
によるものです。
 """
#coffee = """コーヒーチェリーは _色_ く、甘みは少ないです。しかし、
#近年では、チェリーを _飲料_ にしたりなど再利用の動きが活発になっ
#ています。
#"""
#author = """「告白」を書いたのは _作者名_ で、「ツイラク」を書いた
#のは、_作者名_ です。「告白」の作者は _作品名_ も発表しています。
#"""

#challenge = [text, coffee, author]
#n = random.randint(0,2）
#i = challenge[n]
#print("\n")
#print(i)
print(text)

def mad_libs(mls):

    #赤色の部分を含めて実行するとランダムに問題出題。
    #ランダムにする場合はmad_libsの引数も in にする。
    
    
    hints = re.findall("_.*_", mls)
    if hints is not None:
        for word in hints:
            q = "{}入力してください：".format(word)
            new = input(q)
            mls = mls.replace(word, new)
        print('\n')
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数無効です")
        
mad_libs(text)

