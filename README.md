# Python Flask graphing with Plotly
While coding to integrate Plotly graph into web application with Flask, I faced a few coding problems and there are limited resources online regarding this! Fortunately, Professor Malan helped to figure out the problem on CS50 Edx. Hence, I would like to share the code and keep it for future reference!

# Tips while integrating Flask with Plotly
##### 1. {% block script %}{% endblock %}
In layout.html, create a {% block script %}{% endblock %} after the </body> tag to put your javascript code after in the index page.
##### 2. Use plotly.graph_objs as go. Not plotly.express
I tried multiple ways to integrate plotly.express into flask, but failed. As for what I have experimented, it only work with plotly.graph_objs.
##### 3. On plotting multiple graph on same webpage
Refer application.py and index.py (GraphJSON and GraphJSON1)

# Happy Coding!
I hope this helps!
