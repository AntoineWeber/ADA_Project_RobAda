---
layout: story
title: "Organic, you said?"
feature: './assets/img/featureimg.jpg'
permalink: /story/
---

Nowadays, most products come in two flavors: **organic** or **standard**. Consequently, while shopping, we are always confronted to organic products whose [costs are about 20-40% higher](https://www.consumerreports.org/cro/news/2015/03/cost-of-organic-food/index.htm) than their standard equivalent. Such a price increase must imply a more responsible production and therefore better product quality, right? 

<br><br>

<b><i><center><font color="#00864B"><font size="7">So concretely, are organic products healthier than regular ones? </font></font></center></i></b>

<br><br>

<b><center><font size="5"> Open Food Facts </font></center></b>

To investigate, we based our exploration on the [Open Food Facts](https://fr.openfoodfacts.org/) dataset, regrouping millions of products from all around the world, although the majority of the products originate from France or the USA. It provides insights on the products' composition, nutritional score, the place they are sold and many other information.  A complete list of all the available fields can be found [here](https://static.openfoodfacts.org/data/data-fields.txt).

There is even an [app](https://play.google.com/store/apps/details?id=org.openfoodfacts.scanner&hl=fr_CH) based on the dataset which allows the user to scan the barcode of a product and immediately get its evaluation.
<br><br>

<b><center><font size="5"> Product categories </font></center></b>

To correctly compare the **organic** and **standard** categories, one should be careful with what products are actually being compared, to avoid comparing oil with salad, for instance. Hence, to carry out a more rigorous analysis, we split the Open Food Facts dataset into *8 categories of products*:
* Meat, fish, egg
* Fruit, vegetable
* Cereal based
* beverages
* Dairy
* Oil, butter
* Spices, salsa, condiments
* Sugary products

All these categories actually embed different subcategories that were merged for our analysis. If the reader is curious about which kind of products goes into each category, please have a look at the following word-clouds. The bigger the word, the most common the product. Also, feel free to zoom in for a better readability.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/36.embed" height="650" width="100%"></iframe>
Now that the data is ready, let's dive into the main question of this analysis being:

{% include section.html text="Is Organic better?" image_url="images/carrot.jpg" %}

Are organic products really healthier? Let us try to get a first intuition by observing the scores of organic and standard products for different food categories.

<br><br>
<b><center><font size="5"> French nutrition grade </font></center></b>

The French Nutri-Score is a nutrition label that converts the nutritional value of a product into a simple letter. There are 5 letters in total, each with its own color, A being the best and E the worst.

<img src="{{ site.url }}/images/nutri-score-a.png"  alt="Nutri-score"   width="100"  />

The score is based on a formula that takes into account the properties to avoid, such as high energy values, high sugar content, saturated fats and salt; and the properties to favor, such as the amount of fibers, proteins, fruit, vegetables and nuts.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/10.embed" height="525" width="100%"></iframe>
Interestingly, both organic and standard products have similar grades distribution shapes. In particular, we observe that the organic distributions are most of the time shifted towards better grades! Some exceptions exist for the beverages for instance but this observation holds in general.

This is a good start for the organic category which seems to surpass the standard category in terms of French nutritional score. Now let's observe if this specific nutrition score is in accordance with the UK nutrition score.

<br><br>
<b><center><font size="5"> UK nutrition grade </font></center></b>


The UK score is essentially a finer version of the French score. Its range goes from -10 (best) to 40 (worst).

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/15.embed" height="525" width="100%"></iframe>
This score, also displays similar distributions between the two classes of products. Indeed, the shift of the organic products towards better scores is again visible here. This may emerge from the fact that both nutrition scores rely on the same type of rules mostly based on the compositions of the products.

Hence in terms of nutrition score, the organic products do not fail to their reputation of being healthier than standard products. Now let's dig a bit deeper with other analysis to check whether this statement remains true! Let's dig into the Nova group.

<br><br>
<b><center><font size="5"> Nova group </font></center></b>

The NOVA group helps people classify foods according to the extent and purpose of the processing they underwent.

<img src="{{ site.url }}/images/nova.png"  alt="nova"   width="100"  />

The values of this group are within the interval {1,2,3,4}:

* Group 1 - Minimally processed foods (parts of plants or animals)
* Group 2 - Processed culinary ingredients (issued from simple processes such as pressing, refining, grinding, milling or drying)
* Group 3 - Processed foods (bottled vegetables, canned fish, fruits in syrup, cheeses or freshly made breads, with additions of salt, oil, sugar or other substances)
* Group 4 - Ultra-processed food and drink products (soft drinks, sweet packaged snacks, pre-cooked meals)

With these definitions, we can state that the higher the nova group, the less natural the product. Moreover, as group 4 contains the most processed products, it also contains the less healthy products.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/6.embed" height="525" width="100%"></iframe>
Different interesting observations can be established here! First, we observe that generally both categories show relatively high levels of processing, being that both organic and standard categories have a lot of products in the groups 3 and 4. But besides that, we also observe that for some categories there is a clear difference between the tendency of the organic and standard products! The most striking category is the beverage one where we clearly observe opposite tendencies. The organic products are mostly present in the nova group 1 while the complete opposite can be observed for the standard products which are mostly present in the 4th group. Moreover, the 4th group is **for all categories** composed of a bigger proportion of standard products compared to organic ones.

Hence, here one can state that in terms of nova groups, the same analysis as for the nutrition scores can be established, being that **the organic products surpass the standard ones!**


{% include section.html text="So what now?" image_url="images/tomato.jpg" %}

Thus far, we analyzed different pre-computed scores or groups. All the different metrics were leaning towards the win of the organic products. The goal now is to try to analyze more raw attributes of the different products. For the sake of this study, we focused our sight on the two following types of attributes:

- Nutrient composition
- Additives

Although the nutrient composition directly impact the nutritional scores, it is interesting to go a bit deeper into the products composition.

<br><br>
<b><center><font size="5">  Nutrient composition </font></center></b>

Let us see for ourselves the main nutrients found in the two categories of products. This information is typically displayed on the packaging of most products like in the example below.

<img src="{{ site.url }}/images/nutrient_table_focus.png"  alt="Nutriment table"   width="200"  />

The average quantity in grams for 100g of the main nutrients contained in the products is shown in the following figure, again for each category.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/21.embed" height="525" width="100%"></iframe>
There are quite a few interesting remarks that can be made regarding the results:

* There are more fibers in organic products, no matter the category. This is highlighting the fact that the products are less processed than regular ones.
* Conventional products containing meat, fish, and egg have more saturated fat than organic ones. The reason for this difference is mainly the diet of the animals. For example, animals that eat more grass have lower fat levels than animals that are fed processed cattle feed. This also can be seen with dairy products.
* Interestingly, organic products have more protein than the conventional ones for all the categories except for meat, fish, and egg based products.
* There is no significant difference in sugar between conventional and organic products for the majority of categories.

Hence the products' nutrient compositions also lean towards the organic products being healthier. As stated before, the nutrition scores take into account part of the nutrient compositions which may explain why the unanimity is still present here.

Finally, let's dig into a big subject being the **additives**. Will we again observe that the organic products surpass the standard ones with this analysis?

<br><br>
<b><center><font size="5">  Additives </font></center></b>

Additives are often source of controversy, and some are even believed to be cancerous. Let us recall the main types of additives, as listed in [Wikipedia](https://en.wikipedia.org/wiki/Food_additive) (check [this page](https://en.wikipedia.org/wiki/E_number) for a more in depth listing):

- **Antioxidants/acidity regulators** (E300–E399, used for controlling the [pH](https://en.wikipedia.org/wiki/PH) of foods for stability or to affect activity of enzymes)
- **Colorants** (E100–E199, enhance or add colors to the product)
- **Flavor enhancers** (E600–E699, enhance the food's existing flavor. Some flavor enhancers have their own flavors that are independent of the food.)
- **Glazing agents, gases and sweeteners** (E900–E999, provide a shiny appearance or protective coating to foods)
- **Preservatives** (E200–E299, prevent or inhibit spoilage of food due to [fungi](https://en.wikipedia.org/wiki/Fungus), [bacteria](https://en.wikipedia.org/wiki/Bacteria) and other [microorganisms](https://en.wikipedia.org/wiki/Microorganism))
- **Thickeners, stabilizers and emulsifiers** (E400–E499, increase the product's [viscosity](https://en.wikipedia.org/wiki/Viscosity) without substantially modifying its other properties)
- **pH regulators and anti-caking agents** (E500–E599, keep powders such as milk powder from caking or sticking)

Some of these additives are natural while some others are chemically synthesized and added to the products to enhance their flavor, appearance or texture or even to extend the products' life. Hence, while some are indeed harmless, it is not clear whether some others should be avoided at all costs or consumed with moderation. Due to the ambiguity of whether an additive may be harmful or not, it can be considered a good practice to try to consume as little additives as possible.

Now let's observe how these additives are represented in our organic and standard products! To ensure a fair comparison between them, each product categories defined above has been investigated independently to avoid comparing cats with dogs.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/8.embed" height="525" width="100%"></iframe>
Organic products should, by definition, undergo as little processing as possible. Hence, they should contain less additives, right ? Well, look at the previous plot! The proportions of additives is in general drastically different when looking at organic products vs. standard products. Indeed, as stated before, our intuition was right! **There is in general much less additives in organic products versus standard ones.** In particular, there is almost no flavor enhancers in organic products! Although, there are some exceptions, such as the anti-caking agents in the cereal based category, the general tendency is that the shape drawn by organic products is inscribed in the one of the standard products. This nicely illustrates the smaller general amount of additives in organic products.


{% include section.html text="Conclusion" image_url="images/eggplant.jpg" %}

We hope that the analysis and figures provided in this data story have helped you  understand more about food products, and the difference between organic and standard products.  

Overall, the analysis we carried out tends to show a tangible positive difference  in favor of organic products compared to standard ones, and the results are quite coherent across all categories.  

The organic products have in average better nutritional scores, both for the French and British ones. This is arguably relevant, as there could be two explanations: either the organic products are indeed healthier, or for marketing reasons only  organic products with high nutritional score are sold, because otherwise customers  would be less inclined to pay more for these.

Beyond the difference in nutritional scores, we also observed a noticeable difference when diving in the composition in nutrients. In particular, organic products tended  to contain more fibers and proteins than standard products, which would go in the  direction that they are less processed. This theory would also be in adequacy with the distribution of products in the Nova groups. The proportion of organic products in the less processed groups (1st and 2nd) was higher than for standard products, and  similarly there was a lower proportion of products in the 4th group.

We also investigated the presence of different categories of additives in the products. In general, there are less additives in organic products, and especially less  conservatives and flavor enhancers. Even though the medical experts don't all agree  on the potential harm of all these additives, it is often advised to be limit them to the strict necessary. Let’s not forget that not so long ago, [cigarettes were advertised as being healthy](https://www.buzzfeed.com/copyranter/healthy-cigarette-ads). So if you want to make sure to ingest as little additives as possible, it is pretty clear that you should favor organic products over standard  products !

So all in all, should we all stop eating standard products in favor of organic products? Well, there is no need to go to that extreme. While our results tend to show that organic products are healthier, the results must be looked at carefully. Indeed, since we worked on the Open Food Facts dataset, which is crowd-sourced, there were quite a lot of missing information and there could be some erroneous. More importantly,  there are much more standard products than organic products, which means that the  data is more reliable for the former than for the latter. Thank you for reading this story, and eat well :) !



The team: <br>
* **Lucas Wälti** : Master student in Robotics
* **Mohamed Hedi Fendri**: Master student in Robotics
* **Thomas Havy**: Master student in Robotics
* **Antoine Weber**: Master student in Robotics
