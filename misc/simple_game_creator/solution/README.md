## SOLUTION

What interests us is this piece of code
```python2
def show_details(self):
    print('{0.players} can play this easy game called ' + self.name).format(self)
```

We have to overwrite `self.name` using specific syntax `{}` passed to name of multiplayer game.

`{0.__init__.__globals__}` gives us a lot of data which contains our flag