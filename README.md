# What Reviews Reveal About Skin-Type Fit: Sephora Skincare Review Mining

## Problem Statement

Sephora's digital merchandising team wants skincare shoppers to find products that work for their skin on the first try. When a product is a poor match, such as a stripping cleanser for sensitive skin or a heavy cream for oily skin, customers leave negative reviews, return products, and may shop elsewhere. Sephora's recommendation quiz, product filters, and seasonal campaigns could make better use of what reviewers say about why products fail for their skin type. This project analyzes moisturizer and cleanser reviews to identify complaints concentrated by skin type, ingredient, brand, and season, so the team can refine quiz recommendations, filters, and campaign timing.

**Why it matters:** Better product-to-skin matching can reduce returns and negative reviews and improve customer satisfaction.

## Dataset

| | |
|---|---|
| **Source** | Kaggle, [Sephora Products and Skincare Reviews](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews) |
| **Rows** | About 1M skincare reviews in total; filtered to moisturizers (and cleansers, if time allows). Final count TBD after cleaning |
| **Key columns (products csv)** | Product ID, product name, brand name, price, ingredients, highlights, review count, primary/secondary/tertiary category |
| **Key columns (reviews csv)** | Rating, is recommended, submission time, skin type, review title, review text, product ID |
| **Text fields** | Review text and review title; product ingredient lists |
| **Target variable** | None (Path B) |
| **Segments** | Skin type, brand, price tier, season/year |

The two files are joined on `product_id`. Categories are used to filter to moisturizers and cleansers.

## Analysis Path

This project follows Path B: Understanding/Extraction. Rather than predicting ratings, the goal is to identify which complaints drive negative sentiment in skincare reviews and whether they are concentrated among specific skin types, ingredients, brands, and seasons. The analysis will combine keyword and frequency analysis, sentiment analysis, topic modeling, and ingredient extraction from product data. It will also test whether patterns hold across years and segments, so Sephora's merchandising team gets findings specific enough to act on in its quiz, filters, and campaign timing. The primary focus will be moisturizers by skin type and ingredient, followed by brand and seasonal comparisons, with cleansers added as a secondary category if time allows. The final scope will be confirmed after data cleaning, since some segments may not have enough reviews to support reliable comparisons.


## Project Status

**Phase 1:** Problem definition, dataset selection, and repo setup. 