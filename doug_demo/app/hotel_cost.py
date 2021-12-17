import asyncio
import math
from typing import Tuple
from jetpack import function


@function
async def hotel_cost(n: int) -> int:
    #n is number of travel days
    #n-1 is days in hotel - as last day of travel is home to your bed
    #hotel_cost is average night in hotel
    nightly_hotel_cost = 200
    total_hotel_cost = nightly_hotel_cost*(n-1)
    print(f'the estimated hotel cost is {total_hotel_cost} dollars')
    return total_hotel_cost