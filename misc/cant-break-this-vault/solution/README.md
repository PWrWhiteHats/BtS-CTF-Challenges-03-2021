## SOLUTION

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