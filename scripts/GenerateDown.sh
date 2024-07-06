script_name=$0
script_full_path=$(dirname "$0")

cat $1 | awk -v P=$2 -v R=$3 -f $script_full_path/CELF.awk
