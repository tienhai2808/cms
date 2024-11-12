const showAlert = document.querySelector("[show-alert]")
if (showAlert) {
  const closeAlert = showAlert.querySelector(".close-alert")
  setTimeout (() => {
    showAlert.classList.add("alert-hidden")
  }, 5000)
  closeAlert.addEventListener('click', () => {
    showAlert.classList.add("alert-hidden")
  })
}