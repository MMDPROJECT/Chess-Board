import json
import socket

import sys
import os

sys.path.append(os.getcwd() + "/Database")
from Database import query

query_obj = query.Query()
s = socket.socket()

port = 9999

s.bind(("", port))

s.listen(1)

c, addr = s.accept()
print(f"client with address: {addr} connected")

try:
    c.send((json.dump(query_obj.get_all_scores())).encode())
    json_str = c.recv(2048).decode()
    query_obj.ins_score(json_str)
finally:
    c.close()
    s.close()
