import pickle
k=open("list_form.pickle","rb")
data=pickle.load(k)
k.close()

print(data[0])