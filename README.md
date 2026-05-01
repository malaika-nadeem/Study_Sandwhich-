# 🥪 Study Sandwich

Study Sandwich is an AI-powered study assistant that converts uploaded notes into interactive quizzes.

It helps students learn actively by generating MCQs and short questions from study material, along with instant evaluation and scoring.

---

## 🚀 Features

- 📂 Upload study materials (PDF, DOCX, PPTX, TXT)
- ✂️ Select specific content range (PDF support)
- 🧠 AI-generated quizzes:
  - Multiple Choice Questions (MCQs)
  - Short Questions
- ✅ Instant answer evaluation
- 📊 Final score display
- 🧾 Simple and interactive UI using Streamlit

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- pdfplumber (PDF reading)  
- python-docx (Word files)  
- python-pptx (PowerPoint files)  
- Groq API (AI quiz generation & evaluation)

---

## 📁 Project Structure

study-sandwich/
│
├── app.py              # Main landing page
├── pages/
│   ├── quiz.py        # File upload & settings
│   └── test.py        # Quiz generation & evaluation
│
└── README.md

## ▶️ How to Run This Project

### 1. Install required libraries
```bash
pip install streamlit pdfplumber python-docx python-pptx groq
````

### 2. Run the app

```bash
streamlit run app.py
```

## 🧠 How It Works

1. User uploads study notes
2. Text is extracted from the file
3. User selects number of MCQs and short questions
4. AI generates quiz from the content
5. User answers questions
6. System evaluates answers and shows score

## 🎯 Purpose

The goal of this project is to make studying more interactive by converting notes into quizzes using AI, helping students practice active learning.



⭐ If you like this project, feel free to give it a star!


