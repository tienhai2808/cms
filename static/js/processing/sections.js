const btnCreate = document.querySelector('.btn-create')
const divSection = document.querySelector('.div-section')
const closeSection = document.querySelector('.fa-circle-xmark')
btnCreate.addEventListener('click', () => {
  divSection.classList.toggle('d-none')
})
closeSection.addEventListener('click', () => {
  if (!divSection.classList.contains('d-none')) {
    divSection.classList.add('d-none')
  }
})

const btnDeletes = document.querySelectorAll('.btn-delete')
const formDelete = document.querySelector('[form-delete]')
if (btnDeletes.length > 0) {
  btnDeletes.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmDelete = confirm('Xóa danh mục này?')
      if (confirmDelete) {
        formDelete.querySelector("input[name='id_section']").value = btn.getAttribute('id')
        formDelete.submit()
      }
    })
  })
}