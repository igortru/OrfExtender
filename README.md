prerequisites

https://www.ncbi.nlm.nih.gov/books/NBK179288/

sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

python


use:

./scripts/ExtendDownStream.sh <acc> <len> <letter> <count>
./scripts/ExtendUpStream.sh  <acc> <len> <letter> <count>

test:
  awk '{printf "echo %s;./scripts/ExtendDownStream.sh %s 200 U\n",$1,$1;}' ./tests/test.set  | sh

