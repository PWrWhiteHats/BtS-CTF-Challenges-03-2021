# Can't break this vault

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

Kinda easy challenge if you know what to look for.

1. Looking at the source files in the browser

2. What interests us is a `module.wasm` file. Download it.

3. Now, you can use tool called `wabt` - e.g. as a Docker image from [here](https://hub.docker.com/r/thearqsz/wabt)

```bash
docker pull thearqsz/wabt
```

4. Run command:
```bash
docker run -it --rm -v $(pwd):/src -u  $(id -u):$(id -g) thearqsz/wabt wasm-decompile module.wasm -o wasm.js
```

5. Look inside the `wasm.js` file - do you see something in the first variable?

