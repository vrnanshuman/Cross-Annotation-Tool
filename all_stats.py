import pickle

f=open("details_all.txt","w")

f1=open("list_form.pickle","rb")
list_of_list=pickle.load(f1)
f1.close()
f.write("Statistics for the terms 'ExtraCellular Matrix Remodeling,ECM,ECM Remodeling '")
f.write("\n")
f.write("\n----------------------------------------------------------------------------------------------------------\n")
f.write("Total Number of abstracts :  "+str(len(list_of_list)))
f.write("\n")
f.write("\n")
f.write("\n----------------------------------------------------------------------------------------------------------\n")

f1=open("mesh_dictionary.pickle","rb")
counts=pickle.load(f1)
f1.close()

f.write("Total number of MeSH Terms : "+str(len(counts)))
f.write("\n")
f.write("\n")
f.write("\n----------------------------------------------------------------------------------------------------------\n")

f.write("Most common MeSH terms with frequency:(25) ")
f.write("\n")
f.write("\n")
# f.write("\n----------------------------------------------------------------------------------------------------------\n")

for key,value in counts.most_common(25):
	f.write(str(key)+"\t"+str(value))
	f.write("\n")

f.write("\n")
f.write("\n----------------------------------------------------------------------------------------------------------\n")

f.close()