from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import time

"""
Receives the requests and stores the requests and
their arrival time
"""

app = Flask(__name__)
api = Api(app)

# Store POST request information
TRANSFERS = {

}


def abort_if_doesnt_exist(t_id, collection):
    """ Abort if t_id not key within dictionary collection
    """
    if t_id not in collection:
        abort(404, message="Transfer {} doesn't exist".format(t_id))

parser = reqparse.RequestParser()
parser.add_argument('t_id')
parser.add_argument('TimeSent')


# shows a single transfer item
class Transfer(Resource):
    def get(self, t_id):
        abort_if_doesnt_exist(t_id, TRANSFERS)
        return TRANSFERS[t_id]


# shows a list of all transfers, and lets you POST to add new tasks
class TransferList(Resource):
    def get(self):
        return TRANSFERS

    def post(self):
        """ POST response in structure below
        {"id": {
            "TimeSent",
            "TimeReceived"
        }}
        Returns object posted with time received and STATUS_CODE
        """
        # parse response for time sent
        args = parser.parse_args()
        # transfer id
        t_id = args['t_id']
        time_sent = args["TimeSent"]
        time_recieved = time.time()

        # update TRANSFERS list with message number, time sent, and time recieved
        data = {
            t_id: {
            "TimeSent": time_sent, 
            "TimeReceived": time_recieved
            }
        }
        TRANSFERS.update(data)
        return TRANSFERS[t_id], 201


# setup the Api resource routing
api.add_resource(TransferList, '/transfer')
api.add_resource(Transfer, '/transferlist/<t_id>')


if __name__ == '__main__':
    app.run(debug=True)