import re
import sqlite3
import sys

if len(sys.argv)!=2:
	print("Entrer le fichier concord.html en arguments")
else:
	fichier=open(sys.argv[1],"r",encoding="utf8")
	posol=re.findall("<a href=\"(\d| )+?\">(.+)?</a>",fichier.read())
	data_base=sqlite3.connect("extraction.db")
	a=data_base.cursor()
	a.execute("créer dans le tableau si n'exixte pas EXTRACTION(id int,posologie text)")
	k=1
	for k in posol:
		a.execute("insert dans EXTRACTION(id,posologie) values ("+str(k)+",'"+k[1]+"')")
		print(str(i)+" "+k[1])
		k=k+1
	data_base.commit()
	data_base.close()
	fichier.close()