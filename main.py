from website import setup

app = setup()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)