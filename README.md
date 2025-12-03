# DormFinder AI
A Feature-Based Housing Recommendation System for Rutgers University

Authors: Lily Del Pilar, Charley Yang
Tech Stack: Python · Pandas · BeautifulSoup · Scikit-Learn · Cosine Similarity · k-NN · Feature Engineering

# Overview

DormFinder AI is an intelligent dorm recommendation system designed to help Rutgers students find housing based on specific needs such as amenities, occupancy, layout, and campus location. Rutgers currently lacks a centralized, searchable database of housing options—forcing students to navigate multiple pages of inconsistent or incomplete information.

This project transforms unstructured housing data into an interpretable, feature-driven recommendation engine, using data-science techniques taught in class and real-world scraping + modeling practices.

Example query:

“2-person dorm with air-conditioning on College Avenue” → Hardenbergh Hall returned as a top match

✨ Key Features
✔ Full Dorm Dataset (Scraped + Cleaned)

Scraped dorm names and campus groups from Rutgers public housing pages using Requests + BeautifulSoup

Consolidated campus listings for:

Busch

College Avenue

Livingston

Cook/Douglass

Manually enriched dataset with per-dorm amenities (AC, laundry, Wi-Fi, occupancy, layout) when JS-based dropdown data could not be scraped automatically

✔ Feature Engineering & Encoding

Converted textual amenity data into one-hot encoded, numerical vectors

Normalized continuous and binary features

Resolved missing or inconsistent fields through automated checks and manual verification

✔ Similarity-Based Recommendation Model

Implemented cosine similarity and prototype k-NN ranking

Matches user queries to the most similar dorm feature vectors

Returns top-N recommendations with similarity scores

✔ End-to-End Data Pipeline

Collect dorm metadata from public Rutgers webpages

Clean and standardize raw data

Enrich with manually collected amenity details

Encode features numerically

Match dorms using similarity models

Evaluate accuracy using test queries

# Motivation

Rutgers provides centralized systems like WebReg for courses but offers no equivalent for housing. Students often struggle to compare dorms based on essential features like AC, room type, or lounge availability.

DormFinder AI serves as an early prototype for a campus-wide, data-driven housing exploration tool—interpretable, accessible, and student-focused.

# Methods & Algorithms
Data Collection

requests + BeautifulSoup used to extract:

Dorm names

Campus categories

Data stored in rutgers_dorms.csv

Data Cleaning

Removed duplicates

Standardized amenity labels

Verified JS-rendered amenity data manually

Feature Representation

One-hot encoding for amenities (AC, elevator, suite layout, etc.)

Binary indicators for occupancy, building type

Normalization for similarity calculations

Recommendation Models

Cosine Similarity for ranking dorms

Optional k-Nearest Neighbors (k-NN) for expanded matching

🧪 Evaluation & Testing

Success is measured by:

Recommendation Accuracy:
The correct dorm appears in the top 3 matches for test queries.

Data Completeness:
All Rutgers dorms have complete, consistent feature entries.

Interpretability:
Model outputs include similarity scores or top contributing features.

Example Test Case:

Query: “Air-conditioned doubles on Busch”
→ Best matches include Brett Hall, Allen Hall, and Barr Hall

# Limitations

Many Rutgers dorm pages use JS-loaded dropdowns, blocking automated scraping

Hybrid collection (automated + manual) resolves gaps but increases overhead

Dataset currently excludes subjective information (reviews, noise level, social culture)

# Future Work

The DormFinder AI will be extended into a full interactive platform:

Web UI with advanced filtering

Visualization of similarity scores

Map-based dorm exploration

Student reviews and crowdsourced features

Admin interface for data updates
