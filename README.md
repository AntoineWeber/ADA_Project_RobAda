# Jekyll data story branch

For our datastory, we decided to use [Jekyll](https://jekyllrb.com/) to generate a static website, hosted on [GitHub pages](https://pages.github.com/).

The datastory is accessible [here](https://antoineweber.github.io/ADA_Project_RobAda/).

This branch is meant only for writing the content of the datastory and handling the website. The data analysis and plot generation is done on the `master` branch. 

## Edit the datastory

Simply edit the file `story.md`, as any Markdown file.

To include plotly figures: add the following code snippet:
```HTML
{::nomarkdown}
<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~inutile/plot_number.embed" height="525" width="100%"></iframe>
{:/}
```

## Credits

The website template is based on [Moon](https://github.com/TaylanTatli/Moon), modified at our convenience to include plots.
