import asyncio
from typing import Dict, List
from starlette.responses import HTMLResponse
from coin_toss import flip_coin
from fibonacci import fibonacci
from error_job import error_thrower
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
#      A
#    /  \
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