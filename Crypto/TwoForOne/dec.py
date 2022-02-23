import sys, gmpy, base64

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)

    return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def pad_even(x):

        return ('', '0')[len(x)%2] + x



def CipherB2n(c):
    c2 = base64.b64decode(c)
    temp = ''
    for i in c2:
        temp += pad_even(str(hex(ord(i)))[2:])
    temp = eval('0x'+temp)
    return (temp)


def CipherN2b(m):
    hex_m=hex(m)[2:]
    if hex_m[-1] == 'L' :
        hex_m=hex_m[:-1]
    return hex_m.decode('hex')


if __name__ == '__main__':

    sys.setrecursionlimit(1000000)
    e1 = 65537 
    e2 = 343223
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    c1 = 'RBVdQw7Pllwb42GDYyRa6ByVOfzRrZHmxBkUPD393zxOcrNRZgfub1mqcrAgX4PAsvAOWptJSHbrHctFm6rJLzhBi/rAsKGboWqPAWYIu49Rt7Sc/5+LE2dvy5zriAKclchv9d+uUJ4/kU/vcpg2qlfTnyor6naBsZQvRze0VCMkPvqWPuE6iL6YEAjZmLWmb+bqO+unTLF4YtM1MkKTtiOEy+Bbd4LxlXIO1KSFVOoGjyLW2pVIgKzotB1/9BwJMKJV14/+MUEiP40ehH0U2zr8BeueeXp6NIZwS/9svmvmVi06Np74EbL+aeB4meaXH22fJU0eyL2FppeyvbVaYQ=='
    c2 = 'TSHSOfFBkK/sSE4vWxy00EAnZXrIsBI/Y6mGv466baOsST+qyYXHdPsI33Kr6ovucDjgDw/VvQtsAuGhthLbLVdldt9OWDhK5lbM6e0CuhKSoJntnvCz7GtZvjgPM7JDHQkAU7Pcyall9UEqL+W6ZCkiSQnK+j6QB7ynwCsW1wAmnCM68fY2HaBvd8RP2+rPgWv9grcEBkXf7ewA+sxSw7hahMaW0LYhsMYUggrcKqhofGgl+4UR5pdSiFg4YKUSgdSw1Ic/tug9vfHuLSiiuhrtP38yVzazqOZPXGxG4tQ6btc1helH0cLfw1SCdua1ejyan9l1GLXsAyGOKSFdKw=='
    c1 = CipherB2n(c1)
    c2 = CipherB2n(c2)
    #print hex(c1)
    n = 25080356853331150673712092961488349508728123694382279186941974911344272809718201683391687288116618021523872262260746884803456249468108932413753368793568123710905490623939699616018064364038794824072468125668702688048418916712950393799664781694224559810656290997284081084848717062228887604668548576609649709572412523306016494962925450783098637867249337121156908328927249731928363360657779226929980928871118145919627109584218577535657544952661333527174942990937484743860494188129607347202336812042045820577108243818426559386634634103676467773122325120858908782192357380855678371737765634819794619802582481594876770433687 
    if s1<0:
        s1 = - s1
        c1 = modinv(c1, n)
    elif s2<0:
        s2 = - s2
        c2 = modinv(c2, n)
    m=(pow(c1,s1,n)*pow(c2,s2,n)) % n
    print (m)
    print (CipherN2b(m))
