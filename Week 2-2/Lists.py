studentIDS = [18, 25, 99, 7, "tamer"]
studentIDS[4] = 34.76

x = studentIDS[1:3]

studentIDS[1] = 12
y = studentIDS # aynı listeye iki isim verilmiş oldu, linki kopyaladı, değerleri değil

studentIDS[2]=33

y = studentIDS[:]

def f():
    return 10