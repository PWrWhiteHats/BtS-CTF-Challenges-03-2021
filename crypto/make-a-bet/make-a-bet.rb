#!/usr/bin/ruby
require 'socket'
require './resources.rb'
require './games.rb'

def start_server port
    incom_tcp = TCPServer.open port
    puts "accepting connections on port #{port}".lolcol
    loop do
        client_tcpsock = incom_tcp.accept
        puts "got connection from #{client_tcpsock.peeraddr(:numeric)[3]}".lolcol

        fork do
            begin
                handle_client client_tcpsock
                client_tcpsock.shutdown
                puts "finished connection with #{client_tcpsock.peeraddr(:numeric)[3]}".lolcol
            rescue 
                puts "Connection lost!"
            end
        end
    end
end

def handle_client socket
    socket.print $strings[:welcome]
    
    resp = socket.gets.chomp
    if resp == 'n'
        socket.puts $strings[:notaccepted]
        return
    end
    if resp != 'y'
        socket.puts $strings[:notunderstood]
        return
    end

    socket.puts $strings[:challengeaccepted]

    sleep 1

    challenges_won=0
    begin
        if play_coin socket
            challenges_won += 1   
            socket.puts ("+="*12)+"+"
        else
            return
        end

        # return unless play_dice socket
        # socket.puts ("+="*12)+"+"

        if play_rand socket
            socket.puts ("+="*12)+"+"
            challenges_won += 1
        end

        if challenges_won == 2
            give_flag socket
        end
    rescue ArgumentError
        puts "Invalid input"
    rescue Error
        puts "Error happened!"
        return
    end
end

start_server 4444
