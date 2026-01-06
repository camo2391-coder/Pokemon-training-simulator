# 🧠 POKEMON TRAINING SIMULATOR — Pokémon Training Simulator with EVs, Level and Stats

This project is an interactive Pokémon training simulator built in Python. It allows you to query Pokémon data from a database, assign training values (EVs), customize levels, and calculate final stats for two Pokémon.

---

## 📂 Project Structure

```
Project Structure

POKEMON TRAINING/
├── config/
│   ├── app_config.py        # SQL queries and base columns
│   └── database_config.py   # Database credentials and connection parameters
├── src/
│   ├── pokemon_simulator_main.py   # Main simulator logic
│   ├── tests/                       # Unit and integration tests (to be added)
│   └── utils/                       # Helper functions (PokeAPI scripts, charts, lists)
├── .gitignore               # Ignore unnecessary files
└── README.md                # Project documentation
```

---

## ⚙️ Features

- Connects to a MySQL database to retrieve Pokémon data  
- Search by ID or partial name  
- Manual assignment of EVs for each stat (HP, ATK, DEF, SPATK, SPDEF, SPD)  
- Validation of EV limits (maximum 510)  
- Custom level assignment (1–100)  
- Final stat calculation using standard formulas  
- Console output displayed with `pandas.DataFrame`

---

## 🚀 Execution

Run from the project root:

```bash
python -m src.pokemon_simulator_main