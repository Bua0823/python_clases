import math;

t1=291;
t2=298.5;
R1=589.12;
R2=453.02;
B=(math.log(R1)-math.log(R2))/(1/t1-1/t2)
A=R1*math.e**(-B/t1)