Key terms/ideas/concepts:
- Jinja: a templating engine used for rendering templates in Flask web applications
- Templating languages: tools used for writing templates in different languages
- Looping: repeating a block of code multiple times
- Conditionals: executing code based on a certain condition
- Render: convert data into a format that can be displayed
- Inheritance: a way of sharing functionality between templates by creating a base template and inheriting from it
- API overview: a page in Jinja's documentation that provides an overview of the different methods and features available in Jinja
- Filters: Jinja-specific functions that can be applied to a variable in a template using the pipe operator, to modify the variable's output
- Built-in filters: a set of filters that come with Jinja, such as max, min, replace, sort, and sum
- Macros: reusable pieces of templates with logic that can be passed arguments, similar to functions
- Caching: storing data in memory for quick retrieval, useful for portions of a template that are unlikely to change often
- Super: a way of referencing the contents of a parent block in a child template
- Delimiters: special characters used to denote statements, expressions, and variables in a template

Sure, here's an example of how to use a Jinja filter in Flask:

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tweets = ['I love Jinja', 'Flask is awesome', 'Python is the best']
    return render_template('index.html', tweets=tweets)

if __name__ == '__main__':
    app.run()

```

And in the `index.html` file, we can use the `max` Jinja filter to display the tweet with the maximum length:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Jinja Example</title>
  </head>
  <body>
    {% for tweet in tweets %}
      <p>{{ tweet }}</p>
    {% endfor %}
    <p>The longest tweet is: {{ tweets|max }}</p>
  </body>
</html>
```

This will display all the tweets in the `tweets` list and then display the longest tweet using the `max` filter.
