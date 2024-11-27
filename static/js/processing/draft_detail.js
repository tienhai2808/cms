const formAction = document.querySelector("[form-action]");
const btnSend = document.querySelector('[btn-send]')
const btnDelete = document.querySelector('[btn-delete]')
if (formAction) {
  btnDelete.addEventListener("click", () => {
    const confirmDelete = confirm("Xác nhận xóa bản nháp?");
    if (confirmDelete) {
      formAction.querySelector('[hidden]').value = 'delete'
      formAction.submit();
    }
  });
  btnSend.addEventListener('click', () => {
    const confirmSend = confirm('Xác nhận gửi bản nháp tới Tổng biên tập?')
    if (confirmSend) {
      formAction.querySelector('[hidden]').value = 'send'
      formAction.submit()
    }
  })
}
