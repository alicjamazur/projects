from bottle import * 
from pprint import pprint
import time 
import algebra
import os 


@route('/')
def welcome():
    response.set_header('Vary', 'Accept')
    response.set_cookie()
    pprint(dict(request.headers))

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'

    response.content_type = 'text/plain'
    return 'Hi There!'

@route('/now')
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=10')
    return time.ctime()

@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()


secret = 'celo eh o amor da minha vida'

@route('/area/circle')
def circle_area_service():

    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'Last visited: {last_visit}')

    response.set_cookie('last-visit', time.ctime(), secret=secret)

    pprint(dict(request.query))

    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
       return e.args[0]
    area = algebra.area_circle(radius)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html' 
        return f'<p> The area is <em> {area} </em> </p>'
    else:
        return dict(area=area, radius=radius, service=request.path)

#### File Server

file_template = """\
    <h1> List of files in <em> Pub-Sub App </em> directory </h1>
    <hr>
    <ol>
        % for file in files:
            <li> <a href = "files/{{file}}"> {{file}} </a>  </li>
        % end
    </ol>
    """

@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir()
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return dict(files=files)
    return template(file_template, files=files)


@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, '/home/alicja/projects/alicja/projects/pub-sub-app')

if __name__ == '__main__':

    run(hostname='localhost', port=8080)
