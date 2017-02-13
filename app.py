import web

urls = ('/', 'Index', '/contact', 'Contact')

app = web.application(urls, globals())

web.config.debug = True

class Index :
	def __init__(self) :
		self.render = web.template.render('templates/')

	def GET(self) :
		return self.render.index("test de passage de variable", [1,2,3,4])
		#return "Hello world"

class Contact :
	def __init__(self) :
		self.render = web.template.render('templates/')

	def GET(self) :
		return self.render.index("Formulaire de contact dynamique", [])



if __name__ == '__main__' :
	app.run()