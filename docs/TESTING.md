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
|Sign-up button|When the user is not logged in, a sign-up button is visible|Viewed header when logged out|As expected|![Header sign-up button](./images/testing/header-buttons.png)|
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When the user is not logged in, a log-in button is visible|Viewed header when logged out|As expected|![Header log-in button](./images/testing/header-buttons.png)|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Log-out button|When the user is logged in, a log-out button is visible|Viewed header when logged in|As expected|![Header log-out button](./images/testing/header-logged-in.png)|
|Log-out button|When clicked, the user is taken to the log-out page|Clicked log-in button|As expected|None|

### Footer Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Social media links|When clicked, a new tab opens showing the relevant social media platform|Clicked each link|As expected|None|

### Posts by Category Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Post title link|When clicked, the user is taken to the Post Detail page for that post|Clicked several links|As expected|None|

### Post Detail - Content Section

The Post Detail main content section has no interactive functionality to test.

### Post Detail - Premium Content Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Premium content panel|When the user is logged out and the post contains premium content, the user is shown a sign-up/log-in panel|Viewed a post with premium content as a logged-out user|As expected|![Premium content panel](./images/testing/post-detail-premium-content-panel.png)|
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Premium content|When the user is logged in and the post contains premium content, the user is shown the premium content|Viewed a post with premium content as a logged-in user|As expected|![Premium content](./images/testing/post-detail-premium-content.png)|

### Post Detail - Comments Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Sign-up or log-in request|When the user is logged out, the comments section asks the user to sign-up or log-in |Viewed the comments section of a post as a logged-out user|As expected|![Comments sign-up request](./images/testing/comments-sign-up-log-in.png)|
|Sign-up button|When clicked, the user is taken to the sign-up page|Clicked sign-up button|As expected|None|
|Log-in button|When clicked, the user is taken to the log-in page|Clicked log-in button|As expected|None|
|Hide unapproved comments|When the user is logged out, unapproved comments are not visible|As a logged out user, viewed the comments section of a post with unapproved comments|As expected|![Hidden unapproved comment](./images/testing/comments-hidden-unapproved.png)|
|Show approved comments|When the user is logged out, approved comments are visible|As a logged out user, viewed the comments section of a post with approved comments|As expected|![Visible approved comments](./images/testing/comments-visible-approved.png)|
|Comment form|When the user is logged in, the sign-up/log-in request is replaced with a comment form|Viewed the comments section as a logged-in user|As expected|![Comments form](./images/testing/comments-form.png)|
|Empty comment validation|If the user submits an empty comment form, a validation message is shown and the form does not submit|Tried to submit an empty comment form|As expected|![Empty comment form validation](./images/testing/comments-empty-form-validation.png)|
|Create comment|When the user submits the comment form with content, an unapproved comment is created and shown below the form|Submitted the comment form with a new comment|As expected|*Before submitting* ![New comment - before](./images/testing/comments-create-before.png) *After submitting* ![New comment - after](./images/testing/comments-create-after.png)|
|Create comment message|When the user submits the comment form, an "awaiting approval" message is shown|Submitted the comment form|As expected|![Awaiting approval message](./images/testing/comments-create-message.png)|
|Unapproved comments|When the user is logged in, they can see their unapproved comments with Edit and Delete buttons|Viewed unapproved comments as the logged-in comment author|As expected|![Visible unapproved comment](./images/testing/comments-visible-unapproved.png)|
|Editable comments|When the user is logged in, all of their comments have Edit and Delete buttons|Viewed comments as the logged-in comment author|As expected|![Editable comment](./images/testing/comments-editable.png)|
|Edit comment|When the edit button is clicked, the comment text is copied into the comment form and the comment form's button text changes to "Update"|Clicked the edit button for an unapproved comment|As expected|![Edit comment](./images/testing/comments-edit-unapproved.png)|
|Update approved comment|When the comment form is submitted to update an approved comment, the comment text is updated and its status is set to unapproved|Updated an approved comment via the comment form|As expected|![Edited comment](./images/testing/comments-edited-comment.png)|
|Edit comment message|When a comment is edited, an "awaiting approval" message is shown|Edited a comment|As expected|![Edited comment message](./images/testing/comments-edited-comment-message.png)|
|Delete comment|When the delete button is clicked, a confirmation modal is shown|Clicked the delete button|As expected|![Delete comment modal](./images/testing/comments-delete-modal.png)|
|Delete comment|When the Confirm Delete button is clicked, the comment is deleted|Clicked the Confirm Delete button|As expected|![Comment deleted](./images/testing/comments-deleted-comment-gone.png)|
|Deleted comment message|When the Confirm Delete button is clicked, a "comment deleted" message is shown|Clicked the Confirm Delete button|As expected|![Deleted comment message](./images/testing/comments-deleted-comment-message.png)|

### Post List Section

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Post title link|When clicked, the user is taken to the Post Detail page for that post|Clicked several links|As expected|None|

### Portfolio and About Sections

The Portfolio and About sections have no interactive functionality to test.

### Sign-up, Log-in and Log-out Sections

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Sign-up validation|When the sign-up form is submitted with missing required fields, validation messages are shown and the form is not submitted|Tried submitting the sign-up form with various required fields missing|As expected|![Sign-up validation](./images/testing/sign-up-validation.png)|
|Sign-up message|After submitting the sign-up form, a new user profile is created, the user is logged in and a confirmation message is shown|Signed up as a new user|As expected|![Sign up message](./images/testing/sign-up-message.png)|
|Log-in validation|When the log-in form is submitted with missing required fields, validation messages are shown and the form is not submitted|Tried submitting the log-in form with various required fields missing|As expected|![Log-in validation](./images/testing/log-in-validation.png)|
|Logged-in message|After submitting the log-in form, the user is logged in and a confirmation message is shown|Logged in|As expected|![Log-in message](./images/testing/log-in-message.png)|
|Log-out|When a logged-in user clicks the log-out button, the user is logged out and a confirmation message is shown|Clicked the log-out button as a logged-in user|As expected|![Log-out message](./images/testing/log-out-message.png)|

### 404 and 500 Error Sections

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|404 error page|When an invalid path is entered, a helpful error page is shown|Entered an invalid path|As expected|![404 error page](./images/testing/404-error-page.png)|
|404 homepage button|When the "homepage" button is clicked, the user is sent to the homepage|Clicked the "homepage" button|As expected|None|
|500 error page|When an internal server error occurs, a helpful error page is shown|Simulated an internal server error (in the development environment, as this is not appropriate for production)|As expected|![500 error page](./images/testing/500-error-page.png)|
|500 homepage button|When the "homepage" button is clicked, the user is sent to the homepage|Clicked the "homepage" button|As expected|None|

## Admin Site Functionality

The admin site is a built-in part of Django, so I didn't test it as thoroughly as the parts I coded. However, I did run some basic tests to ensure the required functionality was there.

### About Admin

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|About fields|The About admin area has the correct fields|Checked the About fields|As expected|![About admin](./images/testing/about-admin.png)|
|About image|Local images can be uploaded, stored in Cloudinary and accessed from the front-end|Uploaded a local image, saved the About record and checked the About page|As expected|See above image|
|About front-end|The About content and image are visible and correctly formatted on the front-end|Viewed the About page|As expected|![About front-end](./images/testing/about-front-end.png)|

### Portfolio Admin

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Portfolio fields|The Portfolio admin area has the correct fields|Checked the Portfolio fields|As expected|![Portfolio admin](./images/testing/portfolio-admin.png)|
|Portfolio image|Local images can be uploaded, stored in Cloudinary and accessed from the front-end|Uploaded a local image, saved the Portfolio record and checked the Portfolio page|As expected|See above image|
|Portfolio front-end|The Portfolio content and image are visible and correctly formatted on the front-end|Viewed the Portfolio page|As expected|![Portfolio front-end](./images/testing/portfolio-front-end.png)|

### Post Admin

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Post fields|The Post admin area has the correct fields|Checked the Post fields|As expected|![Post admin](./images/testing/post-admin.png)|
|Post image|Local images can be uploaded, stored in Cloudinary and accessed from the front-end|Uploaded a local image, saved the Post record and checked the Post Detail page|As expected|See above image|
|Post front-end|Post content and image are visible and correctly formatted on the front-end|Viewed the Post Detail page|As expected|![Post front-end](./images/testing/post-front-end.png)|

### Comment Admin

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Comment fields|The comment admin area has the correct fields|Checked the comment fields|As expected|![Comment admin](./images/testing/comment-admin.png)|
|Comment editing|Comments can be CRUDed on the back-end|CRUDed a comment on the back-end|As expected|![Comment CRUD](./images/testing/comment-admin-crud.png)|

### Category Admin

|Feature|Expect|Action|Result|Image|
|---|---|---|---|---|
|Category fields|The Category admin area has the correct fields|Checked the Category fields|As expected|![Category fields](./images/testing/category-admin.png)|
|Category editing|Categories can be CRUDed on the back-end|CRUDed a category on the back-end|As expected|![Category CRUD](./images/testing/category-admin-crud.png)|
|Category front-end|Changes to categories are visible on the front end|Updated a category and checked the front-end|As expected|![Category front-end](./images/testing/category-front-end.png)|

## Colour Contrast

I tested colour contrasts using [colourcontrast.cc](https://colourcontrast.cc/) as the [WebAIM](https://webaim.org/) site was down.

### White + Primary

This combination is used across the site for headings and passes all tests.

![White/primary contrast](./images/testing/contrast/white-primary-blue.png)

### White + Secondary

This combination is mostly used for buttons and passes all tests at the minimum AA standard.

![White/secondary contrast](./images/testing/contrast/white-secondary-blue.png)

### Tertiary + Primary

This combination is used for the header navigation bar, footer text, outline buttons in the hover state and other areas where a light background colour is used. It passes all tests.

![Tertiary/primary contrast](./images/testing/contrast/tertiary-primary.png)

### Tertiary Highlight + Primary

This combination is used in the header navigation bar on hover and it passes all tests.

![Tertiary-highlight/primary contrast](./images/testing/contrast/tertiary-highlight-primary.png)

### Bootstrap Light + Secondary

This combination is used in the premium content info panel and for unapproved comments. It passes all tests at the minimum AA standard.

![BS Light/Secondary](./images/testing/contrast/bs-light-secondary.png)

### Bootstrap Light + Bootstrap Body Color

This combination is used for unapproved comments and it passes all tests.

![BS Light/BS Body](./images/testing/contrast/bs-light-bs-body-color.png)

### Bootstrap Light + Bootstrap Danger

This combination is used for unapproved comments. It only passes the AA Large test, but as this combination is only used with bold test, this is acceptable.

![BS Light/BS Danger](./images/testing/contrast/bs-light-bs-danger.png)

## Responsiveness

|Section|Mobile Responsive?|Tablet Responsive?|Desktop Responsive?|
|---|---|---|---|
|Header Nav|Yes|Yes|Yes|
|Footer Contact Details|Yes|Yes|Yes|
|Posts by Category|Yes|Yes|Yes|
|Posts Archive|Yes|Yes|Yes|
|Post Detail|Yes|Yes|Yes|
|Premium Content|Yes|Yes|Yes|
|Comments|Yes|Yes|Yes|
|Portfolio|Yes|Yes|Yes|
|About|Yes|Yes|Yes|

### Responsiveness Screenshots

<details>
<summary>Home - Mobile</summary>

![Home - Mobile](./images/testing/responsiveness/home-mobile.png)

</details>

<details>
<summary>Home - Tablet</summary>

![Home - tablet](./images/testing/responsiveness/home-tablet.png)

</details>

<details>
<summary>Home - Desktop</summary>

![Home - Desktop](./images/testing/responsiveness/home-desktop.png)

</details>

<br>

<details>
<summary>Post Detail - Mobile</summary>

![Post Detail - Mobile](./images/testing/responsiveness/post-detail-mobile.png)

</details>

<details>
<summary>Post Detail - Tablet</summary>

![Post Detail - tablet](./images/testing/responsiveness/post-detail-tablet.png)

</details>

<details>
<summary>Post Detail - Desktop</summary>

![Post Detail - Desktop](./images/testing/responsiveness/post-detail-desktop.png)

</details>

<br>

<details>
<summary>Archive - Mobile</summary>

![Archive - Mobile](./images/testing/responsiveness/archive-mobile.png)

</details>

<details>
<summary>Archive - Tablet</summary>

![Archive - tablet](./images/testing/responsiveness/archive-tablet.png)

</details>

<details>
<summary>Archive - Desktop</summary>

![Archive - Desktop](./images/testing/responsiveness/archive-desktop.png)

</details>

<br>

<details>
<summary>Portfolio - Mobile</summary>

![Portfolio - Mobile](./images/testing/responsiveness/portfolio-mobile.png)

</details>

<details>
<summary>Portfolio - Tablet</summary>

![Portfolio - tablet](./images/testing/responsiveness/portfolio-tablet.png)

</details>

<details>
<summary>Portfolio - Desktop</summary>

![Portfolio - Desktop](./images/testing/responsiveness/portfolio-desktop.png)

</details>

<br>

<details>
<summary>About - Mobile</summary>

![About - Mobile](./images/testing/responsiveness/about-mobile.png)

</details>

<details>
<summary>About - Tablet</summary>

![About - tablet](./images/testing/responsiveness/about-tablet.png)

</details>

<details>
<summary>About - Desktop</summary>

![About - Desktop](./images/testing/responsiveness/about-desktop.png)

</details>

## Browsers

The site's functionality and responsiveness were tested on Chrome, Edge and Firefox, as these are some of the most popular browsers.

|Test|Chrome|Edge|Firefox|
|---|---|---|---|
|Home as expected?|Yes|Yes|Yes|
|Post Detail as expected?|Yes|Yes|Yes|
|Archive as expected?|Yes|Yes|Yes|
|Portfolio as expected?|Yes|Yes|Yes|
|About as expected?|Yes|Yes|Yes|

### Browser Screenshots

All of the screenshots in the sections above were taken on Chrome. Rather than include every screenshot for every browser, here are a few screenshots from Edge and Firefox showing similar results to Chrome:

<details>
<summary>Home - Desktop - Firefox</summary>

![Homepage screenshot, desktop width, on Firefox](./images/testing/browsers/home-desktop-firefox.png)
</details>

<details>
<summary>Archive - Tablet - Firefox</summary>

![Archive page screenshop, tablet width, on Firefox](./images/testing/browsers/archive-tablet-firefox.png)
</details>

<details>
<summary>Post Detail - Mobile - Edge</summary>

![Post Detail page, mobile width, on Edge](./images/testing/browsers/post-detail-mobile-edge.png)
</details>

## Code Validation

### HTML Validation

HTML was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

#### Home HTML Validation

![Homepage HTML validation results](./images/testing/validation/home-html-validation.png)

There were four errors relating to unnecessary ARIA roles. I fixed these warnings by removing the offending roles.

There was one error relating to an unnecessary closing `li` tag. I fixed this error by removing the offending tag.

I revalidated the page and there were no errors or warnings.

![Homepage HTML validation fixed results](./images/testing/validation/home-html-validation-fixed.png)

#### Post Detail HTML Validation

![Post Detail HTML validation errors](./images/testing/validation/post-detail-html-validation-errors.png)

There was one warning about a section without a heading. To fix this, I changed the section to a div.

There was one warning about an article without a heading. This was a comment. To fix this, I changed the comment meta-info into a heading.

There was one error about the use of aria-labelledby on a plain div. I fixed this by giving the div a role of `dialog`.

I revalidated the page and there were no errors or warnings.

![Post Detail HTML validation fixed](./images/testing/validation/post-detail-html-validation-fixed.png)

#### Archive HTML Validation

![Archive HTML validation errors](./images/testing/validation/archive-html-validation-errors.png)

There were two errors relating to an unclosed section element. The closing element was outside the `{% endblock content %}` statement, so I moved it inside.

I revalidated the page and there were no errors or warnings.

![Archive HTML validation fixed](./images/testing/validation/archive-html-validation-fixed.png)

#### Portfolio HTML Validation

![Portfolio HTML validation errors](./images/testing/validation/portfolio-html-validation-errors.png)

There was one warning about a missing section heading. I fixed this by changing the section to a div. I thought the about page would have the same defect, which it did, so I applied the same fix to the about page.

I revalidated the page and there were no errors or warnings.

![Portfolio HTML validation fixed](./images/testing/validation/portfolio-html-validation-fixed.png)

#### About HTML Validation

![About HTML validation success](./images/testing/validation/about-html-validation.png)

There were no errors or warnings.

### CSS Validation

CSS validation was carried out using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

#### style.css Validation

![CSS validation errors](./images/testing/validation/css-validation-errors.png)

There was one error relating to an empty `var()` function. To fix this, I removed the empty call and its CSS selector. 

There were also three warnings about CSS variables not being statically checked. These warnings are unavoidable and do not need to be fixed.

I revalidated the CSS and there were no errors.

![CSS validation success](./images/testing/validation/css-validation-fixed.png)

### JavaScript Validation

JavaScript validation was carried out using [JSHint](https://jshint.com/).

#### comments.js

![JS validation messages](./images/testing/validation/js-validation.png)

There was one warning about `bootstrap` being an undefined variable. This is expected and is okay as the bootstrap JS is loaded by the HTML file before this custom JS file.

### Python Validation

Python code was validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/).

#### about/admin.py

![About admin.py validation](./images/testing/validation/about-admin-py-validation.png)

#### about/models.py

![About models.py validation](./images/testing/validation/about-models-py-validation.png)

#### about/test_views.py

![About test_views.py validation](./images/testing/validation/about-test-views-py-validation.png)

#### about/urls.py

![About urls.py validation](./images/testing/validation/about-urls-py-validation.png)

#### about/views.py

![About views.py validation](./images/testing/validation/about-views-py-validation.png)

#### portfolio ...



## Lighthouse

## Unfixed Bugs