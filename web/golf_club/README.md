## Description

Our leaderboard shows the results of the last golf tournament. Some of the players want to be anonymous, so the table only show their score. Anonymous player should receive specian link to access their profile in email message.



## Flag format
Look at id - HTTP GET parameter and try to enumerate it to find a flag.

BtS-CTF{do_you_like_stroke_or_match_play}


## RUN

docker run -p 80:80 IMAGE_NAME
docker exec -u 0 CONTAINER_NAME bash -c "/usr/sbin/apachectl -D FOREGROUND"

## SOLUTION

Check in [solution folder](./solution/README.md)

