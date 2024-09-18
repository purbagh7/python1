a=input("Net Imcome of Current Year: ")
b=input("Total Asset of Current Year: ")
c=input("Cash flow from operation: ")
d=input("Net Imcome of Previous Year: ")
e=input("Total Asset of Previous Year: ")
f=input("Long Term Debt of Current Year: ")
g=input("Long Term Debt of Previous Year: ")
h=input("Current Asset of Current Year: ")
i=input("Current Asset of previous Year: ")
j=input("Current Liability of current Year: ")
k=input("Current Liability of previous Year: ")
l=input("Sales of Current Year: ")
m=input("Sales of Previous Year: ")
n=input("Gross profit of Current Year: ")
o=input("Gross profit of Previous Year: ")
p=input("No of share declared in current year: ")
a=float(a)
b=float(b)
c=float(c)
d=float(d)
e=float(e)
f=float(f)
g=float(g)
h=float(h)
i=float(i)
j=float(j)
k=float(k)
l=float(l)
m=float(m)
n=float(n)
o=float(o)
p=float(p)
#ROA
ROA=(a/b)*100
R11=(": %.2f" % round(ROA))
R=str(R11)
R1=(R11+"%")
print("ROA OF CURRENT YEAR=", R1)
#CFO
CFO=(c/b)*100
CFO1=("{:.2f}".format(CFO))
C=str(CFO1)
C1=(C+"%")
print("CFO=",C1)
#D(ROA)
DROA=(d/e)*100
Dfina=(ROA-DROA)
Dfina1=("{:.2f}".format(Dfina))
Dfinal=str(Dfina1)
print("D(ROA)=",Dfinal)
#D(Leverage)
DLEV1=(f-g)
DLEV2=(b+e)/2
DLEV11=(DLEV1/DLEV2)
DLEV=("{:.2f}".format(DLEV11))
print("D(Leverage)=",DLEV)
#D(Liquidity)
CR1=(h-j)
CR2=(i-k)
DLC0=(CR1-CR2)
DLC=("{:.2f}".format(DLC0))
print("D(Liquidity)=", DLC)
#D(Gross Margin)
GR1=(n/l)
GR2=(o/m)
DG0=(GR1-GR2)
DG=("{:.2f}".format(DG0))
print("D(Gross Margin)=", DG)
#D(Turnover)
AT1=(l/DLEV2)
AT2=(m/DLEV2)
DTUE1=(AT1-AT2)
DTUE=("{:.2f}".format(DTUE1))
print("D(Turnover)=", DTUE)

if(ROA>=0):
    print("POINT 1")
else:
    print("POINT 0")

if(CFO>=0):
    print("POINT 1")
else:
    print("POINT 0")

if(CFO>ROA):
    print("POINT 1")
else:
    print("POINT 0")

if (Dfina>=0):
        print("POINT 1")
else:
        print("POINT 0")
if (DLEV11>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (p==int):
        print("POINT 0")
else:
        print("POINT 1")
if (DLC0>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (DG0>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (DTUE1>=0):
        print("POINT 1")
else:
        print("POINT 0")

Total=((ROA>=0)+(CFO>=0)+(CFO>ROA)+(Dfina>=0)+(DLEV11>=0)+(p==int)+(DLC0>=0)+(DG0>=0)+(DTUE1>=0))
print(Total)

if(Total==0,1,2,3):
    print("The company is experiencing financial challenges or operational issues.")
elif(Total==4,5,6):
    print("The company's performance is mixed; further investigation may be necessary.")
elif(Total==7,8,9):
    print("Indicates strong financial health and operational efficiency of the company")
else:
    print("error")