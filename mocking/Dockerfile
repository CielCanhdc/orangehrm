FROM alpine:3.17

RUN apk add --update nodejs-lts && \
    apk add --update npm
RUN npm install -g mountebank

EXPOSE 2525

ENTRYPOINT ["mb"]
CMD ["start"]