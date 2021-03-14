# Can't break this vault

_Author: [TheArqsz](https://github.com/TheArqsz)

Holy truck, those hackers locked out all my dogecoins in this password-protected vault. Help me Pla-Yer. You're my only hope.

## Flag

```
BtS-CTF{VGVsbCBtZSBob3cgeW91IGdvdCBpdC4gRGlkIHlvdSBkZWJ1ZyBpdCBvciBkaWQgeW91IGp1c3QgcmVhZCB0aGUgZmxhZyBmcm9tIHdhc20gZmlsZT8gSSBhbSBraW5kYSBjdXJpb3VzLiAvQXJxc3ou}
```

## How to run - locally

To set up this challenge locally you need to have [emsdk](https://github.com/emscripten-core/emsdk) and python 3.6.

1. Install requirements:
```
pip install -r requirements
```
2. Change flag in `generate_challenge.py`

3. Run generator:
```bash
python3 generate_challenge.py
```

You will be prompted with password to "get a flag".

4. Run:
```bash
emcc challenge/challenge.c -s WASM=1 -o challenge/static/js/module.js  -s NO_EXIT_RUNTIME=1  -s EXPORTED_FUNCTIONS="['_calculate']" -s "EXTRA_EXPORTED_RUNTIME_METHODS=['cwrap']"
```

5. Run app:
```
cd challenge && gunicorn -c gunicorn.py app
```

## How to run - Docker container

To set up this challenge in container you need to have [emsdk](https://github.com/emscripten-core/emsdk), python3 and Docker.

1. Change flag in `generate_challenge.py`

2. Run generator:
```bash
python3 generate_challenge.py
```

3. Run:
```bash
emcc challenge/challenge.c -s WASM=1 -o challenge/static/js/module.js  -s NO_EXIT_RUNTIME=1  -s EXPORTED_FUNCTIONS="['_calculate']" -s "EXTRA_EXPORTED_RUNTIME_METHODS=['cwrap']"
```

4. Run:
```bash
docker build -t imagename .
```

## How to run - only with examples

```bash
cp examples/* challenge/static/js/ 
```
And now run gunicorn or build docker image.

## Solution

Check in [solution folder](./solution/README.md)



