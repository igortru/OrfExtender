script_name=$0
script_full_path=$(dirname "$0")
temp_dir=$(mktemp -d)
L=$4
if [ -z "$L" ]
then
       L="2"
fi

$script_full_path/GenerateList.sh $1 0 $2 $L >$temp_dir/tmp
R=$(cat $temp_dir/tmp | egrep "TAA|TGA" | wc -l)

if [ "$R" -eq "0" ] 
then
        echo "no upstream stop codons"
        P="1"
else
    P=$(head -n $(wc -l < $temp_dir/tmp) $temp_dir/tmp | tail -n +1 | egrep "TAA|TGA" | tail -1 | awk  '{ printf "%d\n",$1; }')
fi
R=$(cat $temp_dir/tmp | tail -1 | awk  '{ printf "%d\n",$1; }')
$script_full_path/GenerateUp.sh $temp_dir/tmp $P $R $3
rm -rf $temp_dir