# Solution here

This challenge have a lot of random pages, lot more than you can check manualy. 
You know only you need to pass certain header to one of them.

Solution is to write a spider (python + scrapy would be good choice) that recuresively goes through all links on website and sends header to them.

You could check basic spider doing so in [solution.py](solution.py) file

Usage is (change url to good one): 
```bash
pip3 install -r requirements.txt
python3 solution.py "http://localhost:30085" > result.txt
```
Then look for strings matching flag in file