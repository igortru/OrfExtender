import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m" 

accs = []
seqs = []
with open(sys.argv[1], "r") as file:
  sels = file.readlines()
  ssels = [s.rstrip() for s in sels]
  seq = ""
  acc = ""
  for s in ssels:
      if s[0] == ">":
          if acc != "":
              accs.append(acc)
              seqs.append(seq)
          acc = s
          seq = ""
      else:
          seq = seq + s
  accs.append(acc)
  seqs.append(seq)
  
up = len(seqs[0]) - len(seqs[2])
print(f"{accs[0]} {accs[2][1:]}\n{RED}{seqs[0][0:up]}{RESET}{seqs[0][up:]}{GREEN}{seqs[1][len(seqs[2]):]}{RESET}")
