# Quality Shares - Automated Testing

The Django project has three apps (about, blog and portfolio), each of which has a `test_views.py` file containing unit tests.

## About App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestAboutView|test_about_page|Pass|

## Blog App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestBlogViews|test_post_list_view|Pass|
|TestBlogViews|test_post_detail_view|Pass|
|TestBlogViews|test_category_list_view|Pass|
|TestBlogViews|test_new_comment_submission|Pass|

Tests for editing and deleting comments would have been ideal, but these were not a required part of the project and were deferred due to time constraints.

## Portfolio App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestPortfolioView|test_portfolio_page|Pass|

# Quality Shares - Manual Testing

## Front-End Functionality

### Header Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Site logo|When clicked, the user is taken to the homepage|Clicked the logo|As expected|None|
|Site title|When clicked, the user is taken to the homepage|Clicked the title|As expected|None|
|Sign-up button|When the user is not logged in, a sign-up button is visible|Viewed header when logged out|As expected|![Header sign-up button](/docs/images/testing/header-buttons.png)|
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When the user is not logged in, a log-in button is visible|Viewed header when logged out|As expected|![Header log-in button](/docs/images/testing/header-buttons.png)|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Log-out button|When the user is logged in, a log-out button is visible|Viewed header when logged in|As expected|![Header log-out button](/docs/images/testing/header-logged-in.png)|
|Log-out button|When clicked, the user is taken to the log-out page|Clicked log-in button|As expected|None|

### Footer Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Social media links|When clicked, a new tab opens showing the relevant social media platform|Clicked each link|As expected|None|

### Posts by Category Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Post title link|When clicked, the user is taken to the Post Detail page for that post|Clicked several links|As expected|None|

### Post Detail - Premium Content Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Premium content panel|When the user is logged out and the post contains premium content, the user is shown a sign-up/log-in panel|Viewed a post with premium content as a logged-out user|As expected|![Premium content panel](/docs/images/testing/post-detail-premium-content-panel.png)|
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Premium content|When the user is logged in and the post contains premium content, the user is shown the premium content|Viewed a post with premium content as a logged-in user|As expected|![Premium content](/docs/images/testing/post-detail-premium-content.png)|

### Post Detail - Comments Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Sign-up or log-in request|When the user is logged out, the comments section asks the user to sign-up or log-in |Viewed the comments section of a post as a logged-out user|As expected|![Comments sign-up request](/docs/images/testing/comments-sign-up-log-in.png)
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Hide unapproved comments|When the user is logged out, unapproved comments are not visible|As a logged out user, viewed the comments section of a post with unapproved comments|As expected|![Hidden unapproved comment](/docs/images/testing/comments-hidden-unapproved.png)|
|Show approved comments|When the user is logged out, approved comments are visible|View the comments section as a logged out user|As expected|![Visible approved comments](/docs/images/testing/comments-visible-approved.png)|
|Comment form|When the user is logged in, the sign-up/log-in request is replaced with a comment form|Viewed the comments section as a logged-in user|As expected|![Comments form](/docs/images/testing/comments-form.png)|

### Post List Section

### Portfolio and About Sections

There are no links within the Portfolio and About sections, other than those embedded within admin-created content. Content formatting and functionality is dealt with in a separate section of this document.

### Sign-up, Log-in and Log-out Sections

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Logged-in message|After logging in, a relevant message is shown|Logged in|As expected|![Header log-in message](/docs/images/testing/header-logged-in.png)|

### 404 Error Page Section

### 500 Error Page Section

## Admin Site Functionality

### Managing About information

### Managing Portfolio information

### Managing Posts

### Managing Comments

