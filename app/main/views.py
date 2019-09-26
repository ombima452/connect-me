from flask_login import login_required


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    return render_template('index.html')