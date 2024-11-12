const inputFields = document.querySelectorAll('input')
if (inputFields) {
  inputFields.forEach((input) => {
    if (input.getAttribute('type') !== 'checkbox') {
      input.classList.add('form-control')
    }
  })
}

const section = document.querySelector('#id_topic')
if (section) {
  section.classList.add('form-select')
}

const topic = document.querySelector('#id_section') 
if (topic) {
  topic.classList.add('form-select')
}

const textarea =  document.querySelector('textarea')
if (textarea) {
  textarea.removeAttribute('required')
}

const labelFields = document.querySelectorAll('label')
if (labelFields) {
  labelFields.forEach((label) => {
    label.classList.add('fw-semibold')
  })
}

const formCreate = document.querySelector('[form-create]')
if (formCreate) {
  const btnSend = formCreate.querySelector('[btn-send]')
  btnSend.addEventListener('click', () => {
    if (formCreate.checkValidity()) {
      const confirmSend = confirm('Xác nhận gửi bản nháp đến Tổng biên tập?')
      if (confirmSend) {
        const inputHidden = formCreate.querySelector('[hidden]')
        inputHidden.value = 'send'
      }
      formCreate.submit()
    } else {
      formCreate.reportValidity()
    }
  })
}