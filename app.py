from website import __init_

app = __init_.create_app()

if __name__ == '__main__':
    app.run(debug=True)
