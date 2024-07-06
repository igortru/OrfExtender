script_name=$0
script_full_path=$(dirname "$0")

cat $1 | awk -v P=$2 -v S=$3 -v R=$4 -f $script_full_path/CELG.awk

