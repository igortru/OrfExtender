(./scripts/ExtendUpStream15.sh $1 1000; ./scripts/ExtendDownStream15.sh $1 1000; efetch -id $1 -db protein -format fasta) >tmp.tmp
python ./scripts/color_prot.py tmp.tmp
cat tmp.tmp >>result.prot
 
