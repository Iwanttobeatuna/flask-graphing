# Python Flask graphing with Plotly
While coding to integrate Plotly graph into web application with Flask, I faced a few coding problems and there are limited resources online regarding this! Fortunately, Professor Malan helped to figure out the problem on CS50 Edx. Hence, I would like to share the code and keep it for future reference!

# Notes
In this example, I decided to plot a stock closing price and stock volume graph vs time graph, specifically AAPL(Apple Inc) graph with real time information collected from Investing.com with the Python library: investpy.
It works for other data too, so feel free to change the framework as you wish. 
If you want to specifically want to plot a stock graph based on what the user have searched, refer Trading Frog for coding reference!

# Tips while integrating Flask with Plotly
##### **1. {% block script %}{% endblock %}**
In layout.html, create a {% block script %}{% endblock %} after the </body> tag to put your javascript code after in the index page.
##### **2. Use plotly.graph_objs as go. Not plotly.express**
I tried multiple ways to integrate plotly.express into flask, but failed. As for what I have experimented, it only work with plotly.graph_objs.
##### **3. On plotting multiple graph on same webpage**
Refer application.py and index.py (GraphJSON and GraphJSON1)


# Happy Coding!
I hope this helps!
