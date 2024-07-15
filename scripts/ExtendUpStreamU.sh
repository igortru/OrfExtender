script_name=$0
script_full_path=$(dirname "$0")
temp_dir=$(mktemp -d)
AA="U"
L=$3
if [ -z "$L" ]
then
       L="2"
fi

$script_full_path/GenerateList.sh $1 0 $2 $L >$temp_dir/tmp
R=$(cat $temp_dir/tmp | egrep "TAA|TAG" | wc -l)

if [ "$R" -eq "0" ] 
then
        echo "no upstream stop codons"
        P="1"
else
    P=$(cat $temp_dir/tmp | sed '$d' | egrep "TAA|TAG" | tail -1 | awk  '{ printf "%d\n",$1; }')
    if [ -z "$P" ]
    then
        P=$2
    fi
fi
R=$(cat $temp_dir/tmp | tail -1 | awk  '{ printf "%d\n",$1; }')
$script_full_path/GenerateUp.sh $temp_dir/tmp $P $R $AA 
rm -rf $temp_dir
