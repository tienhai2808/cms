const formPending = document.querySelector('[form-pending]')
const btnAccept = document.querySelector('[btn-accept]')
const btnRefuse = document.querySelector('[btn-refuse]')
if (formPending) {
  btnAccept.addEventListener('click', () => {
    const confirmAccept = confirm('Duyệt bản nháp này?')
    if (confirmAccept) {
      formPending.querySelector('[hidden]').value = 'accept'
      formPending.submit()
    }
  })
  btnRefuse.addEventListener('click', () => {
    const confirmRefuse = confirm('Từ chối bản nháp này?')
    if (confirmRefuse) {
      formPending.querySelector('[hidden]').value = 'refuse'
      formPending.submit()
    }
  })
}

const formSend = document.querySelector('[form-send]')
const btnSend = document.querySelector('[btn-send]')
if (formSend) {
  btnSend.addEventListener('click', () => {
    const confirmSend = confirm('Gửi bài viết lên Tổng biên tập?')
    if (confirmSend) {
      formSend.submit()
    }
  })
}

const formDelete = document.querySelector("[form-delete]");
const btnDelete = document.querySelector("[btn-delete]");
if (formDelete) {
  btnDelete.addEventListener("click", () => {
    const confirmDelete = confirm("Xác nhận xóa bài viết?");
    if (confirmDelete) {
      formDelete.submit();
    }
  });
}

const btnPost = document.querySelector('[btn-post]')
const divPost = document.querySelector('.div-post')
const formPost = document.querySelector(".form-post")
const closePost = document.querySelector('.fa-circle-xmark')
if (btnPost) {
  btnPost.addEventListener('click', () => {
    divPost.classList.toggle('d-none')
  })
}

if (closePost) {
  closePost.addEventListener('click', () => {
    if (!divPost.classList.contains('d-none')) {
      divPost.classList.add('d-none')
    }
  })
}

if (formPost) {
  const btnSubmit= formPost.querySelector('[btn-submit]')
  btnSubmit.addEventListener('click', () => {
    const startTime = formPost.querySelector('#start-time')
    const endTime = formPost.querySelector('#end-time')
    if (startTime.value === '' && endTime.value === '') {
      const confirmPost = confirm('Đăng bài viết ở mọi khung giờ?')
      if (confirmPost) {
        formPost.submit()
      }
    } else if (startTime.value === '' || endTime.value === '') {
      alert('Chọn khung giờ đăng')
      return
    } else {
      const confirmPost = confirm('Xác nhận đăng bài?')
      if (confirmPost) {
        formPost.submit()
      }
    }
  })
}
