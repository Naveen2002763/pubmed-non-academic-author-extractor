from typing import List

NON_ACADEMIC_KEYWORDS = [
    # Pharma & Biotech Companies
    "genentech", "roche", "pfizer", "moderna", "astrazeneca", "novartis", "merck",
    "sanofi", "biontech", "amgen", "illumina", "bristol-myers", "abbvie",
    "gsk", "boehringer", "bayer", "teva", "abbott", "takeda", "lilly",
    "novo nordisk", "genzyme", "regeneron", "gilead", "biogen"

    # CROs & industry support
    "syneos", "parexel", "iqvia", "icon plc", "medpace", "covance",

    # Suffixes and legal identifiers
    "inc", "ltd", "corp", "llc", "gmbh", "plc", "s.a.", "s.r.l.", "pvt", "co.", "company",

    # Industry terms
    "pharma", "pharmaceutical", "biotech", "bioscience", "biosciences",
    "therapeutics", "genomics", "diagnostics", "vaccines",
    "r&d", "contract research", "life sciences", "clinical research", "clinical trials",
    "innovation", "technologies", "labs", "healthcare", "solutions", "systems"
]


ACADEMIC_KEYWORDS = [
    "university", "universitas", "universität", "college", "school",
    "institute", "hospital", "clinic", "faculty", "department", "center", "centre", "lab",
    "mayo clinic", "cleveland clinic", "va", "veterans affairs", "public health",
    "medical center", "academic", "health science center", "nih", "government"
]



def is_non_academic(affiliation: str) -> bool:
    aff = affiliation.lower()
    return any(keyword in aff for keyword in NON_ACADEMIC_KEYWORDS) and not any(univ in aff for univ in ACADEMIC_KEYWORDS)

def extract_info(article: dict) -> dict:
    article_data = {
        "PubmedID": article['MedlineCitation']['PMID']['#text'],
        "Title": article['MedlineCitation']['Article']['ArticleTitle'],
        "Publication Date": article['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate'],
        "Non-academic Author(s)": [],
        "Company Affiliation(s)": [],
        "Corresponding Author Email": None
    }

    try:
        authors = article['MedlineCitation']['Article']['AuthorList']['Author']
        if isinstance(authors, dict):
            authors = [authors]
        for author in authors:
            aff = author.get('AffiliationInfo', [{}])[0].get('Affiliation', '')
            if is_non_academic(aff):
                fullname = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                article_data["Non-academic Author(s)"].append(fullname)
                article_data["Company Affiliation(s)"].append(aff)

            if 'ElectronicAddress' in author:
                article_data["Corresponding Author Email"] = author['ElectronicAddress']
    except Exception:
        pass

    return article_data