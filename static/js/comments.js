/* jshint esversion: 11 */

/**
 * When the comment edit button is clicked, initialise the comment form for
 * editing.
 */
function addEditCommentEventListeners() {
  const commentEditButtons = document.querySelectorAll(".edit-btn");
  const commentTextField = document.querySelector("#id_content");
  const commentForm = document.querySelector("#commentForm");
  const submitButton = document.querySelector("#submitButton");

  for (const commentEditButton of commentEditButtons) {
    commentEditButton.addEventListener("click", (e) => {
      // Insert the comment's text into the comment form.
      const commentId = e.target.getAttribute("data-comment-id");
      const commentText = document.querySelector(
        `#comment${commentId}`
      ).innerText;
      commentTextField.value = commentText;

      // Update the form's submit button text to "update".
      submitButton.innerText = "Update";

      // Set the focus on the form's text field.
      commentTextField.focus();

      // Send the form's submitted data to the edit comment view.
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }
}

/**
 * When the comment delete button is clicked, set up and display the delete
 * comment modal.
 */
function addDeleteCommentEventHandlers() {
  const deleteModal = new bootstrap.Modal(
    document.querySelector("#delete-modal")
  );
  const deleteButtons = document.querySelectorAll(".delete-btn");
  const confirmDeleteButton = document.querySelector("#confirm-delete");

  for (const deleteButton of deleteButtons) {
    deleteButton.addEventListener("click", (e) => {
      const commentId = e.target.getAttribute("data-comment-id");
      confirmDeleteButton.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }
}

addEditCommentEventListeners();
addDeleteCommentEventHandlers();
