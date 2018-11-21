#my_perceptron
def my_product_two_dim_with_threshold(a,b): #a*b yi bulan fonksiyon
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def get_my_data(): # tabloyu elde etmek için kullandık
    my_data_x=[]
    my_data_x.append([1,0,0])
    my_data_x.append([1,0,1])
    my_data_x.append([1,1,0])
    my_data_x.append([1,1,1])
    my_data_y=[]
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    return (my_data_x,my_data_y)

x,y= get_my_data()
for a,b in zip(x,y):
    print(a,b)

def get_parameters(): #random olusturulan epoch ve diger degerler
    w=[]
    w.append(300)
    w.append(200)
    w.append(100)
    learning_rate = 1 # randomly
    epoch=100
    return  w,learning_rate,epoch

w,learning_rate,epoch = get_parameters()
samples,output = get_my_data()

for i in range(151):
    error = "hata_yok"
    s = -1
    for each_sample, d in zip(samples, output):
        s=s+1
        print("")
        print("agırlık :",w)
        print("örnek :",each_sample)
        print("gercek output : ", d)
        #print(my_product_two_dim_with_threshold(w,each_sample))
        u = my_product_two_dim_with_threshold(each_sample,w)
        if (u > 0):
            y = 1
        else:
            y = 0
        print("tahmin cıktı : ",y)
        #print("")
        if (y != d):#hata var
            for s in range(3):
                w[s] = w[s] - learning_rate * (y - d) * each_sample[s]
            error = "hata_var"
            print(error)
        else:
            print(error)
print("")
print(w)


#w parameters
#print(w)
