FROM node:16-alpine3.15

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY frontend/package.json .
COPY frontend/package-lock.json .
RUN npm install

CMD ["npm", "run", "dev", "--host"]
