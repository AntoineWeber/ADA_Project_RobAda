# Organic, you said?

[Link to the data story](https://antoineweber.github.io/ADA_Project_RobAda/).

# Abstract
While everybody buys and consumes numerous food-related products every day, little care is given in the precise products’ compositions.   
For the sake of this study, we decided to focus our effort on the [Open Food Facts database](https://world.openfoodfacts.org/data) regrouping the information of a very broad variety of products, including their nutrition facts and derived nutrition scores from different standards, such as the [UK Food Standards Agency](https://en.wikipedia.org/wiki/Food_Standards_Agency)'s (FSA) or the same score but derived from the French market

In particular, this study is focused on the quantitative **comparison of organic and standard products. Is there a difference between them ?** It is generally assumed that organic products are healthier and hence should be favored for our food habits. But is it really the case ? Is there a real and significant difference between an organic product and a standard one ? If yes, what is the biggest contributing factor of difference ?

These fundamental questions were assessed within this study. The developed data story will guide the reader through this comparison journey.

# Research questions
To compare organic and standard products, the group had to define different factors or attributes present in the dataset. For the sake of this study, these are the selected fundamental questions:

  1. Is there a difference of nutrition score between these two categories as well as for their respective nova groups ?
  2. Are there any differences in terms of presence of additives ?
  3. Is the difference in processing of these products induce a difference in terms of their composition ?

Each of them were investigated individually to observe whether a distinction between these two product categories could emerge from them. Then, the conclusion of this work regroups all the different analysis to draw conclusions on the main question being: Is there a difference between these products ?

# Dataset
Lettuce analyse this dataset: [Open Food Fact database](https://world.openfoodfacts.org/data).  
The dataset is built as part of a collaborative project to build a free and open database of alimentary items commercially available worldwide. It is stored as a `.csv` file containing several fields (not always indicated), typically the list of ingredients of the product, the nutritional table (usually indicated on the back of the product), nutritional scores, the brand and distributor, the packaging of the product, and more. The raw dataset is very unbalanced in terms of organic and standard products. Hence, the data cleaning and pre-processing part was crucial in order to provide meaningful and un-biased analysis.

To complement this dataset and filter the different products into main categories such as dairies, beverages, etc... the data present in [this website](http://www.synonymy.com/synonym.php) was scrapped. Indeed, grouping the products into categories is also very usefull to compare only comparable organic and standard products between them. With this processing, salad will never be compared with oil for instance. 


# Work repartition

**Thomas Havy**: Jekyll & HTML master / Wordclouds / Web scrapping / Interactive plots / Nutritional scores analysis.

**Mohamed Hedi Fendri**: Data cleaning / Data processing / Correlation master / Wordclouds.

**Lucas Wälti**: Debugging of data processing / Data story writer / Categories creator / Merge master.

**Antoine Weber**: Data processing / Additives analysis / Interactive plots master / Data story writer.

These are representative subjects. As a matter of facts nearly all team members helped and participated for all parts of this project. It is hence expected that all team members will participate to prepare the final presentation.
