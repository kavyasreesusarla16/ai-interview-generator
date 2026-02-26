🚀 AI Interview Question Generator
Live Demo: https://ai-interview-generator-58ez.onrender.com

This project is a Flask-based AI web application that generates domain-specific interview questions using the Groq Llama-3 model.
The user selects a subject/domain → clicks generate → and instantly receives interview questions powered by AI.

📌 Features

✔️ Modern, attractive UI

✔️ Select any interview topic

✔️ AI-generated questions (Groq API)

✔️ Fully deployed & live on Render

✔️ Fast responses using Llama-3

✔️ Clean HTML/CSS templates

✔️ Organized project structure

🛠️ Tech Stack
Component	Technology
Backend	Flask (Python)
AI Model	Groq Llama 3
Deployment	Render Web Service
Frontend	HTML, CSS
Server	Gunicorn
📁 Project Structure
ai-interview-generator/
│── app.py
│── requirements.txt
│── Procfile
│── keep.txt
│── static/
│── templates/
│   │── index.html
│   │── result.html
⚙️ Setup Instructions (Local)
1. Clone the repository
git clone https://github.com/kavyasreesusarla16/ai-interview-generator
2. Install dependencies
pip install -r requirements.txt
3. Add your Groq API key

Create a .env file:

GROQ_API_KEY=your_api_key_here
4. Run the application
python app.py

App will run at:

http://127.0.0.1:5000
🌐 Deployment

The project is deployed on Render using:

Procfile

Python 3.14

requirements.txt

Environment variable: GROQ_API_KEY

Live link:
👉 https://ai-interview-generator-58ez.onrender.com

🎯 How It Works

User selects a domain (AI, DBMS, Python, Java, etc.)

App sends the selection to Groq's API

Llama-3 generates structured interview questions

Questions are displayed neatly on the result page

🧠 Sample Output
1. Explain supervised vs unsupervised learning.  
2. What is overfitting in machine learning?  
3. Define confusion matrix.  
4. Explain gradient descent.  
5. What is regularization?

👩‍💻 Author

Kavya Sree Susarla
B.Tech CSE (AI)
AI Projects • Python Developer • Flask Apps

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
https://github.com/kavyasreesusarla16/ai-interview-generator
