FROM alpine:3.20

RUN apk add --no-cache traefik gettext

RUN mkdir -p /etc/traefik/acme \
    && touch /etc/traefik/acme/acme.json \
    && chmod 600 /etc/traefik/acme/acme.json

COPY ./compose/production/traefik/traefik.template.yml /etc/traefik/traefik.template.yml

CMD envsubst < /etc/traefik/traefik.template.yml > /etc/traefik/traefik.yml && \
    traefik --configFile=/etc/traefik/traefik.yml
