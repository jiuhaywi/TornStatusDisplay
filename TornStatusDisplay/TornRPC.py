from pypresence import Presence
import time
import requests
import math


from creds import client_id, user_id, api_key
RPC = Presence(client_id)
tmp = 0
flying = None
time_left = 0
life = 0


def UpdateFlying(Location, Time, Depart):
    Hours = math.floor(Time/3600)
    Minutes = int(math.floor((Time/60)-(Hours*60)))
    Seconds = int(math.floor((Time)-(Hours*3600))-(Minutes*60))
    if Location == "Torn":
        RPC.update(
            details="Flying back to Torn City!",
            state="Time left: "+str(Hours)+"h "+str(Minutes)+"m "+str(Seconds)+"s.",
            start=time.time() - (int(time.time()) - Depart),
            end=time.time() + Time,
            large_image="plane-to-left",
            large_text="Torn City"
            )
    else:
        RPC.update(
            details="Flying to "+Location+"!",
            state="Time left: "+str(Hours)+"h "+str(Minutes)+"m "+str(Seconds)+"s.",
            start=time.time() - (int(time.time()) - Depart),
            end=time.time() + Time,
            large_image="plane-to-right",
            large_text=Location
            )
            
    
def UpdateNotFlying(Location, Status):
    Location2 = Location[:6]
    if Location == "United Kingdom":
        Location2 = "UnitedK"
    if Location == "South Africa":
        Location2 == "South"
    if Location == "Torn":
        RPC.update(
            details="In Torn City!",
            state="Is currently "+Status+".",
            large_image="torn-city",
            large_text="Torn City"
            )
    else:   
        
        RPC.update(
            details="Abroad, in "+Location+"!",
            state="Is currently "+Status+".",
            large_image=Location2,
            large_text=Location
            )


def GetInfo():
    url = f"https://api.torn.com/user/{user_id}?selections=travel,basic&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("GET request failed:", response.status_code)
        print(response.text)
        return None
    destination = data["travel"]["destination"]
    time_left = int(data["travel"]["time_left"])
    departed = int(data["travel"]["departed"])
    timestamp = int(data["travel"]["timestamp"])
    status = data["basic"]["status"]["state"]
    return destination, time_left, departed, timestamp, status


def Update():
    global flying, time_left, destination, departed, life
    destination, time_left, departed, timestamp, life = GetInfo()
    
    print(destination, time_left, departed, timestamp)
    if time_left == 0:
        flying = False
        UpdateNotFlying(destination, life)
    else:
        flying = True
        UpdateFlying(destination, time_left, departed)




RPC.connect()
Update()
while True:
    time.sleep(5)
    tmp = tmp+5
    
    if flying == True:
        time_left -= 5
        UpdateFlying(destination, time_left, departed)
        if tmp >= 300:
            Update()
            tmp = 0

    else:
        if tmp >= 60:
            Update()
            tmp = 0

    
