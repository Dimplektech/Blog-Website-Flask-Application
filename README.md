
# Blog Website Flask Application

A simple Flask-based blogging website that displays posts fetched from an external API and allows users to contact the site owner via email.

## Features

1. **Home Page (`/`)**
   - Displays all blog posts retrieved from an external API.

2. **Post Page (`/post/<int:index>`)**
   - Shows the content of a single blog post based on its ID.

3. **About Page (`/about`)**
   - A static page about the blog or website.

4. **Contact Page (`/contact`)**
   - Users can submit their contact information and message via a form.
   - Sends the form data to the site owner's email using Gmail SMTP.
   - Displays feedback after submission.

5. **Email Integration**
   - Emails are sent via Gmail SMTP.
   - Uses `My_Email` and `PASSWORD` environment variables for secure credentials.

## Technologies Used

- **Flask**: Web framework.
- **Requests**: Fetching blog posts from an external API.
- **SMTP**: Sending emails.
- **SSL**: Secure email connections.
- **Dotenv**: Securely handling environment variables.

## Installation and Setup

1. Clone the repository:  
 ```bash
   git clone https://github.com/Dimplektech/Blog-Website-Flask-Application.git

2.  Install dependencies:
```bash
   pip install -r requirements.txt

3. Create a .env file in the project directory with:
```bash
   My_Email=your-email@gmail.com
   PASSWORD=your-app-password

4.Run the application:
```bash
python app.py

## Directory Structure
    
    blog-flask/
    ├── templates/
    │   ├── index.html      # Home page template
    │   ├── about.html      # About page template
    │   ├── contact.html    # Contact form page
    │   ├── post.html       # Individual blog post page
    ├── app.py              # Flask application
    ├── requirements.txt    # Project dependencies
    ├── .env                # Environment variables (not included in the repository)
    └── README.md           # Project documentation

## API for Blog Posts
    The application fetches blog data from an external API. Replace the URL in the script with your custom API URL if necessary:
 ```bash
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

## Example .env File
  make file
```bash
    My_Email=example@gmail.com
    PASSWORD=yourapppassword
      

 

