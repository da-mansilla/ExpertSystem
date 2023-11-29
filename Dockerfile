FROM node:18.14-alpine3.16

WORKDIR /app


ARG REACT_APP_API_URL
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.8.12
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY --from=0  /app/dist/ ./build
COPY --from=0  /app/dist/assets ./build
# COPY backend/main.py backend/constants.py backend/MotorInferencia.py backend/controller.py backend/models.py backend/__init__py ./
COPY backend /app/
EXPOSE 80

# ENTRYPOINT [ "python3" ]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



