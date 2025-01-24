# 📊 **Information Extraction Project**

This project automates the extraction, enrichment, and storage of medical data from HTML files, focusing on creating structured dictionaries and analyzing medication-related information.

---

## 🚀 **Features**
- 🔍 **Entity Extraction**: Extracts names of medications based on active substances from 26 HTML pages.
- 📂 **Dictionary Creation**: Generates a structured dictionary (`subst.dic`) in **DELAF format**, encoded in **UTF-16 LE with BOM**.
- ✨ **Data Enrichment**: Updates and enriches the dictionary with additional data from a medical corpus (`corpus-medical.txt`).
- 📊 **Posology Extraction**: Identifies dosage, frequency, and treatment details using **Unitex** linguistic tools.
- 🗄️ **Database Integration**: Stores extracted posologies in an **SQLite database** for easy management.

---

## 🛠️ **Technologies**
- **Python**: For scripting and automation.
- **Unitex**: To build linguistic extraction graphs.
- **SQLite**: As the database to store and query extracted data.
- **HTML**: The source of the raw data for extraction.
