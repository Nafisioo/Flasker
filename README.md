# Flasker

Flasker is a web application built using the Flask framework. This project demonstrates my understanding of web development, Python, and backend integration.

## Features

- **User Authentication**: Secure login and registration system.
- **Database Integration**: Utilizes SQLAlchemy for ORM.
- **Dynamic Routing**: Displays content based on user interactions.
- **Template Rendering**: Uses Jinja2 templating engine for dynamic content.
- **API Integration**: Integrates with third-party APIs to fetch and display data.
- **Responsive Design**: Ensures the app looks good on all devices.
- **Error Handling**: Comprehensive error handling for better user experience.
- **Testing**: Unit tests to ensure the functionality of key components.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Nafisioo/flasker.git
    cd flasker
    ```

2. Create a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

5. Initialize the database:

    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Run the application:

    ```sh
    flask run
    ```

## Usage

After running the application, navigate to `http://127.0.0.1:5000/` in your web browser. You can register a new user, log in, and explore the features of the application.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions, feel free to contact me at nafisebahoosh3@gmail.com.
