import subprocess
import sys
from ORF import translation
sels = sys.stdin.readlines()
ssels = [d.rstrip() for d in sels]
for s in ssels:
        arr = s.split("\t")
        loc = (arr[1], arr[2], "plus","+") if int(arr[1]) < int(arr[2]) else (arr[2], arr[1], "minus","-")
        command = ["efetch","-id",arr[0],"-db","nuccore","-format","fasta"]
        result = subprocess.run(command, capture_output=True, text=True)
        f = result.stdout.split("\n")
        slen = 0
        seq = ""
        for s in f:
           if ">" not in s:
              seq = seq + s.rstrip()
        slen = len(seq)
        sfrom = int(loc[0])
        sto = int(loc[1])
        while sfrom <= 0:
           sfrom = sfrom + 3
        while sto > slen:
           sto = sto - 3       
        loc = (str(sfrom),str(sto),loc[2],loc[3])
        fasta = seq[sfrom-1:sto]
        if loc[3] == "-":
          rfasta = ""
          for e in fasta:
             if   e == "A":
                rfasta = rfasta + "T"
             elif e == "T":
                rfasta = rfasta + "A"
             elif e == "C":
                rfasta = rfasta + "G"
             elif e == "G":
                rfasta = rfasta + "C"
             elif e == "R":
                rfasta = rfasta + "Y"
             elif e == "Y":
                rfasta = rfasta + "R"
             elif e == "S":
                rfasta = rfasta + "W"
             elif e == "W":
                rfasta = rfasta + "S"
             elif e == "K":
                rfasta = rfasta + "M"
             elif e == "M":
                rfasta = rfasta + "K"
             elif e == "B":
                rfasta = rfasta + "V"
             elif e == "V":
                rfasta = rfasta + "B"
             elif e == "D":
                rfasta = rfasta + "H"
             elif e == "H":
                rfasta = rfasta + "D"
             else:
                rfasta = rfasta + "N"
          fasta = rfasta[::-1]
#        command = ["efetch",
#                   "-id", arr[0] , "-db", "nucleotide", "-format", "fasta" ,"-seq_start",loc[0], "-seq_stop", loc[1], "-strand", loc[2]]
#        result = subprocess.run(command, capture_output=True, text=True)
#        f = result.stdout.split("\n")
#        fasta = ""
#        for ff in f:
#            if ">" not in ff:
#               fasta = fasta + ff
        protein = translation(fasta)
        print(f"1:{arr[0]}:{loc[0]}:{loc[1]}:{loc[3]}:{arr[3]}|{protein}|{fasta}")	
