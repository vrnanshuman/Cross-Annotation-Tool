from __future__ import division
import pickle
import re
import threading
# from nltk.tokenize import sent_tokenize
import codecs

lock=threading.Lock()

f=open("genedb.txt","r").read()

tr=[]
document=[]

abstext=""

f=f.split("\n")
f=f[1:-1]
# print(f[1])
# print(f[1])
# print("\n")

k=open("list_form.pickle","rb")
data=pickle.load(k)
k.close()

print(len(data))

fd=open("absonly.txt","w")
for each in data:
	abstext+=each[1]
save_abs=open("saved_abstract.pickle","wb")
pickle.dump(abstext,save_abs)
save_abs.close()
# abstext = abstext.decode('unicode_escape').encode('ascii','ignore')
# print(sent_tokenize(abstext))





# fd.write(abstext)
# # print(abstext)

list_of_search_terms=[]

for each in f:#gene database
	each=each.split("\t")#each is one row of items
	# print(each)
	# ids=[0,9]
	indices=[1,2,4,5,6,0,9]
	temp1=[each[x] for x in indices]
	# temp2=[each[x] for x in indices]
	# print(temp1)
	list_of_search_terms.append(temp1)

#print list_of_search_terms

stat=open("statistics_new.txt","w")
stat.write("Matched\t\t\t|")
stat.write("Position \t\t\t|")
stat.write("Replaced By \t\t\t|")
stat.write("Frequency \t\t\t|")
stat.write("\n\n")
stat.write("--------------------------------------------------------------------------------------------------\n")
stat.write("--------------------------------------------------------------------------------------------------\n")


def calledfunc(codeword):
	global abstext
	t=codeword
	if t != '':
		find_term=" "+t+" "
		with lock:
			stat.write("\n--------------------------------------------------------------------------------------------------\n")
			try:
				# if find_term in abstext:
				tr.append(find_term)
				print "Find Term: "+str(find_term)
				# print abstext.index(find_term)
				replace_id=each[5]
				if(each[6]!=""):
					replace_id=each[6]

				print "Replace ID : "+replace_id

				# stat.write(str(abstext.index(new_string))+"\t\t\t|")
				new_string=" "+replace_id+" "
				pattern=re.compile(find_term)
				abstext=re.sub(pattern,new_string,abstext)
				stat.write(find_term+"\t\t\t|")
				# print(str(abstext.index(new_string))+"\n")
				stat.write(replace_id+"\t\t\t|")
				
				
			except Exception as e:
				pass	


records_processed=0;
total_records=len(list_of_search_terms)




for each in list_of_search_terms:#list of rows  with required columns
	# per=records_processed/total_records*100.0
	# print(str(per)+"%\n")
	# records_processed+=1
	# ccount=0
	for t in each[:-2]:
		newthread=threading.Thread(target=calledfunc,args=(t,))
		newthread.start()


while threading.activeCount() > 1:
	pass
else:
	stat.close()		
	# 	if t != '':
	# 		find_term=" "+t+" "
	# 		if find_term in abstext:
	# 			tr.append(find_term)
	# 			print find_term
	# 			print abstext.index(find_term)
	# 			print each[5]
	# 			stat.write(find_term+"\t\t\t|")
	# 			stat.write(str(abstext.index(find_term))+"\t\t\t|")
	# 			stat.write(each[5]+"\t\t\t|")
	# 			ccount+=1
	# stat.write("\n--------------------------------------------------------------------------------------------------\n")				
	# stat.write(str(ccount)+"\t\t\t|")
	
				# print(find_term+" FOUND with ID "+each[5])
				# print("\n")
			# else:
				# print(find_term+" NOT FOUND \n")


new_file=open("edited_Abs.txt","w")
new_file.write(abstext)
new_file.close()


print("FOUND ITEMS")
print(tr)
document.append(temp1)

# for each in document[1:]:
# 	print(each)



