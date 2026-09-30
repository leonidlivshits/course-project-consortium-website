FROM node:20 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY ./ .
ENV REACT_APP_API_URL=/api
RUN npm run build

FROM nginx:1 as production-stage
RUN mkdir /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/build /app
