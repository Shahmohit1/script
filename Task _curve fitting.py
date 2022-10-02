# Task4
a=[]
y=[]
x=[]
f = open('Velocity.csv');

for i in f:
    i = i.replace("\n","").split(",")
    #print(i)
    for j in i:
        if j.isdigit():
            #print(j)
            a.append(float(j))
            
f.close()    
print(a ) 
    
    
    
    
    
    
    
    
    
# for(int i=0;i<N;i++) {
#           Sx = Sx + x[i];
#           Sy = Sy + y[i];
#           Sxx = Sxx + x[i]*x[i];
#           Sxy = Sxy + x[i]*y[i];
#       }
#   printf("Sx : %lf \tSy : %lf \nSxx : %lf \tSxy : %lf\n", Sx, Sy, Sxx, Sxy);
#   //formula to find slope and intercept
#   delta = N*Sxx -Sx*Sx;
#   slope = (N*Sxy -Sx*Sy)/delta;
#   inter = (Sy*Sxx -Sx*Sxy)/delta;
