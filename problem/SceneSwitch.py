"""psit"""
def switch(time, temp, ans):
    """sad psit"""
    while time != "End":
        time1 = float(time)
        if time == "0":
            light, status = "cool", "on"
        elif status == "on":
            temp = time1+6
            status = "off"
        elif status == "off" and light == "cool":
            if time1 <= temp:
                ans += 1
                status, light = "on", "warm"
            else:
                status, light = "on", "cool"
        elif status == "off" and light == "warm":
            status, light = "on", "cool"
        time = input()
    print(ans)
switch(input(), 0, 0)
