prerequisites :

1) Entrez Direct: E-utilities on the Unix Command Line
https://www.ncbi.nlm.nih.gov/books/NBK179288/

    sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

2) python,awk

setup: 
  add +x to scripts
  '''
  chmod u+x setup.sh
  ./setup.sh

use:

    ./scripts/ExtendDownStream.sh acc max_len letter row

    acc - genbank protein accession
    max_len  - max number of AA can be added downstream
    letter - replace "*" with "U"
    row - row number from NCBI ipg report , default = 2

    ./scripts/ExtendUpStream.sh  acc max_len letter count

    acc - genbank protein accession
    max_len  - max number of AA can be added upstream
    letter - replace "*" with  "U"
    row - row number from NCBI ipg report , default = 2

test:

    awk '{printf "echo %s;./scripts/ExtendDownStream.sh %s 200 U\n",$1,$1;}' ./tests/test.set  | sh

