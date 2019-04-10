#!/usr/bin/env python3

import rethinkdb

r =rethinkdb.RethinkDB()

conn = r.connect('172.17.0.2', 28015).repl()

res=r.db('test').table('t1').changes().run()

for i in res:
    print(i)