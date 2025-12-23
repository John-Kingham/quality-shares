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
|Show approved comments|When the user is logged out, approved comments are visible|As a logged out user, viewed the comments section of a post with approved comments|As expected|![Visible approved comments](/docs/images/testing/comments-visible-approved.png)|
|Comment form|When the user is logged in, the sign-up/log-in request is replaced with a comment form|Viewed the comments section as a logged-in user|As expected|![Comments form](/docs/images/testing/comments-form.png)|
|Create comment|When the user submits the comment form, an unapproved comment is created and shown below the form|Submitted the comment form with a new comment|As expected|*Before submitting* ![New comment - before](/docs/images/testing/comments-create-before.png) *After submitting* ![New comment - after](/docs/images/testing/comments-create-after.png)|
|Create comment message|When the user submits the comment form, an "awaiting approval" message is shown|Submitted the comment form|As expected|![Awaiting approval message](/docs/images/testing/comments-create-message.png)|
|Unapproved comments|When the user is logged in, they can see their unapproved comments with Edit and Delete buttons|Viewed unapproved comments as the logged-in comment author|As expected|![Visible unapproved comment](/docs/images/testing/comments-visible-unapproved.png)|
|Editable comments|When the user is logged in, all of their comments have Edit and Delete buttons|Viewed comments as the logged-in comment author|As expected|![Editable comment](/docs/images/testing/comments-editable.png)|
|Edit comment|When the edit button is clicked, the comment text is copied into the comment form and the comment form's button text changes to "Update"|Clicked the edit button for an unapproved comment|As expected|![Edit comment](/docs/images/testing/comments-edit-unapproved.png)|
|Update approved comment|When the comment form is submitted to update an approved comment, the comment text is updated and its status is set to unapproved|Updated an approved comment via the comment form|As expected|![Edited comment](/docs/images/testing/comments-edited-comment.png)|
|Edit comment message|When a comment is edited, an "awaiting approval" message is shown|Edited a comment|As expected|![Edited comment message](/docs/images/testing/comments-edited-comment-message.png)|
|Delete comment|When the delete button is clicked, a confirmation modal is shown|Clicked the delete button|As expected|![Delete comment modal](/docs/images/testing/comments-delete-modal.png)|
|Delete comment|When the Confirm Delete button is clicked, the comment is deleted|Clicked the Confirm Delete button|As expected|![Comment deleted](/docs/images/testing/comments-deleted-comment-gone.png)|
|Deleted comment message|When the Confirm Delete button is clicked, a "comment deleted" message is shown|Clicked the Confirm Delete button|As expected|![Deleted comment message](/docs/images/testing/comments-deleted-comment-message.png)|

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

