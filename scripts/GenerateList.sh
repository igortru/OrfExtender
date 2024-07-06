script_name=$0
script_full_path=$(dirname "$0")
temp_dir=$(mktemp -d)

echo $1 | efetch -db ipg |  cut -f 3-6 | sed -n ''$4'p' | awk -v ADD=$2 -v P="$P" -v SUB=$3 -f $script_full_path/CELS.awk >$temp_dir/tmp
python $script_full_path/IdScan.py <$temp_dir/tmp | awk -F'|' -f $script_full_path/CELS2.awk
rm -rf $temp_dir 

