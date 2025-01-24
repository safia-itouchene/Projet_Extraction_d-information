from bs4 import BeautifulSoup
import urllib.request
import sys

srt = open("subst.dic",'w',encoding='utf-16-le')
srt.write('\ufeff')
srt2 = open("infos1.txt",'w')
data = sys.argv[1] 
page = data[0] 
fin_page = data[2]
port = sys.argv[2]
k = 0
n = 0
while(ord(page) <= ord(fin_page)):
    source = urllib.request.urlopen('http://localhost:'+str(port) +
                          '/vidal/vidal-Sommaires-Substances-'+page+'.htm')
    soup = BeautifulSoup(source, 'lxml')
    match = soup.find('ul', class_='substances list_index has_children')
    match.text.strip()
    for ligne in match.text.splitlines():
        if not ligne.strip():
            continue
        srt.write(ligne+",.N+subst\n")
        n = n+1
    srt2.write("le nombre des mediacaments avec la lettre " +
                  str(page)+" est: "+str(nbr)+"\n")
    k = nbr+k
    nbr = 0
    page = chr(ord(page)+1)
srt2.write("le nombre total des medicaments est :"+str(i))
