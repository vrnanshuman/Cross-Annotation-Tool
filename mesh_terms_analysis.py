import re
import pickle
from collections import Counter
# import pandas
# import pandas as pd
# import numpy

f=open("list_form.pickle","rb")
list_of_list=pickle.load(f)#list of 3
f.close()

# print(list_of_list[0])

all_mesh_terms=[]

for each in list_of_list:
	all_mesh_terms.extend([x.lower() for x in each[2]])
	
p1=open("all_mesh.pickle","wb")
pickle.dump(all_mesh_terms,p1)
p1.close()


# p1=open("all_mesh.pickle","rb")
# all_mesh_terms=pickle.load(p1)
# p1.close()

# print all_mesh_terms
# print len(all_mesh_terms)

mesh_set=set(all_mesh_terms)

p2=open("mesh_set.pickle","wb")
pickle.dump(mesh_set,p2)
p2.close()

# p2=open("mesh_set.pickle","rb")
# mesh_set=pickle.load(p2)
# p2.close()

# print len(mesh_set)

f1=open("mesh_statistics.txt","w")

counts=Counter(all_mesh_terms)
# print(df)

p2=open("mesh_dictionary.pickle","wb")
pickle.dump(counts,p2)
p2.close()

for key,value in counts.items():
	f1.write(key+" \t\t"+str(value))
	f1.write("\n")
	print(key+" \t\t "+str(value))

print(counts.most_common(10))
# print(len(counts))


