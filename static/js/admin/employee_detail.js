const formEmp = document.querySelector('.form-emp')
const btnRole = document.querySelector('.btn-role')
const btnDelete = document.querySelector('.btn-delete')
const roleEmp = document.querySelector('[data-role]').textContent
const divTakeCharge = document.querySelector('.div-take-charge')
const btnClose = document.querySelector('.fa-circle-xmark')
const btnSubmit = document.querySelector('[btn-submit]')
const selectTopic = divTakeCharge.querySelector('select')
const textNote = divTakeCharge.querySelector('p')
const btnTakeCharge = document.querySelector('.btn-take-charge')

btnDelete.addEventListener('click', () => {
  const confirmDelete = confirm("Bạn muốn xóa nhân viên này chứ?")
  if (confirmDelete) {
    formEmp.querySelector("input[name='action']").value = 'delete'
    formEmp.submit()
  }
})

btnRole.addEventListener('click', () => {
  if (roleEmp === 'Editor') {
    const confirmRole = confirm('Bạn muốn đổi nhân viên này thành Contributor chứ?')
    if (confirmRole) {
      formEmp.querySelector("input[name='action']").value = 'editor_to_contributor'
      formEmp.submit()
    }
  } else {
    textNote.textContent = 'Nhân viên này là Contributor, nếu đổi vai trò vui lòng chọn chủ đề đảm nhiệm'
    if (divTakeCharge.classList.contains('d-none')) {
      divTakeCharge.classList.remove('d-none')
    }
  }
})

if (btnTakeCharge) {
  btnTakeCharge.addEventListener('click', () => {
    if (divTakeCharge.classList.contains('d-none')) {
      divTakeCharge.classList.remove('d-none')
    }
  })
}

btnClose.addEventListener('click', () => { 
  if (!divTakeCharge.classList.contains('d-none')) {
    divTakeCharge.classList.add('d-none')
  }
})

btnSubmit.addEventListener('click', () => {
  if (selectTopic.value === '') {
    alert('Vui lòng chọn 1 chủ đề')
  } else {
    const valueSubmit = roleEmp === 'Editor' ? 'editor_to_editor' : 'contributor_to_editor'
    const message = roleEmp === 'Editor' 
      ? `Bạn muốn đổi chủ đề cho Editor này thành ${selectTopic.value} chứ?` 
      : `Bạn muốn đổi nhân viên này thành Editor với chủ đề ${selectTopic.value} chứ?`
    const confirmTakeCharge = confirm(message)
    if (confirmTakeCharge) {
      formEmp.querySelector("input[name='action']").value = valueSubmit
      formEmp.querySelector("input[name='take_charge']").value = selectTopic.value
      formEmp.submit()
    }
  }
})

