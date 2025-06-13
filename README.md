# 🔍 Log Analysis using Machine Learning

Logs are a rich source of system and network activity. However, with the **growing volume of log data**, manually identifying anomalies becomes impractical. This project presents a **machine learning–driven log anomaly detection system** that automates the process and improves accuracy.

---

## 📌 Problem Statement

Traditional log analysis is limited in speed and scalability. The goal of this project is to develop an automated log anomaly detection system using machine learning models to:

- Identify abnormal patterns in logs
- Detect potential security threats or system failures
- Minimize false positives with a data-driven approach

---

## 📊 Dataset

We used the **CICIDS2017** dataset, a comprehensive intrusion detection dataset with diverse network traffic features and labels. It includes various attack types and normal behavior patterns.

---

## 🧠 Machine Learning Models and Results

We trained and evaluated multiple machine learning models. Below is a performance comparison:

| Model                | Precision | Recall   | F1 Score |
|---------------------|-----------|----------|----------|
| **Random Forest**        | 0.9614    | 0.9236   | **0.9945** ✅ |
| K-Nearest Neighbors (KNN) | 0.9601    | 0.9212   | 0.9942 |
| Decision Tree         | 0.8862    | 0.7759   | 0.9799 |
| Logistic Regression   | 0.8799    | 0.7735   | 0.9665 |
| Naive Bayes           | 0.7068    | 0.9131   | 0.6319 |

> 📌 **Random Forest** gave the best overall performance with an accuracy of **96.14%**.

---

## 🛠️ Technologies Used

- Python (scikit-learn, pandas, matplotlib)
- Jupyter Notebook
- CICIDS2017 Dataset
- Git for version control
- GitHub for collaboration and hosting

---

## Files

- `project.pptx` - Presentation
- `Report of PS.docx` - Documentation

