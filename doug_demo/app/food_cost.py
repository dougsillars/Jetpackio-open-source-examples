import asyncio
import math
from typing import Tuple
from jetpack import function


@function
async def food_cost(n: int) -> int:
    #n is number of travel days
    #per_diem is the allowed expencse for food
    per_diem = 60
    total_food_cost = per_diem*n
    print(f'the estimated food cost is {total_food_cost} dollars')
    return total_food_cost