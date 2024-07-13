script_name=$0
script_full_path=$(dirname "$0")
temp_dir=$(mktemp -d)

AA="U"
L=$3
if [ -z "$L" ]
then
       L="2" 
fi
$script_full_path/GenerateList.sh $1 $2 0 $L >$temp_dir/tmp
P=$(cat $temp_dir/tmp | grep "*" | awk '{if ($2 != "TGA") { printf "%d\n",$1; exit;} }')
if [ -z "$P" ] 
then
        echo "non-TGA stop codon missing\nadd downstream length" 
	P=$(cat $temp_dir/tmp | wc -l)
fi
$script_full_path/GenerateDown.sh $temp_dir/tmp $P $AA
rm -rf $temp_dir
