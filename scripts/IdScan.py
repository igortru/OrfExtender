import subprocess
import sys
from ORF import translation
sels = sys.stdin.readlines()
ssels = [d.rstrip() for d in sels]
for s in ssels:
        arr = s.split("\t")
        loc = (arr[1], arr[2], "plus","+") if int(arr[1]) < int(arr[2]) else (arr[2], arr[1], "minus","-")
        command = ["efetch","-id",arr[0],"-db","nucleotide","-format","docsum"]
        result = subprocess.run(command, capture_output=True, text=True)
        f = result.stdout.split("\n")
        slen = 0
        for s in f:
           if s.find("<Slen>") > 0:
              slen = int(s.split(">")[1].split("<")[0])       
        sfrom = int(loc[0])
        sto = int(loc[1])
        while sfrom <= 0:
           sfrom = sfrom + 3
#        while sto > slen:
#           sto = sto - 3       
        loc = (str(sfrom),str(sto),loc[2],loc[3])

        command = ["efetch",
                   "-id", arr[0] , "-db", "nucleotide", "-format", "fasta" ,"-seq_start",loc[0], "-seq_stop", loc[1], "-strand", loc[2]]
        result = subprocess.run(command, capture_output=True, text=True)
        f = result.stdout.split("\n")
        fasta = ""
        for ff in f:
            if ">" not in ff:
               fasta = fasta + ff
        protein = translation(fasta)
        print(f"1:{arr[0]}:{loc[0]}:{loc[1]}:{loc[3]}:{arr[3]}|{protein}|{fasta}")	
