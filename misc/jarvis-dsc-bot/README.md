# Jarvis Discord bot

Do you know Jarvis? Mr. Stark's assistant? I am sure you do. During our CTF you can talk with him. Who knows, maybe he will share one of his master's secrets?

## How to install

1. Build Docker image 
```bash
docker build -t jarvis .
```

2. Create application and bot at https://discord.com/developers

3. Collect bot token from https://discord.com/developers

4. Run Docker image
```bash
docker run -it -e DISCORD_TOKEN=REDACTED -e FLAG=tmp{flag} jarvisdsc
```

## How to solve 

Check in [solution folder](./solution/README.md)
