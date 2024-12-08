const formSortBy = document.querySelector('#form-sort-by')
const selectSortBy = formSortBy.querySelector('select')
selectSortBy.addEventListener('change', () => {
  formSortBy.submit()
})
