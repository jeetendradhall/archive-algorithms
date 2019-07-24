## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/jeetendradhall/algorithms/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a 
* **lightweight** 
	* and easy-to-use syntax for styling your writing.
* It includes conventions for

![Algo Design](https://github.com/jeetendradhall/algorithms/raw/master/heuristic.png "Algorithm Designs")

v3

Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

```markdown
#read data
df_data = pd.read_csv ('./datasets/boston-housing.csv')
#train and test data separation
msk = np.random.rand(len(df_data)) < 0.9
df = df_data[msk]
df_test = df_data[~msk]
df.head (2)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/jeetendradhall/algorithms/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
