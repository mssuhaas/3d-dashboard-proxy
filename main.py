import requests
import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

OM2M_ORIGIN=os.getenv('OM2M_ORIGIN')

base_url = "http://onem2m.iiit.ac.in:443/"
headers = {
  "X-M2M-Origin": OM2M_ORIGIN,
  "Content-Type": "application/json"
  }

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/{path:path}')
async def proxy_pass(path:str):
    final_url = base_url + path
    payload = ""
    response = requests.request("GET",url=final_url,headers=headers,data=payload)
    print(response.text)
    return json.loads(response.text)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
