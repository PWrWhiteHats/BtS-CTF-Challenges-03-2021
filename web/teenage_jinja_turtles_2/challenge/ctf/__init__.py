
class Flag(object):
    def get_____flag():
        try:
            with open('/app/flag.txt', 'r') as r:
                return r.read().strip()
        except FileNotFoundError:
            return "temp{temp_flag}"

