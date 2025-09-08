* an example of regression with group dummies: 
clear 


sysuse citytemp
tab region 

reg tempjuly ibn.region, robust  // West as base 

reg tempjuly ibn.region, robust nocons  
