# Instagram Social Network

This project is a simple and small social media platform called Instagram, where users can perform the following actions and benefit from these features:

- Users can have their own profile page with a username, profile picture, and bio.
- Users can view the profiles of other individuals and send them friend requests or follow them.
- Users can create posts containing relatively long texts and multiple images, accompanied by a title and categorization tags.
- Users can like, dislike, and comment on posts.
- Users can follow specific categorization tags in addition to following other users.
- Users who are not logged in should only have the ability to view posts and search for users by username.
- Users should have the ability to archive their posts or deactivate their accounts for privacy reasons.

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- SQLite/MySQL/PostgreSQL (choose the appropriate database for your needs)

## Setup and Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd instagram-social-network`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Apply the database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`
8. Open your web browser and access the application at `http://localhost:8000`

## Usage

1. Sign up for a new account by providing a username, password, profile picture, and bio.
2. Log in to your account.
3. Customize your profile by adding/editing your profile picture and bio.
4. Explore other users' profiles and send friend requests or follow them.
5. Create new posts by adding text content, images, a title, and categorization tags.
6. Interact with posts by liking, disliking, and commenting on them.
7. Follow specific categorization tags to see related posts in your feed.
8. Archive posts or deactivate your account if desired.

## Contributing

Contributions to the Instagram Social Network project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

The Instagram Social Network project is open-source and available under the [MIT License](LICENSE).

## Contact

For any inquiries or further information, please contact danaee4421@gmail.com

## Diagram
![Instagram Diagram.png](utils%2FInstagram%20Diagram.png)