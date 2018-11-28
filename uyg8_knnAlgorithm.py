#KNN ile yeni eklenen verinini sınıfını bulma
import pandas as pd
import csv
iris=pd.read_csv("iris.csv")
results = []
with open("iris.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
def öklid(test,dataset):
    return float((test[0]-dataset[1])**2+(test[1]-dataset[2])**2+
                 (test[2]-dataset[3])+(test[3]-dataset[4]))**.5

def knn(k,dataset,test):
    mesafeler=[]
    for i in range(len(dataset)):
        mesafe=öklid(test,dataset[i])
        mesafeler.append([mesafe,dataset[i][5]])
    mesafeler.sort()
    sınıflar=[[0,0],[1,0],[2,0]]
    for i in range(k):
        if(mesafeler[i][1]==0.0):
            sınıflar[0][1]=sınıflar[0][1]+1
        elif(mesafeler[i][1]==1.0):
            sınıflar[1][1]=sınıflar[1][1]+1
        else:
            sınıflar[2][1] = sınıflar[2][1] + 1

    sınıflar.sort()
    print("Kazanan sınıf=",sınıflar[2][0])



knn(140,results,[4,3,4,4])
