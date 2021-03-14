# Smells like nice challenge

It is now year 2077 and all those 36 Robots that are left, are dancing to old hits. 
All least significant units were destroyed during the Purge.
Wake up soldier, we've got challenge to solve.

## Flag

```python
BtS-CTF{THAT_IS_4_9r34T_94m3}
```

## How to run

To set up this challenge locally you need to:

1. Use following command:
```bash
pip install -r requirements.txt
```
2. Specify flag in [challenge.env](challenge.env) file:
```python
FLAG="fake{fl4gs_4r3_l0ng_or_sH0r7}"
```
3. Make sure that:
   
    - `challenge.env` file is present in [resources](resources/challenge.env) folder
    - `comic.ttf` file is present in [resources](resources/comic.ttf) folder
    - `nirvana.wav` file is present in [resources](resources/nirvana.wav) folder

4. Use following command:
```bash
cd files && \
python generate_image.py && \
python -m pysstv --mode Robot36 flag.png flag.wav && \
python generate_challenge.py
```

or 

```bash
chmod +x generate.sh
./generate.sh
```

5. `challenge.wav` file will be generated in root folder - provide it to contestants

## How to solve

This challenge is based on two topics:

- Least Significant Bit
- SSTV Signal specification

1. We need to extract LSB from [challenge.wav](challenge.wav) file. Example can be found in file [decode.py](decode.py)
2. When we've got out LSBs we need to save them as file - more specifically wave file
3. This wave file is recorded [SSTV signal](https://www.sigidwiki.com/wiki/Slow-Scan_Television_(SSTV)) in Robot36 mode - to decode it use tools like [this](http://users.belgacom.net/hamradio/rxsstv.htm)