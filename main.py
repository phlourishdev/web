from fasthtml.common import *

hdrs =  (MarkdownJS(),
        Link(rel='stylesheet', href='assets/css/colors.css', type='text/css'),
)

app, rt = fast_app(hdrs=hdrs, live=True)

"""
home
"""

with open('assets/markdown/home.md') as file:
    md_home = file.read()

@rt('/')
def get(req):
    return Titled("phlourish dot dev", Div(md_home,cls="marked"))

"""
handle 404 -> redirect to root site
"""

@app.exception_handler(HTTPException)
async def handle_404(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return RedirectResponse("/")
    return await handle_404(request, exc)

serve()
