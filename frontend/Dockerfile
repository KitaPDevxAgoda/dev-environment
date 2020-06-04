FROM node:14.4
# ARG FIREBASE_ACCOUNT

WORKDIR /home/node/app
COPY package*.json ./
RUN yarn install
COPY . .
# RUN echo ${FIREBASE_ACCOUNT} > ./src/firebase/firebase-config.json

# ENV PUBLIC_URL ${PROFILE_PUBLIC_URL}
RUN yarn build

FROM nginx
LABEL DEVELOPER=["Tanakorn Pisnupoomi","Nathabordine Wonghirundecha"]

COPY --from=0 /home/node/app/build /var/www/frontend
COPY ./nginxconf/ /etc/nginx/conf.d/
EXPOSE 80
