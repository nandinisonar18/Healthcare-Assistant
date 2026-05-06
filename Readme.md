# 🏥 Healthcare Assistant - Multi Agent AI Medical Support System

Healthcare Assistant is an intelligent AI-powered medical support platform developed to provide users with instant healthcare guidance through advanced Multi-Agent AI workflows.

This system combines multiple specialized AI agents to perform disease research, personalized diet planning, exercise recommendations, doctor consultation support, and general medical query answering — all within a single user-friendly interface.

The application is built using Python, CrewAI, LangChain, Gradio, OpenRouter LLM APIs, Tavily Search, and Serper Tools to deliver real-time healthcare insights and specialist recommendations.

---

## 🚀 Key Features

### ✅ Disease Analysis & Research Report
Users can enter a disease name or symptoms and receive:
- Detailed disease explanation
- Causes and risk factors
- Common symptoms
- Treatment options
- Prevention measures

---

### ✅ Personalized Diet Recommendation
The AI generates a disease-specific diet plan including:
- Recommended foods
- Foods to avoid
- Nutritional guidance
- Daily meal suggestions

---

### ✅ Exercise Recovery Plan
The assistant provides:
- Recovery-friendly exercises
- Physical wellness tips
- Mobility support suggestions
- Complementary therapy recommendations

---

### ✅ Doctor Consultation Recommendation
Based on detected disease/symptoms, the system:
- Identifies the relevant medical specialist
- Searches recommended doctors
- Displays doctor profiles with qualifications and consultation details

---

### ✅ Patient Experience Videos
The platform fetches relevant YouTube patient journey videos to help users understand real-life recovery stories.

---

### ✅ Medical Query Chatbot
Users can ask general health-related questions and receive:
- AI-generated patient-friendly answers
- Medical precautions
- Health guidance in simple language

---

## 🧠 Multi-Agent AI Workflow

This project uses a collaborative Multi-Agent Architecture where each healthcare task is managed by a dedicated intelligent AI agent.

### Agents Included:
- Medical Research Specialist Agent
- Diet Recommendation Agent
- Exercise Planning Agent
- Doctor Consultation Agent
- YouTube Patient Journey Agent
- Expert Medical Query Analyst

Each agent works independently and is orchestrated using CrewAI for task delegation and execution.

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| LLM Framework | CrewAI, LangChain |
| User Interface | Gradio |
| LLM Provider | OpenRouter API |
| Search Tools | Tavily Search API, SerperDev Tool |
| Doctor Data Filtering | LangChain Prompting |
| Environment Management | Python Dotenv |
| Monitoring | AgentOps |

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd Healthcare-Assistant
```

---

### 2. Create Virtual Environment

```bash
python -m venv healthcareenv
healthcareenv\Scripts\activate
```

---

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4. Configure `.env` File

Create a `.env` file in root directory and add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
SERPER_API_KEY=your_serper_api_key
AGENTOPS_API_KEY=your_agentops_api_key
```

---

### 5. Run Application

```bash
py UI.py
```

---

## 💻 Project Modules

| File Name | Description |
|-----------|-------------|
| `UI.py` | Main Gradio frontend and user interaction |
| `file1.py` | Core CrewAI agents, tasks, and crew definitions |
| `helper_functions.py` | Backend helper methods to trigger crews |
| `doctor_filter_by_degree.py` | Doctor category extraction and consultation filtering |
| `requirements.txt` | Required dependencies |
| `.env` | API key configuration |

---

## 🔄 System Workflow

```text
User Input
   ↓
AI Disease/Symptom Understanding
   ↓
Task Routed to Specific Healthcare Agent
   ↓
External Medical Search APIs Invoked
   ↓
LLM Generates Personalized Healthcare Output
   ↓
Results Displayed in Gradio Interface
```

---

## 📌 Use Cases

- Self preliminary health guidance
- Disease awareness and education
- Diet and exercise planning
- Specialist doctor finding
- Medical question answering
- Patient support assistance

---

## 📷 Output Screenshots

> Add screenshots of:
- Home Interface
- Disease Report
- Diet Recommendation
- Doctor Consultation
- Exercise Plan
- Medical Chatbot

---

## 🔐 Important Note

This project is developed for educational and healthcare assistance purposes only.

It does not replace professional medical diagnosis, treatment, or emergency consultation.

Always consult a certified medical practitioner for serious health concerns.

---

## 🌟 Future Enhancements

- Appointment booking integration
- PDF medical report generation
- Voice-based healthcare chatbot
- Hospital recommendation with maps
- User medical history memory
- RAG-based medical knowledge base

---

## 👩‍💻 Author

**Nandini Sonar**  
MCA Graduate | AI & Data Enthusiast | Python Developer

GitHub: https://github.com/nandinisonar18

---

## ⭐ If you found this project useful, don't forget to star the repository!
