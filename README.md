# pubmed-non-academic-author-extractor
# PubMed Non-Academic Author Extractor

This project is a command-line tool to search PubMed for scientific articles and extract metadata about authors affiliated with **non-academic institutions** such as pharmaceutical or biotech companies. It uses a keyword-based filtering system to classify authors as academic or non-academic based on their affiliations.

---

## 🚀 Features

- 🔍 Search PubMed using any free-text query (e.g., "cancer AND Genentech").
- 📄 Extract metadata including:
  - Author names
  - Affiliations
  - Corresponding author emails (if available)
- 🧪 Identify **non-academic authors** using custom keyword lists.
- 📁 Save results to a structured `.csv` file.

---

## ⚙️ How It Works

1. Takes a query string (e.g., `"Pfizer AND COVID-19"`)
2. Fetches article data from PubMed via the Entrez API.
3. Parses author metadata and affiliation.
4. Applies keyword filtering to classify authors as non-academic.
5. Writes output with these columns:
   - PubMed ID
   - Title
   - Publication Date
   - Non-Academic Author(s)
   - Company Affiliation(s)
   - Corresponding Author Email

---

## 🧠 Keyword Logic

### ✅ Non-Academic Keywords
Includes company names, legal suffixes, and biotech/pharma terms such as:
"pfizer", "genentech", "biotech", "pharmaceutical", "therapeutics", "inc", "llc", "plc", etc.
Used to exclude known academic affiliations:
"university", "hospital", "college", "institute", "government", "va", etc.

---

## 📝 Why Output May Have No Non-Academic Authors

Some queries return only academic authors.  
For example, queries like `"cancer AND Genentech"` or `"Pfizer AND COVID-19"` might result in only academic-affiliated authors, depending on the PubMed dataset at the time.

This is **expected** and proves the tool is filtering correctly.

---

## 💻 Example Usage

```bash
poetry install
poetry run python -m get_papers_list.cli "Pfizer" --file=pfizer_results.csv --debug
poetry run python -m get_papers_list.cli "cancer AND Genentech" --file=cancer_genentech.csv --debug
