n=9;
j=10;

dmin=0;
dmax=0;
tmax=0;

for l=1:n,
    a(l)=rand(1);
end

sa=(a-0.5)*2

% Вивід графіків часових залежностей а1-a8 
for i=1:j,    
    ki(i)=i;
    for l=1:n,
    aa(l,i)=sa(l);
    end
end   

subplot(2,1,1), plot(ki,aa(1,:),'ko-')
hold on;
subplot(2,1,1), plot(ki,aa(2,:),'rh-')
hold on;
subplot(2,1,1), plot(ki,aa(3,:),'b<-')

hold on;
subplot(2,1,1), plot(ki,aa(4,:),'m^-')
hold on;
subplot(2,1,1), plot(ki,aa(5,:),'gv-')
hold on;
subplot(2,1,1), plot(ki,aa(6,:),'kp-')

hold on;
subplot(2,1,1), plot(ki,aa(7,:),'cd-')
hold on;
subplot(2,1,1), plot(ki,aa(8,:),'rx-')
hold on;
subplot(2,1,1), plot(ki,aa(9,:),'b*-')

axis([1 j -1 1])
legend('a_1','a_2','a_3','a_4','a_5','a_6','a_7','a_8','a_9')
xlabel('Number of iteration l')
ylabel('Trajectories a_1 to a_9')

grid
       
x(1)=0.5;
alfa(1)=0.6; 

for k=1:n;
    
    tic

for i=1:j,
    
    ki(i)=i;
    
    for l=1:n,
       if (a(l)-x(i))>0
        s(l)=1;
       else
        s(l)=0;
       end
    end              
      
    if k==1
     d(i)=a*s';
     s1(i,:)=s;
     
    elseif k==2
     d(i)=a*(s'-s1(i,:)'); 
     s2(i,:)=s;
     
     elseif k==3
     d(i)=a*(s'-s2(i,:)'); 
     s3(i,:)=s;   
     
     elseif k==4
     d(i)=a*(s'-s3(i,:)'); 
     s4(i,:)=s;    
     
      elseif k==5
     d(i)=a*(s'-s4(i,:)'); 
     s5(i,:)=s;  
     
      elseif k==6
     d(i)=a*(s'-s5(i,:)'); 
     s6(i,:)=s;  
     
      elseif k==7
     d(i)=a*(s'-s6(i,:)'); 
     s7(i,:)=s;  
     
      elseif k==8
     d(i)=a*(s'-s7(i,:)'); 
     s8(i,:)=s;  
     
      elseif k==9
          s=[1 1 1 1 1 1 1 1 1];
     d(i)=a*(s'-s8(i,:)'); 
     s9(i,:)=s;      
     
    end         
    
       ss=0;
       for l=1:n,       
        ss=ss+s(l);    
       end
      
    e=ss-k;   
       
    if e>0
        miu(i)=1;  
    elseif e<0
        miu(i)=-1;  
    else
        miu(i)=0;
    end   
  
    x(i+1)=x(i)+miu(i)*alfa(i); 
    alfa(i+1)=alfa(i)*alfa(1);
    
end

%toc

if toc*7/10>tmax
   tmax=toc*7/10; 
end

d=(d-0.5)*2;

for kk=1:n,  
if d(kk)>dmax
    dmax=d(kk);
end
if d(kk)<dmin
    dmin=d(kk);
end
end

if k==1
subplot(2,1,2),plot (ki,d,'ko-')
elseif k==2
    hold on;
subplot(2,1,2),plot (ki,d,'rh-')
hold on;
elseif k==3
    hold on;
subplot(2,1,2),plot (ki,d,'b<-')
elseif k==4
    hold on;
subplot(2,1,2),plot (ki,d,'m^-')
elseif k==5
    hold on;
subplot(2,1,2),plot (ki,d,'gv-')
elseif k==6
    hold on;
subplot(2,1,2),plot (ki,d,'kp-')
elseif k==7
    hold on;
subplot(2,1,2),plot (ki,d,'cd-')
elseif k==8
    hold on;
subplot(2,1,2),plot (ki,d,'rx-')
elseif k==9
    hold on;
subplot(2,1,2),plot (ki,d,'b*-')
end

end

tmax=tmax

axis([1 j dmin dmax])
legend('d_1','d_2','d_3','d_4','d_5','d_6','d_7','d_8','d_9')
xlabel('Number of iteration l')
ylabel('Trajectories d_1 to d_9')

dmin=dmin;
dmax=dmax;

grid
clear all;



























