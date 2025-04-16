# Step 1: Build the React frontend
FROM node:18 AS frontend

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Step 2: Build the FastAPI backend
FROM python:3.10 AS backend

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./
COPY --from=frontend /app/build frontend/build

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
