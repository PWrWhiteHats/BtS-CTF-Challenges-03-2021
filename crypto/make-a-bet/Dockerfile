FROM ruby:2.7.1-alpine3.12
WORKDIR /app
COPY ./*.rb /app/
COPY ./flag.txt /app/

EXPOSE 4444

ENTRYPOINT ["ruby"]
CMD ["make-a-bet.rb"]
