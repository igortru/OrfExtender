Given a GenBank protein accession, if it's linked to the nucleotide sequence where the protein was annotated, tool can extend the open reading frame (ORF) upstream or downstream to search for alternative stop codons. This allows for easier validation of annotated GenBank proteins suspected to have premature stop codons

use-cases:

        selenoproteins : replace  "TGA" * -> "U"
        proteins (mostly phages, annotated with genetic code 11) with genetic code 15 :  "TAG" * -> "Q"

prerequisites :

        Entrez Direct: E-utilities on the Unix Command Line https://www.ncbi.nlm.nih.gov/books/NBK179288/

        sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

        python,awk

setup: 
      add +x to scripts

      chmod u+x setup.sh
      ./setup.sh

use:

    ./scripts/ExtendDownStream.sh acc max_len  - selenoprotein
    ./scripts/ExtendDownStream15.sh acc max_len - phage protein

    acc - genbank protein accession
    max_len  - max number of AA will be added downstream,  try = 100..200..1000

    ./scripts/ExtendUpStream.sh  acc max_len - selenoprotein
    ./scripts/ExtendUpStream15.sh  acc max_len  - phage protein

    acc - genbank protein accession
    max_len  - max number of AA will be added upstream, try = 100..200..1000

test:

        cd tests 
         ./test.sh
        result will be in test.result

        NCBI Entrez Utilities (Eutils) requests can sometimes time out. 
        If this happens, simply re-run your script.

