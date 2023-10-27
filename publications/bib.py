import glob
import os
from shutil import copy2
from pybtex.database.input import bibtex

#dir="../../../Bibliography"
#outdir="./bib"
outdir="../bibliography"
bibdir="./texbib"

# 1) copy files from Jabref directory

#files=glob.glob(dir+"/*.bib")
#for file in files:
#    name=os.path.basename(file)
#    print("copy",name)
#    copy2(file,os.path.join(outdir,name))

# 2) create bibitem includes

files=glob.glob(outdir+"/*.bib")
for file in files:
    print("process",file)
    name=os.path.basename(file).replace(".bib","")
    parser = bibtex.Parser()
    bib_data = parser.parse_file(file)
    with open(bibdir+"/"+name+'_bib.tex', 'w') as f:
        for entry in bib_data.entries.keys():
            f.write("\\item\\bibentry{"+entry+"}\\label{"+entry+"}\n")
        
        
    
