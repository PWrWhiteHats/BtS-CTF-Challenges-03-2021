## SOLUTION
This challenge is based on two topics:

- Least Significant Bit
- SSTV Signal specification

1. We need to extract LSB from [challenge.wav](challenge.wav) file. Example can be found in file [decode.py](decode.py)
2. When we've got out LSBs we need to save them as file - more specifically wave file
3. This wave file is recorded [SSTV signal](https://www.sigidwiki.com/wiki/Slow-Scan_Television_(SSTV)) in Robot36 mode - to decode it use tools like [this](http://users.belgacom.net/hamradio/rxsstv.htm)