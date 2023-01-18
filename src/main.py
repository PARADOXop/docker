from fastapi import FastAPI
import debugpy

import redis

r = redis.Redis(host="redis123", port=6379)

app = FastAPI()

debugpy.listen({"0.0.0.0"}, 5678)
# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    print('hii')
    return {"Hello": "my name is khan " "World my age is 22 "}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}