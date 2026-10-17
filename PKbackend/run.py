from app import create_app

# função criate_app
app = create_app()

# Loop
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)