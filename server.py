from random import randrange
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()


@app.get("/get_count")
async def count():
    k = randrange(1, 1000)
    l = 85
    n = 0
    if k < k + n:
        return {"count": 1}
    n += l
    l = 150
    if k < l + n:
        return {"count": 2}
    n += l

    l = 95
    if k < l + n:
        return {"count": 3}
    n += l

    l = 65
    if k < l + n:
        return {"count": 4}
    n += l

    l = 85
    if k < l + n:
        return {"count": 5}
    n += l

    l = 105
    if k < l + n:
        return {"count": 6}
    n += l

    l = 70
    if k < l + n:
        return {"count": 7}
    n += l

    l = 80
    if k < l + n:
        return {"count": 8}
    n += l

    l = 55
    if k < l + n:
        return {"count": 9}
    n += l

    i = 10
    l = 50
    while k >= l + n:
        i += 1
        n += l
    return {"count": i}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
