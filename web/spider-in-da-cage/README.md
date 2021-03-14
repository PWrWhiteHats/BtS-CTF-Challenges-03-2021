# Spider in da cage
Tony! 
I got IT, i finolly got IT... It's part of their config with a key. 
I am in thee hurry.. THEY would get to me soon, I am erasing the evidence, 
but THEY are clever bastards, we ain't have much time, until they would change it..

You must use this key fast, I didn't got time to see more, only this peace..
but I know for sure it opens one of cages in this goddamn labyrinth.

Enter it, but be carefull, all of them are connected, like a big network,
and you must be spider passing fast this network, but never falling for traps.
It would look tempting, like a short earned rest, but don't stop or you will be lost forever...

All you need is below:

------------------------------
if ($http_secure_auth = "t0p_S3cReT_k3y") {
        add_header Content-Type text/plain;

------------------------------

I got a faith in you, Earnie

## Flag

Check in [flag.txt](flag.txt) file

## How to run

```bash
# prod
docker build . -t spider-in-da-cage && docker run -p 30085:80 spider-in-da-cage

# development
docker build . -t spider-in-da-cage && docker run -p 30085:80 -v html:/usr/share/nginx/html  spider-in-da-cage

```

## Solution
Check in [SOLUTION.md](solution/SOLUTION.md) file



## Generate random gallery website:

Download files from google image 
```bash
python3 generators/download_google_images.py
```

Rename images to random names and delete backup files:
```bash
./generators/rename_files_to_random.sh html/images/
rm -rf html/images/*.backup
```

Generate HTML files from images:
```bash
./generators/generate_websites_for_dir.sh -f
```