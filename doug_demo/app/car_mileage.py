import asyncio
import math
from typing import Tuple
from jetpack import function


@function
async def car_mileage(n: int) -> int:
    #in 2021 the federal reimbursement is $0.56/mile
    # keep it all simple so we'll round up to a dollar
    miles = float(n)
    fed_rate = 0.56
    reimburse = math.ceil(miles*fed_rate)
    print(f'the estimated mileage cost is {reimburse} dollars')
    return reimburse
