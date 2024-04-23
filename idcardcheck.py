#!/usr/bin/python
# -*- coding: UTF-8 -*-


def checkcalc(a):
    sum=int(a[0])*7+int(a[1])*9+int(a[2])*10+int(a[3])*5+int(a[4])*8+int(a[5])*4+int(a[6])*2+int(a[7])*1+int(a[8])*6+int(a[9])*3+int(a[10])*7+int(a[11])*9+int(a[12])*10+int(a[13])*5+int(a[14])*8+int(a[15])*4+int(a[16])*2
    #7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2
    yu=sum%11
    if yu==0:
        chk='1'
    elif yu==1:
        chk='0'
    elif yu==2:
        chk='x'
    elif yu==3:
        chk='9'
    elif yu==4:
        chk='8'
    elif yu==5:
        chk='7'
    elif yu==6:
        chk='6'
    elif yu==7:
        chk='5'
    elif yu==8:
        chk='4'
    elif yu==9:
        chk='3'
    elif yu==10:
        chk='2'
    if chk==a[17]:
        return True
    else:
        return False

    # 0－1－2－3－4－5－6－7－8－9－10
    # 这11个数字。其分别对应的最后一位身份证的号码为1－0－X－9－8－7－6－5－4－3－2

    return


if __name__ == '__main__':

    a='3301221984****1712'
    for month in range(1,13):
        for day in range(1, 32):
            b=a[:10]+"%02d" % month+"%02d" % day+a[14:]
            if True==checkcalc(b):
                print('check ok',b)


