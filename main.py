# This code adds custom REST api handler at runtime to a running Streamlit app
#

from tornado.web import Application, RequestHandler
from tornado.routing import Rule, PathMatches
import gc
import streamlit as st


@st.cache_resource()
def setup_api_handler(uri, handler):
    print("Setup Tornado. Should be called only once")

    # Get instance of Tornado
    tornado_app = next(o for o in gc.get_referrers(Application) if o.__class__ is Application)

    # Setup custom handler
    tornado_app.wildcard_router.rules.insert(0, Rule(PathMatches(uri), handler))
    
# === Usage ======
class HelloHandler(RequestHandler):
    # def set_default_headers(self):
    #     self.set_header("Access-Control-Allow-Origin", "*")
    #     self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    #     self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self):
        # Handle pre-flight OPTIONS request
        self.set_status(204)
        self.finish()

    def get(self):
        self.write({'message': 'hello world'})

    def post(self):
        self.write({'message': 'post message'})


# This setup will be run only once
setup_api_handler('/api/hello', HelloHandler)
