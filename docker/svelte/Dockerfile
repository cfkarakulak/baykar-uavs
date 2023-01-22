FROM node:16-alpine

ENV NODE_ENV development
ENV NPM_CONFIG_PRODUCTION false
ENV YARN_PRODUCTION false

WORKDIR /dashboard

COPY ../../src/dashboard .

RUN yarn
RUN yarn global add vite

EXPOSE 5173
EXPOSE 3000
EXPOSE 24678

CMD ["yarn", "dev", "--host", "0.0.0.0"]