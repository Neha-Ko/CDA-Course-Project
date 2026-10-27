# What Reviews Reveal About Skin-Type Fit: Sephora Moisturizer Review Mining

**Topic:** Sentiment analysis of Sephora skincare reviews to identify skin-type-specific complaints and improve product recommendations


## Problem Statement

Sephora's digital product team wants skincare shoppers to find products that work for their skin on the first try. When a product is a poor match, such as a heavy cream for oily skin or a light gel for dry skin, customers leave negative reviews, return products, and may shop elsewhere. Sephora's skincare quiz and product filters could make better use of what reviewers say about why products fail for their skin type. This project analyzes moisturizer reviews to identify complaints that are concentrated in specific skin types for the same product, so the team can turn them into concrete quiz and filter rules.

## Dataset

| | |
|---|---|
| **Source** | Kaggle, [Sephora Products and Skincare Reviews](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews) (scraped March 2023) |
| **Scope** | Moisturizers only (Moisturizers and Night Creams subcategories) |
| **Cleaned size** | 184,664 reviews of 379 products from 90 brands, 2008–2023 |
| **Text fields** | Review title and review text |
| **Key columns** | Rating, submission date, skin type, product, brand, price, ingredients |
| **Target variable** | None (Path B) |

The cleaned dataset is included in `Data/` as a compressed CSV. The raw data (about 1 million skincare reviews across six files) is not included because of its size; notebook 1 downloads it automatically from Kaggle.

## Progress

**Phase 1: Proposal** ✅

**Phase 2: Exploration and text mining** ✅
- **Dataset build:** filtered to moisturizers, removed about 10,300 reviews duplicated across mini and full-size product pages, and dropped reviews missing text, skin type, or ingredients.
- **Exploration:** skin types are imbalanced (54.5% combination, 11.2% oily), and shoppers already choose products by skin type. For example, Clinique's Moisturizing Gel draws 28% of its reviews from oily skin, while its Lotion+ draws 30% from dry skin. The analysis therefore compares complaint rates by skin type *within the same product*.
- **Keyword analysis:** low-rated reviews are marked by "broke" (breakouts), "not work," and "not worth." Oily-skin reviewers more often mention acne and greasiness, and dry-skin reviewers more often mention products not moisturizing enough.
- **Baseline sentiment (VADER):** follows star ratings only weakly (rank correlation 0.36) and scores 55% of 1–2 star reviews as positive, missing skincare-specific complaints like "pilled" or "broke me out." Star ratings serve as the satisfaction measure instead.

**Phase 3: Complaint labeling and findings** (next)
- Use Claude to label every review in a stratified sample of 8,000 (20 products × 4 skin types × 100 reviews) with one or more complaint categories, or "no complaint."
- Hand-check about 100 labels for accuracy.
- Compare complaint rates across skin types within each product and turn the clearest gaps into quiz and filter recommendations.

## Repository Structure

```
├── Data/
│   └── sephora_moisturizer_reviews_clean.csv.gz   # cleaned dataset
├── Notebooks/
│   ├── 1_Build_Final_Dataset.ipynb   # download, filter, deduplicate, clean
│   ├── 2_Data_Exploration.ipynb      # basic stats, text length, skin type mix
│   ├── 3_Text_Mining.ipynb           # preprocessing, keywords, sentiment, Phase 3 plan
│   └── *.html                        # HTML exports of each notebook
├── src/
│   ├── utils.py           # data loading and plotting helpers
│   └── preprocessing.py   # text cleaning for keyword and sentiment analysis
├── requirements.txt
├── LICENSE
└── README.md
```

## How to Run

1. **Clone the repository** and open the project folder.
2. **Create and activate a virtual environment, then install packages:**
   ```
   python3 -m venv .venv
   source .venv/bin/activate        # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Add a Claude API key** (needed only for the Claude cells in notebook 3). Create a file named `.env` in the project folder containing:
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```
   This file is excluded from Git by `.gitignore`. The Claude cells are switched off by default (`RUN_CLAUDE = False`), so notebook 3 runs without a key.
4. **Run the notebooks in order**, using the `.venv` kernel:
   - **Notebook 1** is optional, since the cleaned dataset is already in `Data/`. Running it downloads the full raw dataset from Kaggle (requires a Kaggle account and several GB of disk space) and recreates the cleaned file.
   - **Notebooks 2 and 3** load the cleaned dataset from `Data/` and run in a few minutes.

## License

MIT License. See `LICENSE`.