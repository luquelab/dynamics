def model_fun(t,y,r,aB,c,aP,m):
	B = y[0]
	P = y[1]

	B_dot = +r*B -aB*B*P 
	P_dot = c*aP*B*P -m*P 
	
	y_dot = [B_dot ,P_dot ]
	return y_dot