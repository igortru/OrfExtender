{
	if ($4 == "+") 
		printf "%s\t%d\t%d\t %s\t11\n",$1,$2-SUB*3,$3+ADD*3,P; 
	else 
		printf "%s\t%d\t%d\t %s\t11\n",$1,$3+SUB*3,$2-ADD*3,P;
}
