#Try to Create one server with multiple PORT Number:
import logging
import rollbar
import os
from flask import Flask
app=Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.before_first_request
def add_monitoring():
    return rollbar.init(os.environ.get('ROLLBAR_SECRET'))
    return rollbar.report_message('Rollbar is configured correctly')
@app.route('/server')
def server():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.debug('Debug level logs')
    return 'Server Home'
if __name__=='__main__':
    app.run(host='localhost',port=8080,debug=True)
