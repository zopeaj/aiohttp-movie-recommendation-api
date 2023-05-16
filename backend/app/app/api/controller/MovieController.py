from aiohttp.web import RouteTableDef

movieroutes = RouteTableDef()

@movieroutes.get("/movie/{id}")
def get_movie_id(request):
    pass

@movieroutes.post("/movie")
def post_moive(request):
    pass


