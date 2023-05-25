const nameInput = document.getElementById("name-input");
const lastnameInput = document.getElementById("lastname-input");
const phoneNumberInput = document.getElementById("phone-number-input");
const emailInput = document.getElementById("email-input")
const formBtn = document.getElementById("form-btn");
const personsTlbBody = document.getElementById("persons")
const personForm = document.getElementById("person-form")


let validEmail = false;
let validName = false;
let validLastname = false;
let validPhoneNumber = false;

let regName = /^[a-zA-Z]+ [a-zA-Z]+$/;

nameInput.addEventListener('change', () => {
  let regName = /^[a-zA-Z]+ [a-zA-Z]+$/;
  if (!regName.test(nameInput.value)) {
    nameInput.style.borderColor = '#ff0000';
  } else {
    validName = true;
    nameInput.style.borderColor = '#000';
  }
});
lastnameInput.addEventListener('change', () => {
  let regLastName = /^[a-zA-Z]+[a-zA-Z]+$/;
  if (!regLastName.test(lastnameInput.value)) {
    lastnameInput.style.borderColor = '#ff0000';
  } else {
    validLastname = true;
    lastnameInput.style.borderColor = '#000';
  }
});

emailInput.addEventListener('change', () => {
  let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(emailInput.value)) {
    emailInput.style.borderColor = '#ff0000';
  } else {
    validEmail = true;
    emailInput.style.borderColor = '#000';
    // email.style.borderColor = "transparent"
  }
  // console.log(emailRegex.test(email.value));
});
phoneNumberInput.addEventListener('change', () => {
  let phoneNumberRexex = /^09[0|1|2|3][0-9]{8}$/;
  if (!phoneNumberRexex.test(phoneNumberInput.value)) {
    phoneNumberInput.style.borderColor = '#ff0000';
  } else {
    validPhoneNumber = true;
    phoneNumberInput.style.borderColor = '#000';
  }
});



let id = 1

formBtn.addEventListener("click", (event) => {
  event.preventDefault();
  if (formBtn.innerHTML === "به روز رسانی") {
    // Update the row with new form element values
    const rows = personsTlbBody.getElementsByTagName("tr");
    for (let i = 0; i < rows.length; i++) {
      const editButton = rows[i].querySelector(".edit-btn");
      if (editButton && editButton.classList.contains("editing")) {
        rows[i].getElementsByTagName("td")[1].innerText = nameInput.value;
        rows[i].getElementsByTagName("td")[2].innerText = lastnameInput.value;
        rows[i].getElementsByTagName("td")[3].innerText = emailInput.value;
        rows[i].getElementsByTagName("td")[4].innerText = phoneNumberInput.value;
        editButton.classList.remove("editing");
        formBtn.innerHTML = "عضویت";
        personForm.reset();
        return;
      }
    }
  } else {
    // Add a new row with form element values
    personsTlbBody.innerHTML += `
      <tr>
        <td>${id}</td>
        <td>${nameInput.value}</td>
        <td>${lastnameInput.value}</td>
        <td>${emailInput.value}</td>
        <td>${phoneNumberInput.value}</td>
        <td>
          <a href="#/${id}" class="btn btn-success edit-btn">ویرایش</a>
        </td>
        <td>
          <a href="#/${id}" class="btn btn-danger delete-btn">حذف</a>
        </td>
      </tr>
    `;
    personForm.reset();
    id++;
  }

  const deleteButtons = document.getElementsByClassName("delete-btn");
  for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener("click", (event) => {
      event.preventDefault();
      const row = event.target.parentNode.parentNode;

      // Display an alert before deleting the row
      const confirmDelete = confirm("برای حذف مطمپنی؟");

      if (confirmDelete) {
        row.remove();
        alert("حذف شد.");
      }
    });
  }


  const editButtons = document.getElementsByClassName("edit-btn");
  for (let i = 0; i < editButtons.length; i++) {
    editButtons[i].addEventListener("click", (event) => {
      event.preventDefault();
      const row = event.target.parentNode.parentNode;
      const rowData = Array.from(row.getElementsByTagName("td")).map(td => td.innerText);
      nameInput.value = rowData[1];
      lastnameInput.value = rowData[2];
      emailInput.value = rowData[3];
      phoneNumberInput.value = rowData[4];
      formBtn.innerHTML = "به روز رسانی";

      // Add editing class to the edit button to track the row being edited
      const editButtons = personsTlbBody.getElementsByClassName("edit-btn");
      for (let j = 0; j < editButtons.length; j++) {
        editButtons[j].classList.remove("editing");
      }
      event.target.classList.add("editing");
    });
  }
});





