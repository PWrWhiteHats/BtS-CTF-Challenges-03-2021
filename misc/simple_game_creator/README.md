# Simple game creator

Recently we had to postpone our biggest game for the 6th time...what a shame.
To calm down people who bought preorders we created this app. It will let us collect users' ideas for games and maybe...maybe we will use it in the future (somewhere around 2077, cause who knows how many postpones are waiting for us)

## Challenge

Flag is stored in `conf.py` file - simply edit it to change flag.
Build an image and run it:
```docker
docker run -it --restart unless-stopped -p4444:4444 -d <image_name>
```

Challenge can be accessed:
```sh
nc <ip> 9999
```

## Solution
What interests us is this piece of code
```python2
def show_details(self):
    print('{0.players} can play this easy game called ' + self.name).format(self)
```

We have to overwrite `self.name` using specific syntax `{}` passed to name of multiplayer game.

`{0.__init__.__globals__}` gives us a lot of data which contains our flag