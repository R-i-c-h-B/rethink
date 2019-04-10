# rethink

A simple demo of 2 python3 scripts that connect to your rethinkdb.
rethink.py creates a change listener that prints changes to a named table to the screen.
rethinkupdate.py runs a timed loop that updates the records for a given key in the same table.

As of writing, the code expects the rethinkdb to be at the given ip address and port.
NB: You need to get the reql_port if you want to connect via reql - ie in code.
- you can verify that in teh rethink web ui by running:
  - r.db('rethinkdb').table('server_status')
 
Code currently looks for: 
  - Database: test 
  - table: t1
  
In rethinkdb webui that would equate to:
  - r.db('test').table('t1')
  
  
