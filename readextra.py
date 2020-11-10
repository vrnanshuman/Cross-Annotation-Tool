import pickle
f=open("all_abs.txt","r").read()
f=f.split("<newabs>")

document=[]
k=1

for each in f[:]:
	temp=[]
	print(k)
	elements=each.split("<newchar>")
	if(len(elements)==3):
		temp.append(elements[0])
		temp.append(elements[1])
		temp.append(elements[2].split("<n-term>")[:-1])
		document.append(temp)
	k+=1
	# print(elements)
# print(f[:1])
# print(document[0])
save_list=open("list_form.pickle","wb")
pickle.dump(document,save_list)
save_list.close()