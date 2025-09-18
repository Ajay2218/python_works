


orders=["bms","bms","bms","ptm","ptm","ptm","wkn","wkn","wkn","bms","ptm","bms"]

bms_count = 0

ptm_count = 0

wkn_count = 0

for tic in orders:

    if tic == 'bms':
        
        bms_count += 1

    elif tic == 'ptm':

        ptm_count += 1
    
    elif tic == 'wkn':

        wkn_count += 1

print(orders)

print("bms count =",bms_count)

print("ptm count =",ptm_count)

print("wkn count =",wkn_count)

if bms_count > ptm_count and bms_count > wkn_count:

    print("bms count is largest")

elif ptm_count > bms_count and ptm_count > wkn_count:

    print("ptm count is largest")
    
else:

    print("wkn count is largest")

if bms_count < ptm_count and bms_count < wkn_count :

    print("bms count is lowest")
elif ptm_count < bms_count and ptm_count < wkn_count:

    print("ptm count is lowest")

else:

    print("wkn count is lowest")

total = bms_count + wkn_count + ptm_count

print("total ticket sold = ",total)