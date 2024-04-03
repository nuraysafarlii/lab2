#24
#0;24) intervalında dəyişən n sayda təsadüfi tam ədəddən ibarət siyahının(massivin) 
#cüt indeksli elementlərinin cəmini hesablayan alqoritm tərtib etməli

import random
N=int(input("siyahinin element sayini daxil edin: "))
random_list=random.sample(range(0,24),N)
cem=0
for R in random_list:
    if random_list.index(R)%2==0 and random_list.index(R)!=0:
        cem+=R
print(cem)

