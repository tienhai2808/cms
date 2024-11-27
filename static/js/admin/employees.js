const formActionMulti = document.querySelector('[form-action-multi]')
if (formActionMulti) {
  const checkAll = document.querySelector("[checkbox-all]");
  const checkBox = document.querySelectorAll("[checkbox]");
  checkAll.addEventListener("click", () => {
    if (checkAll.checked) {
      checkBox.forEach((check) => {
        check.checked = true;
      });
    } else {
      checkBox.forEach((check) => {
        check.checked = false;
      });
    }
  });

  checkBox.forEach((check) => {
    check.addEventListener("click", () => {
      const countChecked = document.querySelectorAll("[checkbox]:checked").length;
      if (countChecked == checkBox.length) {
        checkAll.checked = true;
      } else {
        checkAll.checked = false;
      }
    });
  });


  const selectInput = formActionMulti.querySelector('[select-action]')
  const selectRole = formActionMulti.querySelector('[select-role]')
  const selectTopic = formActionMulti.querySelector('[select-topic]')
  selectInput.addEventListener('change', () => {
    const valueSelect = selectInput.value
    if (valueSelect === 'role') {
      selectRole.classList.remove('d-none')
    } else {
      if (!selectRole.classList.contains('d-none')) {
        selectRole.classList.add('d-none')
        selectTopic.classList.add('d-none')
      }
    }
  })

  selectRole.addEventListener('change', () => {
    const valueRole = selectRole.querySelector('select').value;
    if (valueRole === 'Editor') {
      selectTopic.classList.remove('d-none'); 
    } else {
      selectTopic.classList.add('d-none'); 
    }
  });


  const buttonConfirm = formActionMulti.querySelector('[btn-confirm]');
  buttonConfirm.addEventListener('click', () => {
    const valueSelect = selectInput.value;
    if (valueSelect === '') {
      alert('Vui lòng chọn hành động');
      return;
    }

    const inputsChecked = document.querySelectorAll('[checkbox]:checked');
    if (inputsChecked.length === 0) {
      alert('Vui lòng chọn nhân viên');
      return;
    }

    if (valueSelect === 'role') {
      const roleValue = selectRole.querySelector('select').value;
      if (roleValue === '') {
        alert('Vui lòng chọn 1 vai trò');
        return;
      }

      if (roleValue === 'Editor') {
        const topicValue = selectTopic.querySelector('select').value;
        if (topicValue === '') {
          alert('Vui lòng chọn 1 chủ đề');
          return;
        }
      }
    }

    const confirmAction = confirm('Xác nhận hành động?');
    if (confirmAction) {
      const ids = Array.from(inputsChecked).map((input) => input.value);
      const inputSubmit = formActionMulti.querySelector('[ids]');
      inputSubmit.value = ids.join(', ');
      formActionMulti.submit();
    }
  });
}