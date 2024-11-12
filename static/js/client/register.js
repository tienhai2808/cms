document.querySelector('#id_usable_password').remove()
document.querySelector('#id_usable_password_helptext').remove()
document.querySelector('#id_username_helptext').remove()

const pTag = document.querySelectorAll('p')
if (pTag.length > 0) {
  pTag[8].remove()
  pTag.forEach((p) => {
    p.classList.add('input-info')
  })
  pTag.forEach((p) => {
    const inputDiv = p.querySelector('input')
    const labelDiv = p.querySelector('label')
    if (inputDiv && labelDiv) {
      p.insertBefore(inputDiv, labelDiv)
    }
  })
}
