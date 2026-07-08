# 🌱 YieldSync: Smart Agricultural Intelligence & Crop Advisor

> **An open-source, AI-powered multi-agent agricultural assistant built on Agent Kernel to help farmers improve crop productivity, diagnose diseases, monitor farm history, and make data-driven decisions.**

YieldSync bridges the gap between traditional farming and modern AI by giving every farmer an intelligent digital agronomist through a simple conversational interface. The system combines multi-agent reasoning, historical farm memory, market intelligence, and weather insights to deliver personalized agricultural recommendations.

---

# 🎯 Problem Statement

Smallholder farmers, particularly in rural regions, face major challenges in maximizing crop yields due to limited access to expert agricultural knowledge, real-time market information, and crop diagnostics.

According to **UN Sustainable Development Goal 2 (Zero Hunger)**, increasing the productivity and income of small-scale food producers is essential for achieving global food security.

Farmers commonly struggle with:

- 🌾 Identifying crop diseases before they spread
- 🧪 Detecting soil nutrient deficiencies
- 💰 Accessing real-time market prices to avoid middlemen exploitation
- 🌦️ Understanding weather impacts on farming decisions
- 📒 Tracking crop rotation and historical farm records across seasons

Existing solutions are often too technical, fragmented, or fail to remember farm-specific historical context.

---

# 💡 Solution Overview

YieldSync provides an AI-powered agricultural advisor that communicates through a familiar chat interface (WhatsApp, Slack, or a web application).

Built entirely on the **Agent Kernel Framework**, the system coordinates multiple AI agents capable of retrieving external information, maintaining farm memory, and delivering actionable recommendations.

---

# 🏗️ System Architecture

The application follows a modern full-stack architecture.

## Frontend

- **Next.js (React)**
- Responsive farmer-friendly interface
- Hosted on **Vercel**

## Backend

- **Python**
- **FastAPI**
- Built using **Agent Kernel**
- Hosted on **Render**

## AI Engine

- **Llama-3.3-70B-Versatile**

## Framework

- Agent Kernel
- OpenAI Module
- REST API Module

---

# 🤖 Multi-Agent Architecture

YieldSync utilizes Agent Kernel's multi-agent capabilities through specialized AI agents.

## 🌿 Agronomy Advisor Agent

The primary conversational agent responsible for:

- Understanding farmer queries
- Diagnosing crop issues
- Providing cultivation advice
- Coordinating with other agents and tools

---

## 📈 Market & Intelligence Agent

Provides market intelligence including:

- Current wholesale prices
- Market trends
- Selling recommendations
- Crop profitability insights

---

# 🛠️ Agent Tools

The Agronomy Advisor is equipped with several native tools.

| Tool | Purpose |
|------|----------|
| `diagnose_crop_disease` | Detect crop diseases from farmer descriptions/images |
| `get_market_price` | Retrieve current market prices |
| `get_weather_forecast` | Provide localized weather forecasts |
| `check_farm_history` | Retrieve previous crop records |
| `record_crop_planting` | Store planting history for future recommendations |

---

# 🧠 Session Memory

Unlike traditional chatbots, YieldSync uses Agent Kernel's persistent session management to remember:

- Farm location
- Soil characteristics
- Crop history
- Previous diseases
- Seasonal planting cycles
- Farmer preferences

This enables highly personalized agricultural advice over multiple conversations.

---

# 🛡️ Guardrails

YieldSync includes safety mechanisms that prevent unsafe AI recommendations.

If the system detects:

- Quarantined plant diseases
- Hazardous biological outbreaks
- High-risk agricultural emergencies

the workflow is interrupted, and the farmer is advised to contact official agricultural extension services instead of relying solely on AI-generated guidance.

---

# 🚀 API Integration

The backend exposes a native FastAPI endpoint for frontend communication.

## Interactive Swagger Documentation

```
https://YOUR-RENDER-URL.onrender.com/docs
```

---

## Production Endpoint

```
POST /run
```

### Request

```json
{
  "prompt": "My tomato leaves have yellow spots",
  "agent": "agronomy_advisor",
  "session_id": "unique-session-id"
}
```

### Response

```json
{
  "result": "Your tomato plants may be affected by early blight...",
  "session_id": "unique-session-id"
}
```

---

# 📁 Project Structure

```
YieldSync
│
├── backend/
│   ├── agents/
│   ├── tools/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── yieldsync-ui/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── ...
│
└── README.md
```

---

# ⚙️ Local Development

## 1. Clone Repository

```bash
git clone https://github.com/your-username/yieldsync.git

cd yieldsync
```

---

## 2. Backend Setup

Navigate to the backend.

```bash
cd backend
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Start the server.

```bash
python main.py
```

The backend will run at

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## 3. Frontend Setup

Navigate to the frontend.

```bash
cd yieldsync-ui
```

Install packages.

```bash
npm install
```

Run the development server.

```bash
npm run dev
```

Open

```
http://localhost:3000
```

---

# 🌍 Deployment

## Frontend

- Vercel

## Backend

- Render

---

# 🔄 Workflow

```text
Farmer
    │
    ▼
Frontend (Next.js)
    │
REST API
    │
    ▼
Agent Kernel Backend
    │
    ├── Agronomy Advisor
    ├── Market Agent
    ├── Weather Tool
    ├── Farm Memory
    └── Disease Diagnosis
    │
    ▼
AI Response
    │
    ▼
Farmer
```

---

# 🎯 Features

- 🌱 AI Crop Advisor
- 🦠 Crop Disease Diagnosis
- 🌦️ Weather Forecasting
- 💰 Live Market Prices
- 📖 Farm History Tracking
- 🌾 Crop Rotation Records
- 💬 Conversational Interface
- 🧠 Persistent AI Memory
- 🛡️ Safety Guardrails
- 📱 Mobile-Friendly Interface

---

# 🛣️ Roadmap

- [ ] Image-based disease detection
- [ ] Soil nutrient analysis
- [ ] Satellite crop monitoring
- [ ] WhatsApp integration
- [ ] Voice assistant support
- [ ] Multi-language support
- [ ] Farmer community knowledge sharing
- [ ] Government advisory integration
- [ ] IoT sensor connectivity

---

# 🌍 Alignment with UN Sustainable Development Goals

YieldSync directly contributes to:

## SDG 2 — Zero Hunger

By helping farmers:

- Increase productivity
- Reduce crop losses
- Improve decision making
- Maximize profitability
- Promote sustainable agricultural practices

---

# 📄 License

This project is open source and available under the **MIT License**.

---

# ❤️ Built With

- Agent Kernel
- FastAPI
- Python
- Next.js
- React
- Vercel
- Render
- Llama-3.3-70B-Versatile