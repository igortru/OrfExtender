awk '{printf "echo %s;../scripts/ExtendDownStreamU.sh %s 200\n",$1,$1;}' ./test.set  | sh
