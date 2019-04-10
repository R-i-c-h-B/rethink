#!/usr/bin/env python3

import rethinkdb
import time

r =rethinkdb.RethinkDB()

conn = r.connect('172.17.0.2', 28015).repl()

res=r.db('test').table('t1')

res.insert({'key': 2}).run()


import time

tend = time.time() + 5

while time.time() < tend:
    time.sleep(1) # sleep for 250 milliseconds
    print(tend - time.time())
    res.filter({'key': 2 }).update({'val': 'ok', 'time': time.time()}).run()

