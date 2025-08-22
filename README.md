# 🧮 Retirement Calculator

This Streamlit app helps you figure out **how much you need to invest monthly** in order to retire with your desired yearly or monthly income, based on the **4% safe withdrawal rule** and assuming a **7% annual return** on investment.

🔗 **Live App:** [retirement-calculator-maria-brito.streamlit.app](https://retirement-calculator-maria-brito.streamlit.app)

## 📌 Features

- ✅ Simple and clean user interface
- ✅ Input your:
  - Name
  - Current age
  - Desired retirement age
  - Desired income (monthly or yearly)
- ✅ Calculates:
  - How much you need to invest every month
  - Total portfolio value needed
  - Years until retirement
- ✅ Shows a disclaimer on assumptions

## 📈 Assumptions

- 4% safe withdrawal rate (based on the Trinity Study)
- 7% annual return on investment (compounded monthly)

> You can adjust these values in the source code if you'd like to use a different investment philosophy.

## 🚀 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/mariavero-brito/Retirement-Calculator.git
cd Retirement-Calculator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run retirement_calculator_app.py
```

## 🛠 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- 💻 Visual Studio Code

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).