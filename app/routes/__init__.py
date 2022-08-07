# "find the module named 'home' in the current directory, import the 'bp' object from there, and rename it to 'home'"
from .home import bp as home
# also import the dashboard
from .dashboard import bp as dashboard