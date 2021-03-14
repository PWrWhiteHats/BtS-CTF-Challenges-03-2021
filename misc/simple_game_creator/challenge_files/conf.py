try:
    with open('/app/flag.txt', 'r') as r:
        flag = r.read().strip()
except FileNotFoundError:
    flag = "temp{temp_flag}"