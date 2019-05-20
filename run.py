from baitu import create_app

app = create_app()

#cambiar port=5000 por host='0.0.0.0' para despligue

if __name__ == '__main__':
    app.run(debug=True, port=5000)
