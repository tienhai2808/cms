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
  selectInput.addEventListener('change', () => {
    const valueSelect = selectInput.value
    if (valueSelect === 'role') {
      selectRole.classList.remove('d-none')
    } else {
      if (!selectRole.classList.contains('d-none')) {
        selectRole.classList.add('d-none')
      }
    }
  })


  const buttonConfirm = formActionMulti.querySelector('[btn-confirm]')
  buttonConfirm.addEventListener('click', () => {
    const valueSelect = selectInput.value
    if (valueSelect === '') {
      alert('Vui lòng chọn hành động')
    } else {
      if (valueSelect === 'role') {
        const inputsChecked = document.querySelectorAll('[checkbox]:checked')
        const selectRole = document.querySelector('#select-role')
        if (inputsChecked.length > 0) {
          if (selectRole.value === '') {
            alert('Vui lòng chọn 1 vai trò')
          } else  {
            const confirmAction = confirm('Xác nhận hành động?')
            if (confirmAction) {
              ids = []
              inputsChecked.forEach((input) => {
                const id = input.value
                ids.push(id)
              })
              const inputSubmit = formActionMulti.querySelector('[ids]')
              inputSubmit.value = ids.join(', ')
              formActionMulti.submit()
            }
          }
        } else {
          alert('Vui lòng chọn bài đăng')
        }
      } else {
        const inputsChecked = document.querySelectorAll('[checkbox]:checked')
        if (inputsChecked.length > 0) {
          const confirmAction = confirm('Xác nhận hành động?')
          if (confirmAction) {
            ids = []
            inputsChecked.forEach((input) => {
              const id = input.value
              ids.push(id)
            })
            const inputSubmit = formActionMulti.querySelector('[ids]')
            inputSubmit.value = ids.join(', ')
            formActionMulti.submit()
          }
        } else {
          alert('Vui lòng chọn bài đăng')
        }
      }
    }
  })
}