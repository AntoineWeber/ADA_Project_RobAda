# Free Diving into Food Facts

Nowadays, most products come in two flavors: bio or non-bio. Consequently, while shopping, we are always confronted to bio products whose costs are about 20-40% higher than their non-bio equivalent. Such a price increase must imply a more responsible production and therefore better product quality, right? **So concretely, are bio products healthier than regular ones?** 

To explore this question, let us go through the [Open Food Facts](https://fr.openfoodfacts.org/) dataset, regrouping millions of products from all around the world, while the majority of the products originate from France and the USA. The dataset provides insights on their composition, nutritional score, the place they are sold and many other information.  A complete list of all the fields available can be found [here](https://static.openfoodfacts.org/data/data-fields.txt).

There is even an [app](https://play.google.com/store/apps/details?id=org.openfoodfacts.scanner&hl=fr_CH) based on the dataset which allows the user to scan the bar-code of a product and immediately get an evaluation of the product. 

<img src="wordcloud.png" alt="wordcloud" style="zoom:80%;" />

Let us start our investigations with the nutrition scores. But first, some definitions. 

## Nutritional scores

Open Food Facts contains two scores that can be used to evaluate a product: 

- **French and UK Nutri-score**: The Nutri-Score is a nutrition label that converts the nutritional value of products into a simple code consisting of 5 letters, each with its own color. The aim of this code is to help consumers take into account the nutritional quality of the products they are buying.

  Each product is then awarded a score based on a formula that takes into account the nutrients to avoid (energy value and the amount of sugars, saturated fats and salt typically) and the positive ones (the amount of fiber, protein, fruit, vegetables and nuts).  The UK score is essentially a finer version of the French score. 

  Thanks to these scores, it is possible to see at a glance which products are recommended and which should be avoided.

  <img src="nutri_score_def.png"  alt="wordcloud"   style="zoom:90%;"  />

  

- **NOVA group**:  NOVA helps people group foods according to the extent and purpose of the processing they undergo. Food processing as identified by NOVA involved physical, biological and chemical processes that occur after foods are separated from nature, and before they are consumed or used in the preparation of meals. 

   The values of this group are {1,2,3,4}

  - Group 1 - **Unprocessed or minimally processed foods**, typically edible parts of plants (seeds, fruits, leaves, stems, roots) or of animals (muscle, offal, eggs, milk), and also fungi, algae and water, after separation from nature.
  - Group 2 - **Processed culinary ingredients**, such as oils, butter, sugar and salt, which are substances either derived from Group 1 or from nature by processes that include pressing, refining, grinding, milling and drying.
  - Group 3 - **Processed foods, such as bottled vegetables**, canned fish, fruits in syrup, cheeses and freshly made breads, are made essentially by adding salt, oil, sugar or other substances from Group 1 or Group 2.
  - Group 4 - **Ultra-processed food and drink products**, such as soft drinks, sweet or savory packaged snacks, reconstituted meat products and ready-to-cook frozen meals. 

## Is Bio better?

Nowadays, most products come in two flavors: bio or non-bio. Consequently, while shopping, we are always confronted to bio products whose costs are about 20-40% higher than their non-bio equivalent. Such a price increase must imply a more responsible production and therefore better product quality, right? 

But are bio products really healthier? Let us try to get a first intuition by observing the score on bio and non-bio products for different food categories. 

### French nutrition grade

To do so, let us observe groups of products that were chosen based on their categories. As an example, one could observe meat related products independently. 

Let us start with their french nutrition grade:

<img src="nutrition_grade_fr_meat.png" alt="nutrition_grade_fr_meat" style="zoom:80%;" />

<img src="nutrition_grade_fr_dairies.png" alt="nutrition_grade_fr_dairies" style="zoom:80%;" />

Interestingly, while bio and non-bio scores distributions are similar, the bio products have greater proportions of products related to better scores while this tendency is inverted for the non-bio products. This is a first hint that bio products may indeed be healthier. 

What about another score? Let us look at what the UK nutrition score has to tell us.

### UK nutrition grade

<img src="nutrition-score-uk_100g_meat.png" alt="nutrition-score-uk_100g_meat" style="zoom:80%;" />

<img src="nutrition-score-uk_100g_dairies.png" alt="nutrition-score-uk_100g_dairies" style="zoom:80%;" />

The same conclusion arises from these last graphs. While both distributions have similar shape, bio products have larger proportions of products with better nutrition score than non-bio products. 

### Nova group

Does the degree of transformation of the products have something to do with it? Let us see if any tendency is observable:

<img src="nova_meat.png" alt="nova_meat" style="zoom:80%;" />

<img src="nova_dairies.png" alt="nova_dairies" style="zoom:80%;" />

Well... While both categories show relatively high levels of processing, the bio products tend to still have slightly better scores. They indeed tend to be less processed, which contributes to their nutritional scores. 

### So what now?

The previous scores tend to be in favor of the bio products. 

**Do other properties also corroborate this claim?** Let us go through 2 more criteria: 

- Nutrition facts
- Additives

### Why is bio better then?

#### Nutrition facts 

Although the nutrition facts directly impact their nutritional scores, it is interesting to go a bit deeper into the products composition. 

**Goal**: Identify the nutriments that really impact both classes (hence find what makes the difference between the two classes).  Find out where the difference is for each class. 

#### Additives

>  **TODO:** Add correlation map. Illustrate whether additives have impact on nutrition scores. 

What about the additives then? They are often source of controversy, and some are even believed to be cancerous. Let us recall the main types of additives, as listed in [Wikipedia](https://en.wikipedia.org/wiki/Food_additive) (check [this page](https://en.wikipedia.org/wiki/E_number) for a more in depth listing): 

- **Antibiotics** (E700–E799)
- **Antioxidants/acidity regulators** (E300–E399, used for controlling the [pH](https://en.wikipedia.org/wiki/PH) of foods for stability or to affect activity of enzymes) 
- **Colorants** (E100–E199, enhance or add colors to the product)
- **Flavor enhancers** (E600–E699, enhance the food's existing flavor. Some flavor enhancers have their own flavors that are independent of the food.)
- **Glazing agents, gases and sweeteners** (E900–E999, provide a shiny appearance or protective coating to foods) 
- **Preservatives** (E200–E299, prevent or inhibit spoilage of food due to [fungi](https://en.wikipedia.org/wiki/Fungus), [bacteria](https://en.wikipedia.org/wiki/Bacteria) and other [microorganisms](https://en.wikipedia.org/wiki/Microorganism))
- **Thickeners, stabilizers and emulsifiers** (E400–E499, increase the product's [viscosity](https://en.wikipedia.org/wiki/Viscosity) without substantially modifying its other properties)
- **pH regulators and anti-caking agents** (E500–E599, keep powders such as milk powder from caking or sticking)

Considering the same groups of products, let us observe the presence of additives in each category. 

<img src="radar_meat.png" alt="radar_meat" style="zoom:80%;" />

<img src="radar_dairies.png" alt="radar_dairies" style="zoom:80%;" />

That is interesting! The proportions of additives is in general drastically different when looking at bio products vs. regular ones. Less additives are to be found in bio products. But do they actually impact the nutritional scores? 

## Tout doux ma gueule

> **TODO:** Sum up the bar plots of the scores into box-plots or plots with error bars respectively. 

> **TODO:** What about some observations about the composition itself?

> *Hypothesis*: companies that make the effort to produce bio products also the effort to make healthy products. 