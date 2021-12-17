import asyncio
import math
from typing import Tuple
from jetpack import function


@function
async def travel_days(n: int) -> int:
    #n is number of miles
    # max travel is 320 miles per day
    miles_per_day = 320
    days_of_travel = math.ceil(n/320)
    print(f'trip will take {days_of_travel} days')
    return days_of_travel