// Chèn Thứ - Ngày - Tháng - Năm vào Header
const options = { weekday: "long", year: "numeric", month: "numeric", day: "numeric", };
const today = new Date().toLocaleDateString("vi-VN", options);
document.querySelector("li.time").textContent = today;

// Đóng & Mở hộp Search
const btnSearch = document.querySelector(".btn-search");
const inputSearch = document.querySelector(".ip-search");

btnSearch.addEventListener("click", () => {
  if (inputSearch.value && inputSearch.classList.contains('open')) {
    const formSearch = inputSearch.closest('form')
    formSearch.submit()
  }
  inputSearch.classList.toggle('open')
});
const formSearch = document.querySelector('[form-search]')
formSearch.addEventListener('submit', () => {
  inputSearch.classList.toggle('open')
})


// Đóng & Mở Mega Menu
const megaMenu = document.querySelector(".mega-menu");
const closeMenu = document.querySelector(".close-btn");
const menuBar = document.querySelector(".bar");

menuBar.addEventListener("click", () => {
  megaMenu.classList.toggle("open");
});
closeMenu.addEventListener("click", () => {
  megaMenu.classList.remove("open");
});

// Mở xem thêm
function showMore(more) {
  var ul = more.closest("ul");
  var hideItems = ul.querySelectorAll(".line-hide.hide");
  if (hideItems.length > 0) {
    hideItems.forEach(function (item) {
      item.classList.remove("hide");
    });
    more.innerText = "Thu gọn";
  } else {
    var allItems = ul.querySelectorAll(".line-hide");
    allItems.forEach(function (item) {
      item.classList.add("hide");
    });
    more.innerText = "Xem thêm";
  }
}

// Lướt bài viết gần đây 
const wrapper = document.querySelector('.main-viewed');
const btnLeft = document.querySelector('.scroll-left');
const btnRight = document.querySelector('.scroll-right');
const postDiv = document.querySelector('.post-viewed');

if (postDiv) {
  const postWidth = postDiv.offsetWidth
  if (btnLeft && btnRight) {
    btnLeft.addEventListener('click', () => {
      wrapper.scrollBy({ left: -postWidth * 2, behavior: 'smooth' });
    });
    
    btnRight.addEventListener('click', () => {
      wrapper.scrollBy({ left: postWidth * 2, behavior: 'smooth' });
    });
  }
}

