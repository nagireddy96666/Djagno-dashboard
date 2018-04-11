from usrauth.app.views import app, hello_app, create_user, get_users, get_one_user, update_user, delete_user, \
    get_any_user

app.add_url_rule('/', 'hello', hello_app)
app.add_url_rule('/create_user', 'create_user', create_user, methods=["POST"])
app.add_url_rule('/get_users', 'get_users', get_users, methods=["GET"])
app.add_url_rule('/get_one_user/<key>/<value>', 'get_one_user', get_one_user, methods=["GET"])
app.add_url_rule('/get_any_user/<key>/<value>', 'get_any_user', get_any_user, methods=["GET"])
app.add_url_rule('/update_user/<user_id>', 'update_user', update_user, methods=["PUT"])
app.add_url_rule('/delete_user/<user_id>', 'delete_user', delete_user, methods=["POST"])


if __name__ == '__main__':
    # app.debug = True
    app.run(debug = True)
    # app.run()