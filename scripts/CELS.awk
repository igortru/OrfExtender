{
	if ($4 == "+") 
        {
		X = $2-SUB*3;
		printf "%s\t%d\t%d\t %s\t11\n",$1,X,$3+ADD*3,P; 
	}
	else 
	{
		Y = $2-ADD*3;
		printf "%s\t%d\t%d\t %s\t11\n",$1,$3+SUB*3,Y,P;
	}
}
