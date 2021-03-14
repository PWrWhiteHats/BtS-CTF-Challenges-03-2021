#!/bin/sh
while(true); do
tcpserver -t 50 -RHl0 0.0.0.0 27440 /home/ctf/for_server
done
