const editForm=document.getElementById("edit_form")
const add_form=document.getElementById("add_form")
const edit_link=document.getElementById("edit_a")

edit_link.addEventListener('submit', event => {
  event.preventDefault();
  console.log(event);
    edit_form.classList.remove('hidden');
    add_form.classList.add('hidden');})


    