import web
from web import form

# Resources:
# http://webpy.org/form

render = web.template.render('templates/')
urls = ( '/', 'index' )
app = web.application(urls, globals())

class index:
    myform = form.Form(
        form.Textbox("Your Number",
                     form.notnull,
                     form.regexp('\d+', 'Must be an int'),
                     form.Validator('Must be more than 5', lambda x:int(x)>5)),
        form.Button("submit", type="submit"))
    def GET(self):
        web.header('Content-Type', 'text/html')
        form = self.myform()
        result = "<html><body>"
        close = "</body></html>"
        if form.validates():
            n = int(form["Your Number"].value)
            result +=  "<p>%d**2 = %d</p>"%(n,n**2)
        return result + '<p><form>' + form.render() + '</form></p>' + close


if __name__=="__main__": app.run()
