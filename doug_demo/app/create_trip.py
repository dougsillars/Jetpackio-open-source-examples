import random
import time
from jetpack import function

# Diamond Example:#

################
#     A
#   /   \
#  B     C
#   \   /
#     D
################


@function
async def create_trip() -> int:
    #each trip will be between 300 and 1400 miles
    trip_length =  random.randint(300, 1400) 
    
    print(f'trip is {trip_length} miles long')
    time.sleep(1)
    return trip_length
