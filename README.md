# Interactive Professional Portfolio & GPO Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://59azbpzj2vwbkwcn7mjaqe.streamlit.app)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Active-success?logo=github&logoColor=white)](https://johnparente97.github.io/Demo)

Welcome! This repository hosts a dual-concept professional portfolio explaining the purpose behind my apps, my professional background in **Group Purchasing Organization (GPO) account management**, **procurement spend analytics**, and **AI/machine learning models**.

---

## 🔗 Live Access Links

*   🚀 **[Launch Interactive Analytics Dashboard (Streamlit Cloud)](https://59azbpzj2vwbkwcn7mjaqe.streamlit.app)**
*   🖥️ **[Launch Web Portfolio (GitHub Pages)](https://johnparente97.github.io/Demo)**

---

## 🛠️ Portfolio Features

### 1. Static Web Portfolio (`index.html`)
A premium single-page web app built with Vanilla HTML5, CSS (incorporating modern glassmorphism, responsive grids, and variables), and JavaScript:
*   **Animated Impact Snapshot:** Dynamically counts up key business achievements (50+ active accounts, $10M+ analyzed spend, $150K+ rebates managed, 42.5K+ social audience growth).
*   **Interactive Project Explorer:** Instant live search and tag filtering (AI & ML, Data Analytics, Software Development, Pipelines) mapping 14 distinct repositories.
*   **Business Value Modals:** Detail cards explaining the real-world value and technological frameworks behind each repository.
*   **Dark/Light Toggle:** Smooth visual theme transitions storing user selection.

### 2. GPO Spend Dashboard (`app.py`)
A Python Streamlit app offering data-driven insights:
*   **Metrics Snapshot:** Active performance indicators tracking portfolio scope.
*   **Interactive GPO Analytics:** Plots detailing spend distribution and compliance percentages across major categories.
*   **Savings Recovery Calculator:** Real-time GPO calculator showing off-contract leakage reduction outcomes.
*   **Interactive Repository Filter:** Dropdowns and search terms mapping software pipelines and models.

---

## 📂 Repository Structure

*   [index.html](index.html) - Structural framework for the static website portfolio.
*   [style.css](style.css) - Advanced stylesheet containing variables, animations, and dark/light layouts.
*   [app.js](app.js) - Project search database, metric count-ups, and modal control logic.
*   [app.py](app.py) - Streamlit dashboard with Plotly data visualization components.
*   [requirements.txt](requirements.txt) - Python libraries needed to run the Streamlit dashboard.

---

## 🚀 How to Host & Run

### How to Host the Streamlit App (Streamlit Community Cloud)
1. Commit and push all files in this directory to a public GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io) using your GitHub account.
3. Click **New App**, select your repository, specify the branch (usually `main`), and set the main file path to `app.py`.
4. Click **Deploy!** Your app is now live at: https://59azbpzj2vwbkwcn7mjaqe.streamlit.app

### How to Host the Static Portfolio Page (GitHub Pages)
1. Go to your repository settings on GitHub.
2. Scroll to the **Pages** menu on the left sidebar.
3. Under **Build and deployment**, set the source to **Deploy from a branch**.
4. Select `main` (or your current branch) and `/ (root)` folder, then click **Save**.
5. GitHub has hosted your webpage at: https://johnparente97.github.io/Demo/

### How to Run Locally

#### Running the Web Portfolio:
Double-click `index.html` to launch it immediately in your web browser.

#### Running the Streamlit App:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the local server
streamlit run app.py
```
