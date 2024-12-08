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

const btnNoti = document.querySelector('.par-noti');
const divNoti = document.querySelector('.div-noti');
btnNoti.addEventListener('click', (e) => {
  e.stopPropagation(); 
  divNoti.classList.toggle('d-none');
});

document.addEventListener('click', (e) => {
  if (!divNoti.contains(e.target) && !btnNoti.contains(e.target)) {
    divNoti.classList.add('d-none');
  }
});

//Thời tiết
const locationWeather = document.querySelector('.header-weather-location')
const infoWeather = document.querySelector('.header-weather-info')
const imgWeather = document.querySelector('.header-weather-img')
const apiHeader = document.querySelector('#copy-right').getAttribute('error').replace(/[^a-zA-Z0-9]/g, '')

const fetchDataHeader = async (latitude, longitude) => {
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiHeader}&units=metric&lang=vi`
  try {
    const res = await fetch(apiUrl)
    return res.json()  
  } catch (err) {
    console.error(err)
  }
}

const weatherIconHeader = (id) => {
  if (id <= 232) return 'thunderstorm.svg'
  if (id <= 321) return 'drizzle.svg'
  if (id <= 531) return 'rain.svg'
  if (id <= 622) return 'snow.svg'
  if (id <= 781) return 'atmosphere.svg'
  if (id <= 800) return 'clear.svg'
  else return 'clouds.svg'
}

const loadWeatherHeader = async () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async (position) => {
      const { latitude, longitude } = position.coords
      const weatherData = await fetchDataHeader(latitude, longitude)
      updateWeatherHeader(weatherData)
    }, async () => {
      await fetchDefaultWeather()
    })
  } else {
    await fetchDefaultWeather()
  }
}

const fetchDefaultWeather = async () => {
  const latDefault = 21.028511
  const lonDefault = 105.804817
  const weatherData = await fetchDataHeader(latDefault, lonDefault)
  updateWeatherHeader(weatherData)
}

const updateWeatherHeader = ({ name: locat, main: { temp }, weather: [{ id }] }) => {
  locationWeather.textContent = locat
  infoWeather.textContent = `${Math.round(temp)}°C`
  imgWeather.src = `/static/svg/assets/${weatherIconHeader(id)}`
}

loadWeatherHeader()