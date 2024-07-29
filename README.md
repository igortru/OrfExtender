Given a GenBank protein accession, if it's linked to the nucleotide sequence where the protein was annotated, tool can extend corresponding the open reading frame (ORF) upstream or downstream to search for alternative stop codons and provide extended protein sequence.
This allows for easier validation of annotated GenBank proteins suspected to have premature stop codons

use-cases:

        selenoproteins : replace  "TGA" * -> "U"
        proteins (mostly phages, annotated with genetic code 11) with genetic code 15 :  "TAG" * -> "Q"
        proteins (mostly phages, annotated with genetic code 11) with genetic code 4 :   "TGA" * -> "W"
        proteins check alternative start upstream 

prerequisites :

        Entrez Direct: E-utilities on the Unix Command Line https://www.ncbi.nlm.nih.gov/books/NBK179288/

        sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

        python,awk

setup: 
      add +x to scripts

      chmod u+x setup.sh
      ./setup.sh

use:
    efetch -db ipg -id acc
    report nucleotide accession with location where protein found

    ./scripts/ExtendDownStreamU.sh acc max_len ipgrow  - selenoprotein
    ./scripts/ExtendDownStream15.sh acc max_len ipgrow  - phage protein
    ./scripts/ExtendDownStream4.sh acc max_len ipgrow - phage protein

    acc - genbank protein accession
    max_len  - max number of AA will be added downstream,  try = 100..200..1000

    ./scripts/ExtendUpStream.sh  acc max_len ipgrow - move protein start upstream until stop codon 
    ./scripts/ExtendUpStreamU.sh  acc max_len ipgrow - selenoprotein
    ./scripts/ExtendUpStream15.sh  acc max_len ipgrow - phage protein
    ./scripts/ExtendUpStream4.sh  acc max_len  ipgrow - phage protein

    acc - genbank protein accession
    max_len  - max number of AA will be added upstream, try = 100..200..1000
    ipgrow = row number from ipg report , default = 2

test:

	1)
	taken from
	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10769273/
	"Predicting stop codon reassignment improves functional annotation of bacteriophages"
	MG676224	Aeromonas phage AhSzq-1 Shenzhenvirus Demerecviridae


        ./scripts/ExtendUpStream15.sh   AVR76017 300

	original sequence
	efetch -id AVR76017 -format fasta -db protein

	2)
        cd tests 
         ./test.sh
        result will be in test.result

        NCBI Entrez Utilities (Eutils) requests can sometimes time out. 
        If this happens, simply re-run your script.

