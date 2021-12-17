import asyncio
from typing import Dict, List
from starlette.responses import HTMLResponse
from coin_toss import flip_coin
from fibonacci import fibonacci
from error_job import error_thrower
from create_trip import create_trip
from travel_days import travel_days
from hotel_cost import hotel_cost
from food_cost import food_cost
from car_mileage import car_mileage
from fastapi import FastAPI, Response


app = FastAPI()

class TestError(Exception):
    def __init__(self, message):
        self.message = message


@app.get("/")
async def ready() -> Response:
    return Response(status_code=200)

# Diamond Example:#

###################
#     A
#   /   \
#  B     C
#   \   /
#     D
################
# localhost:8080/diamond
@app.get("/diamond")
async def diamond() -> Dict[str, List[str]]:
    results: List[str] = []
    results += [await flip_coin("A")]

    if results[0] == "heads":
        jobs = [
            flip_coin("B-Head"),
            flip_coin("C-Head")
        ]
    else:
        jobs = [
            flip_coin("B-Tails"),
            flip_coin("C-Tails")
        ]
    
    results += await asyncio.gather(*jobs)

    results += [await flip_coin("D")]

    return {"results": results}


@app.get("/fibonacci/{n}")
async def fib(n: int) -> int:
    result = await fibonacci(n)
    print(result)
    return result






@app.get("/error")
async def error():
    try:
        await error_thrower()
    except Exception as err:
        content=f"""
        <h1> {type(err).__name__} </h1>
        <p> {err} </p>
        """
        return HTMLResponse(content=content, status_code=500)


# double Diamond Example:#

################
#     A
#   /   \
#  B     C
#  |    / \
#   \  D   E 
#    \ |  /
#      F 
################
# localhost:8080/trip
@app.get("/trip")
async def trip() -> Dict[str, List[str]]:
    results = []
    total_cost = 0
    mileage = await create_trip()

    #first jobs are to get the car mileage cost and the number of days
    #jobs1 = [
    #     car_mileage(mileage),
    #     travel_days(mileage)
    #
    #get car cost
    mileage_cost= await car_mileage(mileage)
    #get days
    number_of_days = await travel_days(mileage)
    #get the hotel and food caost from number of days
    hotel = await hotel_cost(number_of_days)
    food =  await food_cost(number_of_days)
        
    total_cost = mileage_cost +hotel +food
    print(f'the estimated total cost is {total_cost} dollars')
    return { "miles":mileage,
            "driving cost": mileage_cost,
            "days": number_of_days,
            "hotel cost": hotel,
            "food cost": food,
            "total": total_cost}
