string A;
if(A.length() > 0)
{
	int i = 0;
	while(i < A.length())
	{
		if(!isalnumA[i])
		{
			A.erase(i,1);
		}
		else
		{
			i++;
		}
		for(int i = 0; i < A.length(); i++)
		{
			in j = A.length()-1-i;
			if(tolower(A[i] )!= tolower(A[j]))
			{
				return false;
			}
		}
	}
	print(True)
}
