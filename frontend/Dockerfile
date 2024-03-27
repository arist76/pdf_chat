# Use this image as the platform to build the app
FROM node:18-alpine AS builder

WORKDIR /frontend

COPY pdf_chat/package*.json .

RUN npm ci

COPY pdf_chat/ .



RUN npm run build
RUN npm prune --production

FROM node:18-alpine

WORKDIR /frontend

COPY --from=builder /frontend/build build/
COPY --from=builder /frontend/node_modules node_modules/
COPY pdf_chat/package.json .

EXPOSE 3000

CMD ["node","build"]

