from flask import Flask
from app import create_app

app= create_app()

if __name__ == "__main__":
    app.run(debug=True) # aqui se ejecuta la aplicacion, si se pone debug=True, se recarga automaticamente al hacer cambios en el codigo

