{
	printf ">";
	for (i = 1; i <= NF - 2; i++) 
	{ 
		if (i > 1) 
			printf "|"; 
		printf "%s",$i; 
	} 
	printf "\n";
	for (i = 1; i <= length($(NF-1)); i++) 
		printf "%4d %s %s\n",i,substr($NF,3*i-2,3),substr($(NF-1),i,1); 
}
