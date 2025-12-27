# Quality Shares

- [Live website](https://quality-shares-3f67cc1f7e60.herokuapp.com/)
- [Live admin login](https://quality-shares-3f67cc1f7e60.herokuapp.com/admin)

Quality Shares is an informative and educational website for "quality investors"; in other words, investors seeking high-quality income and growth stocks.

I built the site for Jim Smith, a (fictional) financial analyst with 20 years’ experience. 

Jim was seeking a challenge and wanted to start his own business, leveraging his extensive knowledge as an investor and analyst. He likes writing, so he wanted to launch a paid blog/newsletter business.

Jim already has a Substack where he publishes free weekly articles to build up his audience. He wanted to move from Substack to a bespoke website to give him (a) more control over the platform’s structure, and (b) more flexibility with potential future product offerings, such as books, courses, coaching, etc.

![Responsive on multiple screen sizes](./docs/images/features/responsive-multi-screen.png)

## Table of Contents

- [User Experience Design](#user-experience-design)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Project Management](#project-management)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience Design

I designed the site using the "five planes" UX design process.

### Strategy Plane

The strategy plane is centred around discovering the product owner’s and users’ goals.

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

The scope plane is primarily concerned with defining the project's scope, including what is in scope and what is out of scope.

#### Epics

There were several high-level requirements (or epics) that Jim wanted:

- Blog:
  - A Substack-like blog where Jim can publish content and build trust with users, and where users can find useful information to read. The blog should also allow users to interact, via comments or a chat system, to build more trust.
- Info pages:
  - Pages or sections on the site providing information about Jim, his investment strategy or portfolio, and how to contact him. These should build further trust, which Jim hopes will generate revenue in the future.
- User sign-up:
  - A way for users to sign up to get e-mail newsletters and other premium content, which Jim intends to monetise at a later stage.

I broke the above epics down into user stories to add detail to the project's scope. As the project had a fixed deadline, I prioritised user stories using the MoSCoW method, so I could focus my efforts on the highest-priority must-have and should-have items. 

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

![Website structure diagram](./docs/images/wireframes/page-structure.png)

Note that some of these structural elements did not make it into the deployed website. This was due to a mixture of time constraints, user feedback and (hopefully) better designs as the project progressed and more information became available.

### Skeleton Plane

The skeleton plane adds detail to the structural elements created in the previous plane.

I used wireframes to add detail to the webpage structures outlined above. These wireframes were not intended to be used as blueprints, so there are some minor differences between them and the deployed site, due to time constraints, user feedback and better ideas as the project progressed. The structural About and Contact pages were also combined into a single About/Contact wireframe.

#### Mobile Wireframes

<details>
<summary>Mobile Wireframes</summary>

![Wireframes for mobile](./docs/images/wireframes/wireframes-mobile.png)

</details>

#### Tablet Wireframes

<details>
<summary>Tablet Wireframes</summary>

![Wireframes for tablet](./docs/images/wireframes/wireframes-tablet.png)

</details>

#### Desktop Wireframes

<details>
<summary>Desktop Wireframes</summary>

![Wireframes for desktop](./docs/images/wireframes/wireframes-desktop.png)

</details>

### Surface Plane

The surface plane is where the fine details of the user interface are chosen.

#### Colour Palette

The site's colour palette was inspired by the colours used by [Hargreaves Lansdown](https://www.hl.co.uk/), a leading UK investment platform with the kind of subtle, professional look the product owner was looking for.

- #071D49 (dark blue) - The primary colour
- #0A70DC (medium blue) - The secondary colour
- #0857AB (darker medium blue) - A "highlight" version of the second colour, primarily used for button hover effects
- #EFF7FF (very light blue) - The tertiary colour
- #C2E0FF (darker light blue) - A "highlight" version of the tertiary colour, primarily used for hover effects

#### Custom Fonts

The site uses two custom fonts from Google Fonts.

- [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab): For headings
- [Open Sans](https://fonts.google.com/specimen/Open+Sans): For non-heading text

#### Content

All model-based content (e.g. blog posts, portfolio page content, etc.) was generated using [Microsoft Co-Pilot](https://copilot.microsoft.com/).

## Data Model

### High-Level Entity Relationship Diagram

During the Structure Plane, I created a structural entitiy relationship diagram, showing potential database tables and their relationships without the detail of individual fields:

![ERD structural diagram](./docs/images/erd/erd-structure.png)

### Detailed Entity Relationship Diagram

In the Skeleton Plane, I added detail by adding fields to the data model tables that were most likely to be implemented. I also simplified the parts of the model that related to premium blog content, by removing the SubscriptionTier table and replacing it with a Premium Content field in the Post table.

The fields use generic data types like string and date, as this diagram is still abstract and not implementation specific (i.e. not trying to represent any specific database type or ORM system).

In the diagram, the Post table has the category field as a simple string type, but at the implementation stage I changed the design to have a separate Category table, with name and description fields and a one-to-many relationship from Category to Post.

![ERD detail diagram](./docs/images/erd/erd-skeleton.png)

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Frameworks & Libraries

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Database

- [PostgreSQL](https://www.postgresql.org/) (a PostgreSQL database was supplied for the project by Code Institute)

### External Storage

- [Cloudinary](https://cloudinary.com/)

### Hosting

- [Heroku](https://www.heroku.com/)

### Installed Python Libraries

- [cloudinary](https://pypi.org/project/cloudinary/) (Python and Django SDK for Cloudinary)
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) (Bootstrap5 template pack for django-crispy-forms)
- [django](https://pypi.org/project/Django/) (A high-level Python web framework)
- [django-allauth](https://pypi.org/project/django-allauth/) (Django authentication, registration, account management, social account authentication)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) (Best way to have Django DRY forms)
- [django-summernote](https://pypi.org/project/django-summernote/) (Summernote plugin for Django)
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) (Django package that provides Cloudinary storage for media and static files as well as management commands for removing unnecessary files)
- [dj-database-url](https://pypi.org/project/dj-database-url/) (Use Database URLs in your Django Application)
- [gunicorn](https://pypi.org/project/gunicorn/) (WSGI HTTP Server for UNIX)
- [psycopg2](https://pypi.org/project/psycopg2/) (Python-PostgreSQL Database Adapter)
- [urllib3](https://pypi.org/project/urllib3/) (HTTP library with thread-safe connection pooling, file post, and more)
- [whitenoise](https://pypi.org/project/whitenoise/) (Radically simplified static file serving for WSGI applications)
- Required dependencies for the above libraries

## Features

### Implemented Features

#### Header Navigation

![Header navigation feature](./docs/images/features/header-nav.png)

- Each page contains a header navigation section.
- This section contains the site's logo and title in the primary dark blue colour. The site title has a large font size and uses the site's custom headings font.
- This section also contains sign-up and log-in buttons. The sign-up button is solid and uses the secondary blue as its background colour and white as a high-contrast text colour. The button's colour changes on hover to provide visual feedback. The log-in button has a white background and uses the secondary blue colour for text. On hover, this button's background switches to the tertiary blue colour to give the user visual feedback. Identical sign-up and log-in buttons are used across the site.
- When the user is logged in, the sign-up and log-in buttons are replaced by a log-out button, which uses the same styling as the log-in button.
- This section also contains a navigation bar, with links to the site's top-level pages (Home, Archive, Portfolio, About).
- This section displays messages to users, providing additional feedback for certain activities. These include logging in and logging out, as well as creating, deleting and updating comments.
- This section is useful to users for many reasons. It provides a consistent look-and-feel at the start of each page, it enables users to easily navigate around the site, it enables users to log in and out, and it gives helpful feedback in the form of pop-up messages.

#### Posts by Category

![Posts by category feature](./docs/images/features/posts-by-category.png)

- The homepage contains a list of blog posts grouped by category (e.g. Market Valuations, Company Reviews, Investment Strategy, etc). 
- The category name and post titles are in the primary dark blue colour and use the site's custom headings font.
- Each blog post's feature image, title and last updated date are shown within a bordered "card" with rounded corners. The border is in a generic light grey colour which is not explicitly part of the site's colour palette. This design cleanly separates one post from another, while providing a minimalist, modern look and feel. 
- Each post's title links to the post's detail page. As the title is a link, it provides visual feedback on hover by displaying an underline.
- The post's last updated date is in the site's custom body font and the darker "highlight" version of the secondary blue colour.
- The section and "card" backgrounds are plain white, to avoid distracting users from the content, which is the most important part of the site.
- This section is useful to users because it shows them the various content topics available on the site, and it helps them quickly find blog posts about a specific topic.

#### Contact Details

![Contact details feature](./docs/images/features/contact-details.png)

- The footer of each page contains the company's contact details.
- Contact details include the company's email, postal address and main social media links.
- The footer contains a header, in the site's customer header font and in the site's primary dark blue colour.
- The footer's body text uses the site's custom body font and is in standard black.
- The social media icons are in the secondary medium blue colour and use the "highlight" version of the secondary colour on hover, to provide visual feedback. Each icon links to its respective social media platform.
- This section is useful to users because it enables them to contact the company and to ask questions in various ways.

#### List of Posts (Post Archive)

![List of posts feature](./docs/images/features/post-archive.png)

- The Archive page contains a page heading and a list of all blog posts, sorted by creation date in descending order (newest to oldest).
- As with other sections, this section's headings and post titles use the site's custom heading font and the primary dark blue colour. 
- Posts are shown in a similar "card" format to the Post by Category (homepage) section, with each card containing the post's feature image, title and last updated date. The main difference is that on wide screens, cards in this section are shown in a single column with each card having a horizontal internal layout, whereas in the Posts by Category section the cards have a vertical internal layout and are stacked side-by-side, two-by-two.
- This section lacks pagination, but the site currently has relatively little content so this isn't a major issue, and pagination can easily be added in a future release.
- This section is useful to users as it allows them to quickly scan through all posts on the site, especially the most recent posts as these are listed first.

#### Blog Post Detail

![Post detail feature](./docs/images/features/post-detail.png)

- Clicking on a blog post title on either the List of Posts section or the Posts by Category section takes the user to a detail page for that post.
- This section shows the post's title, feature image, updated date, category and free content. Premium content and comments are shown on the same page, but these are separate sections and I explain them in more detail below.
- The title uses the site's primary dark blue colour and custom heading font.
- The feature image shrinks to fit within the width of the written content, and doesn't grow wider than the original image.
- The post's date and category are shown in the custom body font and in the highlighted version of the secondary blue colour.
- The post's content uses the primary colour and custom headings font for headings, and black and the custom body font for body text.
- This section is useful to users because it's where they'll find educational and informative content about quality investing. 

#### Blog Post Premium Content

![Premium content feature](./docs/images/features/premium-content.png)

- Users must sign up or log in to read premium content.
- If a post contains premium content and the user isn't logged in, they are shown a panel asking them to sign up or log in.
- This panel contains a heading, body content and sign-up and log-in buttons.
- The heading, body content and buttons use the same fonts and colours used across the rest of the site. The sign-up and log-in buttons send the user to the relevant sign-up or log-in page.
- The panel has a generic light grey background, which isn't explicitly part of the site's colour palette. The panel also has a generic darker grey border with rounded edges, and this colour also isn't an explicit part of the colour palette.
- When users log in and revisit this page, this panel is replaced with the post's premium content, which is styled identically to the post's free content.
- This section is useful to users because it allows them to see premium content which is not available to logged-out users.

#### Blog Post Comments

![Comments feature](./docs/images/features/comments.png)

- Users must sign up or log in to submit comments.
- This section contains a request for users to sign up or log in, and a list of comments. Exactly what the user sees will depend upon their logged-in/out status and the approval status of each comment.
- If the user is logged out, they will see a message asking them to sign up or log in, along with the relevant sign-up and log-in buttons. These buttons are styled in the same way as they are across the rest of the site.
- If the user is logged out, they will also see a list of approved comments. Each comment shows the authors username and the comment's creation date, in the site's custom body font and in the darker "highlight" version of the secondary blue colour.
- If the user is logged in, they won't see the section asking them to sign up or log in. And in addition to approved comments, they'll also see any unapproved comments where they are the author.
- Unapproved comments are distinguished by a generic light-grey background and a reminder (in bold red italics) that the comment is awaiting approval.
- If the user is logged in, they will see Edit and Delete buttons below each of their own comments. The Edit button is styled the same as the Sign up button, and the Delete button is styled the same as the Log in button.
- If the user clicks the Edit button, the comment's text is automatically copied into the comment form's text area, ready for updating.
- If the user clicks the Delete button, they're shown a confirmation modal, where they can confirm or cancel their deletion request.
- Images of these various features are available in the TESTING document.
- This section is useful to users as it enables them to converse directly with the site's authors and with other users.

#### Sign up

![Sign up feature](./docs/images/features/sign-up.png)

- This section enables users to sign up to view premium content and post comments. Users can reach this section by clicking on any of the site's Sign-up buttons.
- This section contains a heading (which uses the site-wide standard heading colour and font) and a sign-up form and button.
- The form has fields for username, email (optional) and password.
- There are mininum standards for the password which are enforced through validation.
- The form's sign-up button uses the site's secondary blue colour as its background, with text in white. The background switches to the darker "highlight" variant colour on hover, to provide visual feedback.
- This section is useful to users because it enables them to sign-up to view premium content and engage in conversations with admins or other users by posting comments.

#### Log in

![Log in feature](./docs/images/features/log-in.png)

- This section is where signed-up users can log-in to view premium content and post comments. Users can reach this section by clicking on any of the site's Log-in buttons.
- This section contains a heading (which uses the site-wide standard heading colour and font) and a log-in form and button.
- The form has fields for username and password.
- The form's log-in button uses the site's secondary blue colour as its background, with text in white. The background switches to the darker "highlight" variant colour on hover, to provide visual feedback.
- This section is useful to users because it enables them to log-in and view premium content and engage in conversations with admins or other users by posting comments.

#### Log out

![Log out feature](./docs/images/features/log-out.png)

- This section is where logged-in users can log out.
- This section contains a heading (which uses the site-wide standard heading colour and font), some body text and a log-out button.
- The log-out button uses the site's secondary blue colour as its background, with text in white. The background switches to the darker "highlight" variant colour on hover, to provide visual feedback.
- This section is useful to logged-in users because it enables them to log-out, which helps to keep their user profile secure.

#### Portfolio Information

![Portfolio feature](./docs/images/features/portfolio.png)

- This section contains information about Jim's model investment portfolio.
- It includes a title (using the site-wide standard heading colour and font), a feature image (and caption) and relevant written content.
- The image shrinks to fit within the width of the written content, and never grows beyond its original size.
- The section's content uses the site's standard custom body font for body text and custom heading font and primary dark blue colour for headings.
- This section is useful to users as they can read about Jim's portfolio to see if they like his approach to investing and his past performance.

#### About Information

![About feature](./docs/images/features/about.png)

- This section contains information about Jim.
- It includes a title (using the site-wide standard heading colour and font), a feature image (and caption) and relevant written content.
- The image shrinks to fit within the width of the written content, and never grows beyond its original size.
- The section's content uses the site's standard custom body font for body text and custom heading font and primary dark blue colour for headings.
- This section is useful to users as they can learn more about the person (or people) behind the site, which may help them develop an opinion about whether the site's content is worth reading or not (and perhaps whether future products are worth purchasing).

#### Error Pages
|Error code|Feature|
|---|---|
|404|![404 error notice](./docs/images/features/error-404.png)|
|500|![500 error notice](./docs/images/features/error-500.png)|

- The 404 error section is shown if the user enters an invalid URL, while the 500 error section is shown if there is an internal server error.
- These sections contain a simple error message and a button to return to the homepage.
- These sections are useful to users because they tell users when they've visited an invalid URL, and give users an easy way to get back to the homepage, while retaining the same style as the rest of the site.

### Future Features

Some of the could-have user stories didn't make it into the deployed site before the project's deadline. This is normal with timeboxed agile projects. These stories remain in the GitHub project's product backlog milestone, and may be implemented in future iterations depending on what Jim decides to do.

#### Manage Email Newsletters / Get Posts by Email

This is user story #8 and #16, part of the User Sign-up epic. The idea was that users could subscribe to a free email newsletter and receive the latest posts by email. This would likely require connecting the site to an external bulk email platform, which could make this a relatively large feature, but still technically feasible.

#### Contact the Company through the Website / Manage User Enquiries

This is user story #14 and #18. This is effectively a contact form that users can use to send private messages to the site's admin, who can then respond by email, as appropriate. This is technically simple and could easily be implemented in a future release.

#### View all Posts for a Single Category

This is user story #20. The plan was for users to be able to view all posts for one category by clicking on the category of a single post, or via links on the homepage or a category dropdown selector on the Post Archive page. This should be technically simple and could easily be implemented in a future release.

#### Separate Development and Production Databases

This isn't recorded as a user story, but the site currently uses the same database in its development and production environments. Best practice is to use separate databases, and this would be a high-priority feature for a future release.

## Project Management

I managed the project using a somewhat simplified combination of [AgilePM](https://www.agilebusiness.org/agileprojectmanager.html) (previously known as DSDM) and [Scrum](https://www.scrum.org/).

AgilePM has several phases that occur before the iterative development phase.

### Pre-Project Phase

In this phase, Jim (the fictional product owner) asked me to build him a website, so we met for a high level discussion to assess the project's feasibility.

### Feasibility Phase

In this phase, we discussed the high-level scope of the project (mostly in terms of epics) and its potential cost, and how that compared to Jim's overall budget. This information fed into the Strategy and Scope Planes. The project was technically and economically feasible, so we continued to the next phase.

### Foundations Phase

In this phase, we broke epics down into user stories. Almost all of the project's user stories were written by the end of this stage, so I had a good understanding of the project's scope before launching the Scrum development phase. This phase mostly aligns with the Scope Plane, but it also includes work on both the Structure and Skeleton Planes.

### Scrum Development Phase

In this phase, I turned the requirements and structural/skeletal designs (e.g. wireframes) into working software across three sprints.

For each sprint, my goal was to allocate up to 60% of the sprint backlog to must-have items, and up to 20% each to should-have and could-have items. In practice, with such a small project with so few user stories, this was impossible, but that was still the goal.

You can find more detail about each user story, including acceptance criteria and how I broke the stories down into individual tasks, in the related [GitHub Project](https://github.com/users/John-Kingham/projects/14/views/1).

### Sprint 1

![Sprint 1 backlog](./docs/images/github-project/github-project-sprint-1.png)

#### Sprint 1 Goal

To deploy the first version of the site, with Blog Post editing and a Portfolio page.

#### Sprint 1 User Stories

- #1 Trustworthy look and feel (must-have)
- #5 Read portfolio info (should-have)
- #6 Contact the company offline (must-have)
- #10 Manage blog posts (must-have)
- #13 Manage portfolio info (should-have)

### Sprint 2

![Sprint 2 backlog](./docs/images/github-project/github-project-sprint-2.png)

#### Sprint 2 Goal

Add the Homepage and Blog Archive page.

#### Sprint 2 User Stories

- #2 Read blog posts (must-have)
- #3 Read categorised posts (could-have)
- #11 Categorise posts (could-have)
- #15 Manage user chat (must-have)

### Sprint 3

![Sprint 3 backlog](./docs/images/github-project/github-project-sprint-3.png)

#### Sprint 3 Goal

Add user comments, premium content and an about page.

#### Sprint 3 User Stories

- #4 Read about info (should-have)
- #7 Chat with other users (must-have)
- #9 Read premium content (could-have)
- #12 Manage about info (should-have)
- #17 Manage premium content (could-have)
- #19 Helpful error pages (must-have)

### Product Backlog

By the project deadline, there were several could-have user stories still in the product backlog. This is a normal and expected part of agile software development.

##### Unfinished User Stories in the Product Backlog

- #8 Get posts by email (could-have)
- #14 Manage user enquiries (could-have)
- #16 Manage email newsletters (could-have)
- #18 Contact the company through the website (could-have)
- #20 View all posts for a single category (could-have)

## Testing

The website was thoroughly tested, with all tests documented in [TESTING.md](./docs/TESTING.md).

## Deployment

This repository can be cloned to make a copy on your local machine or forked to make a copy on your GitHub account.

### Cloning

You can clone the repository using these steps:

1. Go to the [GitHub repository](https://github.com/John-Kingham/quality_shares).
2. Click on the green Code button near the top.
3. Select whether to clone using HTTPS, SSH, or GitHub CLI, and copy the URL to your clipboard.
4. On your local machine, open your terminal (or Git Bash, depending on your operating system).
5. Change the current working directory to the location where you want the cloned directory.
6. In your terminal, type the following command to clone the repository:
	- `git clone https://github.com/John-Kingham/quality_shares`
7. Press Enter to create your local clone.

### Forking

By forking the GitHub repository, you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository. You can fork this repository using the following steps:

1. Log in to GitHub and go to the [GitHub repository](https://github.com/John-Kingham/quality_shares).
2. Find the Fork button at the top of the page and click it.
3. You should now have a copy of the repository in your own GitHub account.

### Database

The site uses a PostgreSQL database to store blog posts, comments and other content. The deployment instructions below assume you have a PostgreSQL database to connect to.

Creating a PostgreSQL database is beyond the scope of this document. Please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/) for more information on creating and managing a PostgreSQL database.

### Image Hosting

The site uses [Cloudinary](https://cloudinary.com/) to store images for blog posts and other content in the cloud. The deployment instructions below assume you have a Cloudinary account where you can store images.

### Site Hosting

The site has been deployed to the Internet using [Heroku](https://www.heroku.com/). The deployment instructions below assume you have a suitable Heroku account.

### Local Deployment

To run the site locally, you will need to install the required libraries and set up access to your database using the steps below:

1. Clone the remote repository to your local machine using the instructions above.
1. Start a Python virtual environment of your choice (to avoid loading required libraries into your global environment).
1. Run `pip install -r requirements.txt` to install required libraries.
1. Create a file in the root directory called `env.py` (this is in `.gitignore`, so it wasn't part of the cloned repository).
1. In `env.py`, set the following environment variable defaults:
    - DEBUG (set it to True; this forces the development environment to run in debug mode by default)
    - SECRET_KEY (set it to be a suitably secure secret key)
    - DATABASE_URL (your database's URL)
    - CLOUDINARY_URL (Go to [Cloudinary API Keys](https://console.cloudinary.com/app/c-f3af02b8364ecf9852b2cd2c73bedb/settings/api-keys) and create the  environment variable value in this format: 
      - `cloudinary://<your_api_key>:<your_api_secret>@xyz`
1. The site is now connected to your database, so run `python manage.py migrate` to create both built-in and site-specific database tables.
1. Run `python manage.py createsuperuser` to create an admin account. Admins can log into the site using the `/admin/` path.
1. Run `python manage.py collectstatic`. This copies static files into a directory called `staticfiles` which enables static files to be loaded correctly when running the site locally.
1. Run `python manage.py runserver` to launch the site locally using Django's built-in server.
1. Click the link in the terminal where it says `Starting development server at <your-local-url>` and the site should launch correctly.

### Deployment to Heroku

If you have a working PostgreSQL database and Cloudinary account, the site can be deployed to the Internet using Heroku by following these steps:

1. Fork or clone this repository using the instructions above.
1. If you cloned this repository, push your clone up to a remote repo on your GitHub account.
1. In your Heroku account, create a new app.
1. Add these config variables:
    - Key=SECRET_KEY, Value=(a secure secret key, different to the one in `env.py`)
    - Key=DATABASE_URL, Value=(your database's URL)
    - Key=CLOUDINARY_URL, Value=(your secret Cloudinary URL, created using the steps in the Local Deployment section above)
1. Add a buildpack for Python.
1. Connect the Heroku app to your GitHub repository.
1. Deploy the main branch in Heroku.
1. Wait for the site to deploy and then check that it has deployed correctly.

These steps require knowledge of Heroku that is beyond the scope of this document. If you need additional information to set up your Heroku deployment, read the official [Heroku documentation](https://devcenter.heroku.com/).

## Credits

### Project Management

- I managed the overall project using a simplified combination of [AgilePM](https://www.agilebusiness.org/) and [Scrum](https://www.scrum.org/).
- I organised the design phase using the 5-Planes/Phases method, as detailed in [The Elements of User Experience](https://uk.bookshop.org/p/books/elements-of-user-experience-the-user-centered-design-for-the-web-and-beyond-jesse-james-garrett/e232e0c9869653bd?ean=9780321683687&next=t&next=t).
- I managed the construction phase using [Scrum](https://www.scrum.org/).

### Strategy Plane

- I used [Google Docs](https://docs.google.com/) to record business and user goals.

### Scope Plane

- I used [Google Docs](https://docs.google.com/) to record epics and [GitHub Projects](https://github.com/users/John-Kingham/projects/14) to record user stories and tasks.

### Structure Plane

- I used [Mermaid Chart](https://www.mermaidchart.com/) to create high-level structure diagrams for database tables and the user interface.

### Skeleton Plane

- I used [Mermaid Chart](https://www.mermaidchart.com/) to create detailed entity relationship diagrams for the database.
- I used [Balsamiq](https://balsamiq.com/) to create wireframes for the user interface.
- I used a [Substack](https://substack.com/) called [The Wary One](https://www.thewaryone.com/) as inspiration for the general layout of each page (as reflected in the wireframes).

### Surface Plane

#### Colour Palette

- I used the colour palette of [Hargreaves Lansdown](https://www.hl.co.uk/) as inspiration for the Quality Shares colour palette.
- I used the default [Bootstrap](https://getbootstrap.com/) colours for some elements, including light-grey backgrounds and Django message colours.

#### Images

- I used the following free images from [UnSplash](https://unsplash.com/):
  - [About image](https://unsplash.com/photos/mens-blue-and-white-button-up-collared-top-DItYlc26zVI)
  - [Placeholder image](https://unsplash.com/photos/a-bank-sign-in-front-of-a-building-Wf1opKy4iaI)
  - [SP500 image](https://unsplash.com/photos/a-close-up-of-a-clock-with-different-colored-numbers-lmV3gJSAgbo)
  - [Stock price image](https://unsplash.com/photos/a-person-holding-a-cell-phone-in-front-of-a-stock-chart-K5mPtONmpHM)
  - [Investor laptop image](https://unsplash.com/photos/turned-on-macbook-pro-DfjJMVhwH_8)
  - [Investor laptop image 2](https://unsplash.com/photos/black-and-silver-laptop-computer-mcAUHlGirVs)
  - [Investor mobile image](https://unsplash.com/photos/a-remote-control-sitting-on-top-of-a-table-ip7GFn5JqX8)
  - [Candlestick chart image](https://unsplash.com/photos/black-flat-screen-computer-monitor-N__BnvQ_w18)
  - [Candlestick chart image 2](https://unsplash.com/photos/red-and-blue-light-streaks-fiXLQXAhCfk)

#### Favicons

- I used [Gauger.io](https://gauger.io/fonticon/) to create a favicon image using its "atom" icon.
- I used [Favicon.io](https://favicon.io/) to convert the favicon into multiple favicon formats.

#### Fonts

- I used custom fonts from [Google Fonts](https://fonts.google.com/). The exact fonts are listed at the top of this document.

#### Content

- I used [Microsoft Co-Pilot](https://copilot.microsoft.com/) to generate most of the site's text content.

### Scrum Development Phase

- I used [Visual Studio Code](https://code.visualstudio.com/) as the development environment.
- I mostly used [Ecosia Search](https://www.ecosia.org/), [W3Schools](https://www.w3schools.com/), [Code Institute](https://codeinstitute.net/), [MDN](https://developer.mozilla.org/) and [Microsoft Copilot](https://copilot.microsoft.com/) for general research.
- I read parts of [The Epic Guide to Agile](https://www.davetodarobooks.com/) for additional information about Scrum.
- Although I used various information sources to support the development of this project, no non-trivial code was copy/pasted into the project.

### Documentation

- I used [Code Institute's README.md template](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md) as the starting point for this document.
- I used [Am I Responsive](https://ui.dev/amiresponsive) to generate the multi-screen image shown at the start of the README.
- I used [Green Shot](https://getgreenshot.org/) to add text and arrows to some screenshots.
- I used [Grammarly]() to check spelling and grammar in README.md and TESTING.md.

## People

- I would like to thank my Code Institute mentor, [Simen Daehlin](https://github.com/Eventyret).