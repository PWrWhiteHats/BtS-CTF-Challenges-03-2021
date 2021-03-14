FROM python:2-slim as app
RUN apt-get update \
    && apt-get install xinetd ucspi-tcp -y \
    && apt-get clean
RUN useradd -m ctf
WORKDIR /home/ctf
COPY challenge_files/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./challenge_files/ /home/ctf
RUN chmod a+x /home/ctf/run.py

RUN mkdir /app && chown -R ctf:ctf /app
COPY flag.txt /app/flag.txt

COPY ctf.xinetd /etc/xinetd.d/xinetd
EXPOSE 4444
CMD ["/usr/sbin/xinetd", "-dontfork", "-stayalive"]