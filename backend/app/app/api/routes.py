from app.api.controller.MovieController import movieroutes

def setup_routes(app):
    app.add_routes(movieroutes)
