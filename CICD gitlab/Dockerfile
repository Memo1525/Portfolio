#Dockerfile ————————————

FROM amazon/aws-cli:latest AS aws-cli

WORKDIR /usr/config

# AWS CREDENTIALS 
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_ACCESS_KEY_ID
ARG AWS_DEFAULT_REGION=us-east-1
ARG ENV_FILE_LOCATION

# Get .env file from s3 bucket
RUN aws s3 cp $ENV_FILE_LOCATION .env

FROM node:14.18.1-alpine AS build

# Install dependencies 

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install glob rimraf

RUN npm install --only=development

COPY . .

# Build nestjs project

RUN npm run build

FROM node:14.18.1-alpine AS production

WORKDIR /usr/app

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
ARG PM2_PUBLIC_KEY
ARG PM2_SECRET_KEY

RUN npm install pm2 -g

# Copy build files to /usr/src/app
COPY --from=aws-cli /usr/config/.env ./
COPY --from=build /usr/src/app/dist ./dist

# Copy Ecosystem.config.js 
COPY --from=build /usr/src/app/ecosystem.config.js ./ecosystem.config.js
COPY --from=build /usr/src/app/src/sources ./src/sources 
COPY package*.json ./

RUN npm install --only=production

RUN pm2 link $PM2_PUBLIC_KEY $PM2_SECRET_KEY
# Run server
CMD ["pm2-runtime", "start", "./ecosystem.config.js"]
