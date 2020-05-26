a = []
sum = 0
while True:
    b = input('Pepsy shop\n Nike [1]\n Adidas [2]\n Reebok [3]\n  Pan [4]\n Bill [5]\n Exit [6]\n')
    b = b.lower()
    if b =='1':
        c = input('เลือกรุ่น(1,2,3)\n [1]Nike Air Max 97 \n [2]Air Jordan 1 Mid\n [3]Nike Air Zoom SuperRep\n')
        if c =='1':
            print("Nike Air Max 97 ราคา 2,500฿ ส่วนลด20% จ่ายจริง 2,000฿")
            a.append('Nike Air Max 97 : 2,500฿ : 20% : 2,000฿')
            g = int(2000)
            sum+= g
        elif c == '2':
            print("Air Jordan 1 Mid ราคา 3,500฿ ส่วนลด20% จ่ายจริง 2,800฿")
            a.append('Air Jordan 1 Mid : 3,500฿ : 20% : 2,800฿')
            g = int(2800)
            sum+= g
        elif c == '3':
            print("Nike Air Zoom Sup. ราคา 5,000฿ ส่วนลด20% จ่ายจริง 4,000฿")
            a.append('Nike Air Zoom Sup. : 5,000฿ : 20% : 4,000฿')
            g = int(4000)
            sum+= g
    elif b =='2':
        c = input('เลือกรุ่น(1,2,3)\n [1]PULSEBOOST HD M\n [2]PUSHA T OZWEEGO\n [3]ULTRABOOST M\n')
        if c =='1':
            print("PULSEBOOST HD M  ราคา 4,500฿ ส่วนลด30% จ่ายจริง 3,150฿")
            a.append('PULSEBOOST HD M : 4,500฿ : 30% : 3,150฿')
            g = int(3150)
            sum+= g
        elif c == '2':
            print("PUSHA T OZWEEGO ราคา 1,500฿ ส่วนลด30% จ่ายจริง 1,050฿")
            a.append('PUSHA T OZWEEGO : 1,500฿ : 30% : 1,050฿')
            g = int(1050)
            sum+= g
        elif c == '3':
            print("ULTRABOOST M ราคา 6,500฿ ส่วนลด30% จ่ายจริง 4,550฿")
            a.append('ULTRABOOST M :  6,500฿ : 30% : 4,550฿')
            g = int(4550)
            sum+= g
    elif b =='3':
        c = input('เลือกรุ่น(1,2,3)\n [1]AHARY RUNNER\n [2]SPEED TR FLEXWEAVE\n [3]REEBOK DRIFTIUM\n')
        if c =='1':
            print("AHARY RUNNER  ราคา 3,000฿ ส่วนลด50% จ่ายจริง 1,500฿")
            a.append('AHARY RUNNER : 3,000฿ : 50% : 1,500฿')
            g = int(1500)
            sum+= g
        elif c == '2':
            print("SPEED TR FLEXWEAVE ราคา 1,500฿ ส่วนลด50% จ่ายจริง 750฿")
            a.append('SPEED TR FLEXWEAVE : 1,500฿ : 50% : 750฿')
            g = int(750)
            sum+= g
        elif c == '3':
            print("REEBOK DRIFTIUM ราคา 4,000฿ ส่วนลด50% จ่ายจริง 2,000฿")
            a.append('REEBOK DRIFTIUM : 4,000฿ : 50% : 2,000฿')
            g = int(2000)
            sum+= g
    elif b =='4':
        c = input('เลือกรุ่น(1,2,3)\n [1]Pan A\n [2]Pan B\n [3]Pan C\n')
        if c =='1':
            print("Pan A  ราคา 3,000฿ ส่วนลด50% จ่ายจริง 1,500฿")
            a.append('Pan A : 3,000฿ : 50% : 1,500฿')
            g = int(1500)
            sum+= g
        elif c == '2':
            print("Pan B ราคา 1,500฿ ส่วนลด50% จ่ายจริง 750฿")
            a.append('Pan B : 1,500฿ : 50% : 750฿')
            g = int(750)
            sum+= g
    elif b =='5':
            print('{0:-<60}'.format(""))
            print('{0:<6}{1:<17}{2:<14}{3:<14}{4:<10}'.format('','รายการ','ราคา','ส่วนลด','จ่ายจริง'))
            print('{0:-<60}'.format(""))
            count = 0
            for x in a :
                y = x.split(":")
                count+=1
                print(count,end=")")
                print('{0[0]:<20}{0[1]:<15}{0[2]:<10}{0[3]:<10}'.format(y))
                continue
            print('{0:-<60}'.format(""))
            print('รวมเป็นเงิน',sum)
            print('\n')
    elif b =='6':
        exit()