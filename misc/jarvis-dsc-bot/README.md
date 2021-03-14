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

1. Copy bot ID from Discord

2. Add bot to your own personal server using [dedicated URL](https://discord.com/oauth2/authorize?client_id=817825973789261844&scope=bot) 
```
https://discord.com/oauth2/authorize?client_id=COPIED_ID&scope=bot
```

3. On your server, create role called `Mr.Stark`

4. After assigning yourself to this command, execute command `!!secret`