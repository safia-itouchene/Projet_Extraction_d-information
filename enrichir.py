import sys,re
if len(sys.argv)!=2:#vérifier le nombre des args
	print("Vous devez entrer le fichier corpus")
else:	
	def ordre(sh1,sh2):
		Alphabet=["a","b","c","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		i=0
		while i<len(sh1) and i<len(sh2):
			if Alphabet.index(sh1[i]) > Alphabet.index(sh2[i]):
				return True
			if Alphabet.index(sh1[i]) < Alphabet.index(sh2[i]):
				return False
			else:
				i=i+1
		if(len(sh1)<=len(sh2)):
			return False
		else:
			return True

	file_subst_enri=open("subst_corpus.dic",'w',encoding="utf-16")
	file_subst_enri.write("\ufeff")

	file_subst=open("subst.dic",'r',encoding="utf-16")
	L_subst=file_subst.readlines()
	file_subst.close()
	
	file_corpus=open(sys.argv[1],'r',encoding="utf-8")
	L_corpus=file_corpus.readlines()
	file_corpus.close()

	regex="^([^A-Za-zéèêï]| ){0,3}([A-Za-zéèêï]+) (LP )?:? ?(\d+|\.|,)+ (g|mg|ml|mcg|UI|\d+?/j)".encode("utf-16").decode("utf-16")
	
	cmp=1
	list=[]
	list2=[]
	for j in L_corpus:
		j=j.encode("utf-16-le").decode("utf-16-le")
		
		recherche=re.findall(regex,j,re.I)
		
		if len(recherche)!=0: 
			linne=recherche[0][1].lower()+",.N+subst\n"
			
			file_subst_enri.write(linne)
			
			if(not(linne in L_subst)): 
				k=0
				while k<len(L_subst) and ordre(linne,L_subst[k]):
					k=k+1
				
				if k<len(L_subst):
					L_subst.insert(k,linne)
					if(not(linne in list2)):
						list2.append(linne)
			
			if(not(linne in list)):
				list.append(linne)
				
			print(str(cmp)+" "+recherche[0][1].lower())
			cmp=cmp+1
	file_subst_enri.close()
	
	file_subst=open("subst.dic",'w',encoding="utf-16-le")
	file_subst.write("\ufeff")
	for j in L_subst:
		file_subst.write(j)
	file_subst.close()
	
	file_info=open("infos2.txt",'w',encoding="utf-16")
	total=0
	#pour chaque lettre, on recherche dans list les entitées du cette lettre et on calcule le nombre des entitées 
	for k in ["a","b","c","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] :
		cmp=0
		for j in list:
			if(j[0]==k):
				file_info.write(j)
				cmp=cmp+1
		file_info.write("Total "+k+": "+str(cmp)+"\n")
		file_info.write("\n")
		total=total+cmp
	file_info.write("Total: "+str(total)+"\n")		
	file_info.close()
	
	file_info=open("infos3.txt",'w',encoding="utf-16")
	total=0
	for k in ["a","b","c","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] :
		cmp=0
		for j in list2:
			if(j[0]==k):
				file_info.write(j)
				cmp=cmp+1
		file_info.write("Total "+k+": "+str(cmp)+"\n")
		file_info.write("\n")
		total=total+cmp
	file_info.write("Total: "+str(total)+"\n")		
	file_info.close()
		

