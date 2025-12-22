# Quality Shares

- [Live website on Heroku](https://quality-shares-3f67cc1f7e60.herokuapp.com/) 

Quality Shares is an informative and educational website for "quality investors"; in other words, investors seeking high-quality income and growth stocks.

I built the site for Jim Smith, a (fictional) financial analyst with 20 years’ experience. 

Jim was looking for a challenge and wanted to start his own business to leverage his extensive knowledge as an investor and analyst. He likes writing, so he wanted to launch a paid blog/newsletter business.

Jim already has a Substack where he publishes free weekly articles to build up his audience. He wanted to move from Substack to a bespoke website to give him (a) more control over the platform’s structure, and (b) more flexibility with potential future product offerings, such as books, courses, coaching, etc.

[IMAGE SHOWING THE SITE'S RESPONSIVENESS]

## Table of Contents

- [User Experience Design](#user-experience-design)
- [Technologies Used](#technologies-used)
- [Data Model](#data-model)
- [Features](#features)
- [Project Management](#project-management)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience Design

I designed the site using the "five planes" UX design process.

### Strategy Plane

The strategy plane is centered around discovering the product owner's and users' goals.

#### Product Owner Goals

- Primary goal:
  - To give Jim a bespoke, flexible platform that will help him grow his business.
- Supporting goals:
  - To raise awareness of Jim's business, so that more users enter the top of the sales funnel.
  - To build trust with users, so they're more likely to buy products (paid newsletters, e-books, etc.) from Jim in the future.
  - To publish free content for its SEO value and to nurture users with educational and informational content.
  - To make it easy for users to sign up for premium content.
  - To make it easy for users to subscribe to email newsletters, so we remain top of mind with leads.

#### User goals

- Primary goal:
  - To improve their investment returns.
- Supporting goals:
  - To learn more about investing and become a better investor.
  - To have access to information about companies, stock prices and stock markets that will help them make better-informed investing decisions.
  - To discuss investing with like-minded investors.

### Scope Plane

The scope plane is obviously all about defining the scope of the project; what is in scope and what is out of scope. 

#### Epics

There were several high level requirements (or epics) that Jim wanted:

- Blog:
  - A Substack-like blog where Jim can publish content and build trust with users, and where users can find useful information to read. The blog should also allow user to interact, via comments or a chat system, to build more trust.
- Info pages:
  - Pages or sections on the site, with information about Jim, about his investment strategy or portfolio, and about how to contact him. These should build further trust, which Jim hopes to turn into revenues in the future.
- User sign-up:
  - A way for users to sign up to get e-mail newsletters and other premium content, which Jim intends to monetise at a later stage.

I broke the above epics down into user stories to add detail to the scope of the project. As the project had a fixed deadline, I prioritised user stories using the MoSCoW method, so I could focus my efforts on the highest-priority must-have and should-have items. 

The user stories are listed below, grouped by their related epic.

#### User stories

##### Epic: Blog

*Note: The user story numbers are taken from the [GitHub Project](https://github.com/users/John-Kingham/projects/14) where I managed the sprint backlogs and user stories.*

- #1 Trustworthy look and feel (must-have)
  - As a User, I can see a website that looks good and works well, with an understated professional design, so I’m not put off by something that looks overly flashy and gimmicky.
- #2 Read blog posts (must-have)
  - As a User, I can find and read useful information about relevant investments and investing, so I can become a better investor and discover worthwhile investments.
- #3 Read categorised posts (could-have)
  - As a User, I can see blog posts for different topic categories (e.g. market valuations, company reviews, investing strategies), so I can easily find the type of content I want to read.
- #7 Chat with other users (must-have)
  - As a User, I can converse with other users and the admin, so I can have engaging conversations with like-minded people.
- #10 Manage blog posts (must-have)
  - As an Admin, I can create, update and delete blog posts, so I can attract new Users and nurture them with regular new content.
- #11 Categorise posts (could-have)
  - As an Admin, I can categorise articles, so Users can more quickly find the type of content they’re looking for.
- #15 Manage user chat (must-have)
  - As an Admin, I can authorise, edit or delete user-generated blog comments, to block or remove inappropriate content.
- #19 Helpful error pages (must-have)
  - As a User, if there is an error loading a page then I'm shown a helpful error page in the style of the overall website, so I'm not put off by badly styled error pages.
- #20 View all posts for a category (could-have)
  - As a User, I can view all posts for a single category, so I can quickly find the type of posts I'm looking for.

##### Epic: Info pages

- #4 Read about info (should-have)
  - As a User, I can read about the people behind the website, so I can decide if they’re trustworthy.
- #5 Read portfolio info (should-have)
  - As a User, I can see the author’s investment performance, so I can decide if they know what they’re talking about.
- #6 Contact the company offline (must-have)
  - As a User, I can see the company's contact details, so I can use email, phone or social media to have a private conversation with someone at the company to ask them questions.
- #12 Manage about info (should-have)
  - As an Admin, I can create, update and delete "about" content, so Users know something about the people behind the articles they’re reading.
- #13 Manage portfolio info (should-have)
  - As an Admin, I can create, update and delete content about our investment performance, so Users can see how well our expertise has performed in practice.

##### Epic: User sign-up

- #8 Get blog posts by email (could-have)
  - As a User, I can easily subscribe to an email newsletter, so I can get the latest posts by email.
- #9 Read premium content (could-have)
  - As a User, I can easily sign up to read premium content, so I can further benefit from the author’s knowledge and experience. (could-have)
- #14 Manage user enquiries (could-have)
  - As an Admin, I can read private messages from Users, so I can answer questions they wouldn’t want to ask in public.
- #16 Manage email newsletters (could-have)
  - As an Admin, I can see the emails of all subscribed Users, so I can send them emails with the latest blog post.
- #17 Manage premium content (could-have)
  - 10. As an Admin, I can create free and premium content, and control access accordingly.
- #18 Contact the company through the website (could-have)
  - As a User, I can send a message to the company through the website, so I can ask questions directly, without having to use another app or email.

Some of the could-have stories didn't make it into the deployed website. This is normal and expected as could-haves are lower priority non-essential requirements, and they can easily be added in future sprints.

### Structure Plane

The structure plane is where we begin to design a solution to the previously gathered requirements, and my initial design for the site had the following high-level structural UI elements:

![Website structure diagram](/docs/images/wireframes/page-structure.png)

Note that some of these structural elements did not make it into the deployed website. This was due to a mixture of time constraints, user feedback and (hopefully) better designs as the project progressed and more information became available.

### Skeleton Plane

The skeleton plane adds detail to the structural elements created in the previous plane.

I used wireframes to add detail to the webpage structures outlined above. These wireframes were not intended to be used as blueprints, so there are some minor differences between them and the deployed site, due to time constraints, user feedback and better ideas as the project progressed. The structural About and Contact pages were also combined into a single About/Contact wireframe.

#### Mobile Wireframes

![Wireframes for mobile](docs/images/wireframes/wireframes-mobile.png)

#### Tablet Wireframes

![Wireframes for tablet](docs/images/wireframes/wireframes-tablet.png)

#### Desktop Wireframes

![Wireframes for desktop](docs/images/wireframes/wireframes-desktop.png)

### Surface Plane

The surface plane is where the fine details of the user interface are chosen.

#### Colour Palette

The site's colour palette was inspired by the colours used by [Hargreaves Lansdown](https://www.hl.co.uk/), a leading UK investment platform with the kind of subtle, professional look the product owner was looking for.

- #071D49 (dark blue) - The first colour
- #0A70DC (medium blue) - The second colour
- #0857AB (darker medium blue) - A "highlight" version of the second colour, primarily used for button hover effects
- #EFF7FF (very light blue) - The third colour
- #C2E0FF (darker light blue) - A "highlight" version of the third colour, primarily used for button hover effects.

#### Custom Fonts

The site uses two custom fonts from Google Fonts.

- [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab): For headings
- [Open Sans](https://fonts.google.com/specimen/Open+Sans): For non-heading text

#### Content

All model-based content (e.g. blog posts, portfolio page content, etc.) was generated using [Microsoft Co-Pilot](https://copilot.microsoft.com/).

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Installed Python Libraries

- [cloudinary](https://pypi.org/project/cloudinary/) (Python and Django SDK for Cloudinary)
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) (Bootstrap5 template pack for django-crispy-forms)
- [django](https://pypi.org/project/Django/) (A high-level Python web framework)
- [django-allauth](https://pypi.org/project/django-allauth/) (Django authentication, registration, account management, social account authentication)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) (Best way to have Django DRY forms)
- [django-summernote](https://pypi.org/project/django-summernote/) (Summernote plugin for Django)
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) (Django package that provides Cloudinary storages for media and static files as well as management commands for removing unnecessary files)
- [dj-database-url](https://pypi.org/project/dj-database-url/) (Use Database URLs in your Django Application)
- [gunicorn](https://pypi.org/project/gunicorn/) (WSGI HTTP Server for UNIX)
- [psycopg2](https://pypi.org/project/psycopg2/) (Python-PostgreSQL Database Adapter)
- [urllib3](https://pypi.org/project/urllib3/) (HTTP library with thread-safe connection pooling, file post, and more)
- [whitenoise](https://pypi.org/project/whitenoise/) (Radically simplified static file serving for WSGI applications)
- Required dependencies for the above libraries

### Other Technologies
- [PostgreSQL](https://www.postgresql.org/) (a PostgreSQL database was supplied for the project by Code Institute)

## Data Model

During the Structure Plane, I created a structural entitiy relationship diagram, showing potential database tables and their relationships:

![ERD structural diagram](/docs/images/erd/erd-structure.png)

In the Skeleton Plane, I added fields to the data model tables that were most likely to be implemented. I also simplified the data model that related to premium blog content, by removing the SubscriptionTier table and replacing it with a Premium Content field in the Post table.

![ERD detail diagram](/docs/images/erd/erd-skeleton.png)

## Features

### Implemented Features

#### Header navigation

## Project Management

### Sprint 1

Goal - To deploy the first version of the site, with Blog Post editing and a Portfolio page.

### Sprint 2

Goal - Add the Homepage and Blog Archive page.

### Sprint 3

Goal - Add user comments, premium content and an about page.

## Testing

## Deployment

## Credits