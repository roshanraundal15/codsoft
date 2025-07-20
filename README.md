# CODSOFT AI Internship Projects

This repository contains solutions to the AI internship tasks provided by CODSOFT. Each project demonstrates core concepts in artificial intelligence, machine learning, and web development.

## Table of Contents
- [About](#about)
- [Projects](#projects)
  - [1. Chatbot (Rule-Based & Gemini AI)](#1-chatbot-rule-based--gemini-ai)
  - [2. Tic-Tac-Toe AI (Web)](#2-tic-tac-toe-ai-web)
  - [3. Face Detection (Web)](#4-face-detection-web)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Contact](#contact)

---

## About
This repository showcases a variety of AI and machine learning projects completed as part of the CODSOFT internship. Each task is self-contained and demonstrates a different aspect of AI, from natural language processing to computer vision.

---

## Projects

### 1. Chatbot (Rule-Based & Gemini AI)
- **Folder:** `chatbot/`
- **Description:**
  - A web-based chatbot that responds to user queries using both rule-based logic and the Gemini 2.0 Flash model (Google Generative AI).
  - Features a modern web UI built with Flask and Tailwind CSS.
- **How to Run:**
  1. Navigate to the `chatbot` folder.
  2. Install dependencies:
     ```bash
     pip install flask google-generativeai
     ```
  3. Run the app:
     ```bash
     python chatbot.py
     ```
  4. Open [http://localhost:5000](http://localhost:5000) in your browser.

### 2. Tic-Tac-Toe AI (Web)
- **Folder:** `tic_tac_toe/`
- **Description:**
  - A web-based Tic-Tac-Toe game with two modes: play against an unbeatable AI (Minimax algorithm) or two-player mode.
  - Features a modern, responsive UI with player name input, score tracking, and mode toggle.
- **How to Run:**
  1. Navigate to the `tic_tac_toe` folder.
  2. Install dependencies:
     ```bash
     pip install flask
     ```
  3. Run the app:
     ```bash
     python tic_tac_toe.py
     ```
  4. Open [http://localhost:5000](http://localhost:5000) in your browser.


### 3. Face Detection (Web)
- **Folder:** `face_detection/`
- **Description:**
  - A web app for face detection in images using state-of-the-art RetinaFace (insightface) for robust detection of small and distant faces.
  - Modern UI for uploading images and viewing results.
- **How to Run:**
  1. Navigate to the `face_detection` folder.
  2. Install dependencies (Python 3.10/3.11 recommended):
     ```bash
     pip install flask opencv-python numpy insightface
     ```
  3. Run the app:
     ```bash
     python app.py
     ```
  4. Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Technologies Used
- Python 3
- Flask
- OpenCV
- insightface (RetinaFace)
- Google Generative AI (Gemini)
- Pandas, NumPy, scikit-learn
- Jupyter Notebook
- Tailwind CSS

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd codsoft
   ```
2. Follow the setup instructions for each project folder above.
3. For best compatibility, use Python 3.10 or 3.11 for all AI/ML projects.

---

## Contact
For any questions or issues, please contact:
- **Email:** contact@codsoft.in
- **Website:** [https://www.codsoft.in](https://www.codsoft.in)

---

**Happy Learning and Coding!** 
