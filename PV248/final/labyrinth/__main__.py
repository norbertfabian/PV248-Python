from flask import Flask, request, abort, json
from dijkstra import graph, solver

app = Flask(__name__)


def find_shortest(start, end, rooms, corridors):
    try:
        _graph = graph.Graph(rooms, corridors)
        solution = solver.solve(_graph, start, end)
    except Exception as error:
        solution = repr(error)
    return create_response(solution)


def create_response(solution):
    if isinstance(solution, str):
        response_body = {'solution': None, 'length': None, 'error': solution}
    else:
        response_body = {'solution': solution, 'length': len(solution), 'status': 'OK'}
    return json.dumps(response_body)


@app.route('/', methods=['GET', 'POST'])
def process_request():
    if request.method == 'GET':
        return '<h1>Labyrinth</h1>'

    if request.method == 'POST':
        body = request.get_json()
        return find_shortest(body['start'], body['end'], body['rooms'], body['corridors'])

    abort(405)


if __name__ == '__main__':
    app.run()
