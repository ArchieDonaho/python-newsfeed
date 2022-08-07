# use "from ... import" to import Flask
from flask import Flask
# import our home variable from the routes package
from app.routes import home, dashboard

# "define" the "create_app" function
# functions use indentations to indicate if something is within the function
def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/') # serve any static resources from the root directory
  app.url_map.strict_slashes = False # Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route)
  app.config.from_mapping(SECRET_KEY='super_secret_key') # define our secret key env variable
  # @app.route('/hello') # the "decorator" turns the hello() function into a route
  # def hello():
  #   return 'hello world'

  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app
