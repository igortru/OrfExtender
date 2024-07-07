For any given genbank protein accession, if it linked with nucleotide where protein was annotated
allow extend orf upstream and downstream.

use-cases:

        selenoproteins : replace  "TGA" * with "U"
        proteins (mostly phages, annotated with genetic code 11) with genetic code 15 :  "TGA" * -> "Q"

prerequisites :

        Entrez Direct: E-utilities on the Unix Command Line https://www.ncbi.nlm.nih.gov/books/NBK179288/

        sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

        python,awk

setup: 
      add +x to scripts

      chmod u+x setup.sh
      ./setup.sh

use:

    ./scripts/ExtendDownStream.sh acc max_len letter row

    acc - genbank protein accession
    max_len  - max number of AA can be added downstream,  try = 100-200
    letter - replace "*" with "U"
    row - row number from NCBI ipg report , default = 2

    ./scripts/ExtendUpStream.sh  acc max_len letter count

    acc - genbank protein accession
    max_len  - max number of AA can be added upstream, try = 100-200
    row - row number from NCBI ipg report , default = 2

test:

    awk '{printf "echo %s;./scripts/ExtendDownStream.sh %s 200 U\n",$1,$1;}' ./tests/test.set  | sh

