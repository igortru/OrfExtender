{
	if (index($1,">") == 1) 
	{
		if (NR > 1) printf "\n"; 
		printf "%s\n",$0;
	}  
	else if ($1 <= P) 
	{ 
		if ($3 == "*") 
			printf "%s",R; 
		else 
			printf "%s",$3; 
	} 
} 
END {
	printf "\n";
}
