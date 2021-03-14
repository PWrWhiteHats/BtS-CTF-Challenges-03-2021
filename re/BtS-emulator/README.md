# BtS-emulator

I bet you can't crack BtS-emulator ;)

## Flag 

Check in [flag.txt](flag.txt) file 

## Preparing

ONLY BINARY `emulator` is available for the players, NO SOURCE CODE.

Server side:
```
docker build -t bts-emulator . && docker run -p 27440:27440 bts-emulator:latest
```

## Connect to server

```
nc CHALL_URL 27440
```


## How to compile:

```
g++ -std=c++2a emulator.cpp -o emulator
```

```
sudo apt install libseccomp-dev
g++ -std=c++2a eumlator_for_server.cpp -o emulator_for_server -lseccomp
```

## Solution 

Check in [README.md](solution/README.md) file


