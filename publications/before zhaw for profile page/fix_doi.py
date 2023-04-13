import re
import os

infile="before_zhaw.txt"
outfile="before_zhaw_fixed.txt"

f = open(infile,"r",encoding="utf8")
lines = f.readlines()

if os.path.exists(outfile):
    os.remove(outfile)

re_doi=re.compile('doi:\s\S*\s')
re_onl=re.compile(' \[Online\]. Available: \S*')

with open(outfile,"w",encoding="utf8") as fout:
    for l in lines:
        #print(l)

        no=l.split(" ")[0]
        if no=="[1]":
            fout.write("Journal Publications:\n\n")
        if no=="[30]":
            fout.write("Proceedings:\n\n")
        if no=="[53]":
            fout.write("Conference Papers and Technical Reports:\n\n")
        if no=="[81]":
            fout.write("Theses:\n\n")


        doi=re.search(re_doi,l)
        if doi is not None:
            val=doi.group()
            doi=val.split("doi: ")[1]
            newdoi='https://doi.org/'+doi
            lnew=re.sub(re_doi,newdoi,l)

            # if doi link, remove url link
            onl=re.search(re_onl,lnew)
            if onl is not None:
                lnew=re.sub(re_onl,"",lnew)

            fout.write(lnew)


        else:
            fout.write(l)


        
