FROM ruby:2.7.0

WORKDIR /app
EXPOSE 8443

RUN useradd -m chad_admin
USER chad_admin

COPY --chown=chad_admin Gemfile Gemfile.lock ./
RUN bundle install

COPY --chown=chad_admin . .

CMD [ "./index.rb" ]
