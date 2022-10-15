#警告　宝くじをあまりに大量に購入した事で発生するフリーズ、バグ、クラッシュについてはEBRは賠償責任を負いません。
#1億枚実行した際、結果出力に10分ほどかかりました。個人的趣味でPCをいじめることは良い考えではありません。

import random

print()
#当たった枚数の計算用
atari_1tou = 0
atari_1tou_near = 0
atari_1tou_kumi = 0
atari_2tou = 0
atari_3tou = 0
atari_4tou = 0
atari_5tou = 0
atari_6tou = 0
atari_7tou = 0

#宝くじをn枚買う。
Maisuu = int(input("宝くじを何枚買いますか？")) 
hyouji1 = input("購入した宝くじを一括表示しますか？ はい or いいえ")
hyouji2 = input("宝くじが当選したら、1枚ずつ当選したとメッセージを表示しますか？ はい　or いいえ")
print()
print("実行中・・・")
#購入した宝くじ1枚1枚、組と番号と下3,2,1桁を配列に格納する
A_kumi = []
Takara = []
Takara_list5 = []
Takara_list6 = []
Takara_list7 = []
if hyouji1 == "はい":
    print("あなたの引いた宝くじは",end ="")
else:
    pass
for i in range(Maisuu):
    kumi = str(random.randint(1,100))
    A_kumi.append(kumi)
    A1 = str(random.randint(100000, 999999))
    Takara.append(A1)
    #配列名+[]で下〇桁の数字のみ取り出し、それを配列に格納する。こうする事で下3桁が073番などが表現できる。
    Takara_list5.append(A1[-3]+A1[-2]+A1[-1])
    Takara_list6.append(A1[-2]+A1[-1])
    Takara_list7.append(A1[-1])
    if hyouji1 == "はい":
        if i < Maisuu-1:
            print(str(A_kumi[i])+"組の"+Takara[i]+"番、", end="")
        else:
            print(str(A_kumi[i])+"組の"+Takara[i]+"番の"+str(Maisuu)+"枚です。")
    else:
        pass
print()

#n枚のうち1枚でも当たったかどうかチェッカー
COUNT = 0  

#1等を決める
tousen_1 = random.randint(100000, 999999)
tousen_1_kumi = random.randint(1,100)
print("一等は"+str(tousen_1_kumi)+"組の"+str(tousen_1)+"番です。")

#1等前後賞を決める
tousen_1_near1 = int(tousen_1) + 1
tousen_1_near2 = int(tousen_1) - 1
print("一等前後賞は"+str(tousen_1_kumi)+"組の"+str(tousen_1_near2)+"番と"+str(tousen_1_near1)+"番です。")

#1等組み違いを決める
print("一等組み違い賞は各組共通の"+str(tousen_1)+"番です。")

#2等を決める
tousen_2 = str(random.randint(100000, 999999))
tousen_2_kumi = []
print("二等は", end="")
for i in range(4):
    a2 = str(random.randint(1, 100))
    tousen_2_kumi.append(a2)
    if i < 3:
        print(str(tousen_2_kumi[i])+"組、", end="")
    else:
        print(str(tousen_2[i])+"組の", end="")
print(str(tousen_2)+"番です。")

#3等を決める
tousen_3 = str(random.randint(100000, 999999))
print("三等は各組共通の"+str(tousen_3)+"番です。")

#4等を決める
tousen_4 = []
print("四等は各組共通の", end="")
for i in range(7):
    a4 = str(random.randint(100000, 999999))
    tousen_4.append(a4)
    if i < 6:
        print(str(tousen_4[i])+"番、", end="")
    else:
        print(str(tousen_4[i])+"番です。")

#5等を決める
tousen_5 = []
for i in range(3):
    tousen5_random = str(random.randint(0,9))
    tousen_5.append(tousen5_random)
print("五等は各組共通の下3桁"+tousen_5[0]+tousen_5[1]+tousen_5[2]+"番です。")
T5 = int(tousen_5[0]+tousen_5[1]+tousen_5[2])

#6等を決める
tousen_6 = []
for i in range(2):
    tousen6_random = str(random.randint(0,9))
    tousen_6.append(tousen6_random)
print("六等は各組共通の下2桁"+tousen_6[0]+tousen_6[1]+"番です。")
T6 = int(tousen_6[0]+tousen_6[1])

#7等を決める
tousen_7 = random.randint(0,9)
print("七等は各組共通の下1桁"+str(tousen_7)+"番です。")

print()

#IF文の組み立て（地獄）
#まず1等組み違い→1等と区別
for i in range(Maisuu):
    if Takara[i] == tousen_1:
        if A_kumi[i] == tousen_1_kumi:
            COUNT = 1
            atari_1tou += 1
        else:
            COUNT = 1
            atari_1tou_kumi += 1

#1等前後賞を区別
    elif (Takara[i] == tousen_1 + 1 or Takara[i] == tousen_1 - 1) and A_kumi[i] == tousen_1_kumi:
        COUNT = 1
        atari_1tou_near += 1
    else:
        pass

#2等を区別
#まず購入した宝くじ1枚を配列から持ってきて、それが４つの組に該当するかを調べ、更に番号が一致するかを調べる。これを枚数分繰り返す
for i in range(Maisuu):
    for j in range(4):
        if A_kumi[i] == tousen_2_kumi[j]:
            if Takara[i] == tousen_2:
                COUNT = 1
                atari_2tou += 1
            else:
                pass
        else:
            pass
#3等を区別
if Takara[i] == tousen_3:
    COUNT = 1
    atari_3tou += 1

#4等を区別
#2等と考え方は同じ。組を選考しなくて良いので少し楽
else:
    for i in range(Maisuu):
        for j in range(7):
            if Takara[i] == tousen_4[j]:
                COUNT = 1
                atari_4tou += 1
            else:
                pass

#5,6,7等を区別
for i in range(Maisuu):
    if int(Takara_list5[i]) == T5:
        COUNT = 1
        atari_5tou += 1
    elif int(Takara_list6[i]) == T6:
        COUNT = 1
        atari_6tou += 1
    elif int(Takara_list7[i]) == tousen_7:
        COUNT = 1
        atari_7tou += 1
    else:
        pass

#ユーザーの希望に合わせて当選メッセージを表示
if hyouji2 == "はい":
    for i in range(atari_1tou):
        print("おめでとうございます！1等が当たりました！！7億円をお受け取りください！！")
    for i in range(atari_1tou_kumi):
        print("おめでとうございます！1等組違い賞です！10万円をお受け取りください！！")
    for i in range(atari_1tou_near):
        print("おめでとうございます！1等前後賞が当たりました！1億5000万円をお受け取りください！！")
    for i in range(atari_2tou):
        print("おめでとうございます！2等が当たりました！1000万円をお受け取りください！！")
    for i in range(atari_3tou):
        print("おめでとうございます！3等が当たりました！100万円をお受け取りください！！")
    for i in range(atari_4tou):
        print("おめでとうございます！4等が当たりました！10万円をお受け取りください！！")
    for i in range(atari_5tou):
        print("おめでとうございます！5等が当たりました！1万円をお受け取りください！！")
    for i in range(atari_6tou):
        print("おめでとうございます！6等が当たりました！3000円をお受け取りください！！")
    for i in range(atari_7tou):
        print("おめでとうございます！7等が当たりました！300円をお受け取りください！！")
else:
    pass

#1枚でも当たりが出たらCOUNT=1になるので、これではずれを申告する。
if COUNT != 1:
    print("残念！夢を買っただけのようです！！")
else:
    print("おめでとうございます！配当金をお受け取りください！")

print()

#当たった枚数を一括表示
print("1等:"+str(atari_1tou)+"枚 ", end="")
print("1等前後賞:"+str(atari_1tou_near)+"枚 ", end="")
print("1等組違い賞:"+str(atari_1tou_kumi)+"枚 ", end="")
print("2等:"+str(atari_2tou)+"枚 ", end="")
print("3等:"+str(atari_3tou)+"枚 ", end="")
print("4等:"+str(atari_4tou)+"枚 ", end="")
print("5等:"+str(atari_5tou)+"枚 ", end="")
print("6等:"+str(atari_6tou)+"枚 ", end="")
print("7等:"+str(atari_7tou)+"枚 ")

#集計（単純に当たった枚数×当選金の計算）
MOUKE = 700000000*atari_1tou + 100000*atari_1tou_kumi + 150000000*atari_1tou_near + atari_2tou*10000000 + atari_3tou*1000000 + atari_4tou*100000 + atari_5tou*10000 + atari_6tou*3000 + atari_7tou*300
Katta_takarakuji = 300 * Maisuu
if MOUKE > Katta_takarakuji:
    hantei = "黒字"
    Last = MOUKE - Katta_takarakuji
else:
    hantei = "赤字"
    Last = Katta_takarakuji - MOUKE
print("当選金合計: "+str(MOUKE)+"円")
print("宝くじ購入金額: "+str(Katta_takarakuji)+"円")
print(str(Last)+"円の"+hantei+"です。")









