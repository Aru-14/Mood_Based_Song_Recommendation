# Mood_Based_Song_Recommendation


## 📌 Project Overview
The **Mood-Based Song Recommender** is a Flask web application that suggests songs based on the user's mood. The application:
- Uses **TextBlob** to analyze the sentiment of user input.
- Classifies the mood as **Happy, Sad, Energetic, or Neutral**.
- Matches the detected mood with songs from a **CSV dataset**.
- Randomly selects and displays a song recommendation.

---

## 🛠️ Technologies Used
- **Python** (Flask, Pandas, TextBlob)
- **HTML, CSS, JavaScript (jQuery)**
- **CSV (Song dataset)**

---

## 🚀 How to Run the Project

### **1️⃣ Install Dependencies**
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install flask pandas textblob
```

### **2️⃣ Run the Flask App**
```bash
python app.py #here I've used app(1).py
```

### **3️⃣ Open in Browser**
Go to:
```
http://127.0.0.1:5000/
```

---

## 📜 Project Structure
```
Mood-Song-Recommender/
│── templates/
│   └── index.html  # Frontend UI
│── songvsmood.csv  # Dataset containing songs and moods
│── app.py          # Flask backend
│── README.md       # Project documentation
```

---

## 🎯 Features
✅ **Sentiment Analysis** to detect user mood
✅ **Random Song Selection** based on mood
✅ **Simple Web Interface** (HTML, JavaScript, Flask)
✅ **AJAX Integration** for real-time recommendations

---

## 💡 Future Enhancements
🔹 **Improve Sentiment Analysis** with NLP models
🔹 **Expand Song Dataset** for more variety
🔹 **Integrate Spotify API** to play recommended songs

---

## 🎵 Sample Input & Output

**User Input:**  
```
"I am feeling very excited today!"
```

**Detected Mood:**  
```
Energetic
```

**Recommended Song:**  
```
🎶 Listen to: "Eye of the Tiger" by Survivor
```

---

## 📧 Contact & Contributions
Want to contribute? Feel free to fork the repo and submit a pull request!

👨‍💻 Developed by **Arunima Paunikar**  


