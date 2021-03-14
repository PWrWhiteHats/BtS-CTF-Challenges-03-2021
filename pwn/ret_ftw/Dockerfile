FROM ubuntu:20.04

RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
        ucspi-tcp \
        xinetd \
        gcc libc6-dev gcc-multilib \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  /etc/xinetd.d/*
RUN useradd -m ctf
WORKDIR /home/ctf
COPY ctf.xinetd /etc/xinetd.d/xinetd
COPY for_server.c chall.c
RUN gcc chall.c -o chall -no-pie -fno-stack-protector -z execstack

EXPOSE 4444

CMD ["/usr/sbin/xinetd", "-dontfork", "-stayalive"]
