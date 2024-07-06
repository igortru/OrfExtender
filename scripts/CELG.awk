{
	if (index($1,">") == 1) 
	{
		if (NR > 1) 
			printf "%s\n",substr(SS,1,length(SS)-1); 
		printf "%s\n",$0; 
		SS = ""; 
		F = 0;
	}  
	else if ($1 > P) 
	{ 
			if ($2 == "ATG" || $2 == "TTG" || $2 == "GTG") 
				F = 1; 
			if (F == 1) 
			{ 
				if (SS == "")
					SS = "M"
				else
				{
					if ($3 != "*") 
						SS = SS $3; 
					else 
						SS = SS R;
				}
			} 
	} 
} 
END {
	printf "%s\n",substr(SS,1,length(SS)-1);
}

