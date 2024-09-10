import random
#　それぞれの宝くじの数字を予測をします

#repeat=◯,△,☓,をrandomで出力 
def repeat():
    print(random.sample(( '◯','△','☓', ) ,1))
    
takara = {'ナンバーズ3' :3 , 'ナンバーズ4' :4 ,'ビンゴ5' :5 , 'ロト6' :6 , 'ロト7' :7}
a = list(takara.keys())
print(a)
print('ナンバーズ3')
print(random.sample(range(0,10) ,3))
repeat()
print('ナンバーズ4')
print(random.sample(range(0,10) ,4))
repeat()
print('ビンゴ5')
print(random.sample(range(1,41) ,5))
repeat()
print('ロト6')
print(random.sample(range(1,44) ,6))
repeat()
print('ロト7')
print(random.sample(range(1,38) ,7))
repeat()

x = 50
y = 100
X = y
str = (x)
text = f'{X}%当たりますように。'
print(text)

#shin