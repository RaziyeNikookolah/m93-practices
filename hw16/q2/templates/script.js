const editFormContainer = document.getElementById("edit-form-container");
const addFormContainer = document.getElementById("add-form-container");
const editLink = document.getElementById("edit-a");

editLink.addEventListener("click", (event) => {
  event.preventDefault();
  console.log(event);
  editFormContainer.classList.remove("hidden");
  addFormContainer.classList.add("hidden");
});