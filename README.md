<div align="center">
  <h1>🏙️ Bengaluru House Price Predictor</h1>
  <p>
    <strong>A modern, fast, and visually stunning web application designed to predict real estate prices in Bengaluru using Machine Learning.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version" />
    <img src="https://img.shields.io/badge/FastAPI-0.111.0-009688.svg" alt="FastAPI" />
    <img src="https://img.shields.io/badge/Vite-5.2.0-646CFF.svg" alt="Vite" />
    <img src="https://img.shields.io/badge/Vanilla_JS-ES6+-F7DF1E.svg" alt="JavaScript" />
  </p>
</div>

<br />

## 📖 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#1-backend-setup-fastapi)
  - [Frontend Setup](#2-frontend-setup-vite)
- [Usage](#-usage)

---

## 🌟 Overview
This project seamlessly connects a trained Machine Learning model to a gorgeous, hardware-accelerated frontend. Built to handle complex predictions, the application instantly evaluates various property features (location, total square feet, BHK, etc.) and provides accurate price estimations in real-time.

## 🛠 Tech Stack
- **Backend**: Python, FastAPI, Uvicorn, Pandas, Scikit-learn
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, Custom CSS3, Vite
- **Model Storage**: Joblib / Pickle (AWS exported models)

## ✨ Key Features
- **Dynamic Autocomplete**: The location input utilizes an HTML `<datalist>` to instantly search and filter over 1,300+ valid Bengaluru locations extracted directly from the dataset.
- **Smart Data Filtering**: The size dropdown automatically cleans up abnormal dataset values (like "43 Bedroom") and sorts them logically (e.g., `1 BHK`, `2 BHK`).
- **Hardware-Accelerated UI**: The frontend leverages advanced CSS GPU acceleration (`translateZ`, `will-change`) to ensure silky smooth 60fps scrolling, even with intense blur filters and animated background blobs.
- **Graceful Fallbacks**: The API features built-in fallback mechanisms that intelligently simulate predictions if the primary `.pkl` ML model is unavailable.

## 📂 Project Structure
```text
📦 bengaluru-house-price-prediction
 ┣ 📂 backend
 ┃ ┣ 📜 main.py          # FastAPI application server
 ┃ ┣ 📜 models.py        # Pydantic schemas for data validation
 ┃ ┣ 📜 requirements.txt # Python dependencies
 ┃ ┗ 📜 model.pkl        # Machine learning model
 ┣ 📂 frontend
 ┃ ┣ 📜 index.html       # Main application layout
 ┃ ┣ 📜 style.css        # Glassmorphic UI & layout styling
 ┃ ┣ 📜 main.js          # API integration and DOM logic
 ┃ ┗ 📜 package.json     # Node.js dependencies & scripts
 ┗ 📜 bengaluru_house_prices.csv  # Dataset used for dynamic dropdown population
```

## 🚀 Getting Started

You will need to run the backend and frontend simultaneously in two separate terminals.

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher

### 1. Backend Setup (FastAPI)
Navigate to the backend directory, install the required Python packages, and spin up the server.

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
> **Note**: The backend will run on `http://localhost:8000`

### 2. Frontend Setup (Vite)
Open a new terminal, navigate to the frontend directory, install dependencies, and start the Vite development server.

```bash
cd frontend
npm install
npm run dev
```
> **Note**: The frontend will be accessible at `http://localhost:5173`

## 💡 Usage
1. Open `http://localhost:5173` in your web browser.
2. Search and select a valid Bengaluru location.
3. Choose the Area Type, Size, and Availability.
4. Input the Total Square Feet, number of Bathrooms, and Balconies.
5. Click **Predict Price** and enjoy the smooth counting animation!

---
<div align="center">
  <i>Designed and developed with 💙</i>
</div>
