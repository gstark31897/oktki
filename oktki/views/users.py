from flask import Blueprint, render_template, abort, redirect, url_for

from ..models.users import User, CreateUserForm

blueprint = Blueprint('Users', __name__, template_folder='templates/users', url_prefix='/users')

@blueprint.route('/create', methods=('GET', 'POST'))
def index():
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User.create(form.name.data, form.password.data)
        return redirect(url_for('Users.user', title=page.title))
    return render_template('users/create.html', form=form), 200

