## Notebook structure for M2 :
1) general remark on the dataset with a global view (missing data, corrupted data, ...) (CLEANING)
2) Hedi's part, which serves as a representation for cleaning (EXPLORATION)
3) Thomas' part which filters the data for bio vs non bio + his analysis on the scores (BIO VS NON-BIO : SCORES)
4) Concatenate Antoine's information on the additives (BIO VS non-BIO : ADDITIVES) 
5) Why are bio products bad sometimes? How come they sometimes have poor nutritional scores?
6) Explain why we dropped the global analysis per country (missing countries) by Lucas (DROPPED QUESTIONS : JUSTIFICATION)
7) CONCLUSION : PROPOSED DATA STORY


# Free Diving into Food Facts

# Abstract
While everybody buys and consumes numerous food-related products every day, little care is given in the precise products’ compositions.   
For the sake of this study, we decided to focus our effort on the [Open Food Facts database](https://world.openfoodfacts.org/data) regrouping the information of a very broad variety of products, including their nutrition facts and derived nutrition scores from different standards, such as the [UK Food Standards Agency](https://en.wikipedia.org/wiki/Food_Standards_Agency)'s (FSA) or the same score but derived from the French market. 

We will focus on the analysis of the predominant products over the world. Several directions will be explored such as the nutritional differences between regular and bio-products, the differences across countries, the effect of ingredients on selected nutrition scores.
We will try to provide appealing and interactive visualizations to support our findings and analysis.


# Research questions

* Comparing bio vs. normal products, is there a real difference in composition?
* What are the levels of interdependencies between nations based on their production and importations? 
* Among the largest food companies, which ones have the broadest portfolio? In which sectors are they predominant?
* How do ingredients or categories influence the selected nutrition scores? 

# Dataset
* Lettuce analyse this dataset: [Open Food Fact database](https://world.openfoodfacts.org/data).  
The dataset is built as part of a collaborative project to build a free and open database of alimentary items commercially available worldwide. It is stored as a `.csv` file containing several fields (not always indicated), typically the list of ingredients of the product, the nutritional table (usually indicated on the back of the product), nutritional scores, the brand and distributor, the packaging of the product, and more.

#### Optional
* [Dunnhumby dataset](https://www.dunnhumby.com/careers/engineering/sourcefiles), which could be used to gain consumption information for selected products.

# A list of internal milestones up until project milestone 2
##### 28th to 3rd of November:
* Setup git structure, coding conventions, and select tools/libraries
* Explore data, explore what’s available
* Play with the dataset
##### 4th to 10th of November:
* Assess data cleanliness, missing data proportion, data distribution across countries and categories
* Data preprocessing
* Data cleaning
##### 11th to 17th of November: 
* Preliminary assesment of questions
* Investigation of possible visualizations/plots
* Refinement/selection of kept research questions
#####  18th to 25th of November:
* Selection of plots / visualizations
* Cleaning, proof-reading
* Plan upcoming objectives

# Questions for TAs
* In what extent are we supposed to spread our analysis, meaning should we focus on a single topic and dive deep or should we cover multiple topics superficially?
* The dataset is highly unbalanced between countries, are we allowed to focus the analysis on the most represented countries?
* Are there some other datasets related to openfoodfacts where we can obtain information about food consumption for each countrys? Could we (maybe) use the dunnhumby dataset?
