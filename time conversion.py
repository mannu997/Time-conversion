import sys

time = raw_input().strip()

if time[8]=='P' and time[:2]!='12':
    time =time.replace(time[:2],str(int(time[:2])+12))
    print time[:8]
	
elif time[8]=='A' and time[:2]=='12':
    time= time.replace(time[:2],'00')
    print time[:8]
else :
    print time[:8]
    
    