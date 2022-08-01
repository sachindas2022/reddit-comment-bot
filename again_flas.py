from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
@app.route('/blogs')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.debug('Debug level logs')
    return f"Welcome to the Blog"
@app.route('/home')
def home():
    app.logger.info('Info level log')
    app.logger.debug('Debug level log')
    app.logger.warning('Warning level log')
    return f"{app.logger.warning}Welcome to The Blog home Page"
if __name__=='__main__':
    app.run(host='localhost',port=8180,debug=True)