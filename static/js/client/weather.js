const weatherForm = document.querySelector('.form-search')
const locationInput = weatherForm.querySelector('input')
const searchBtn = weatherForm.querySelector('button')
const noDiv = document.querySelector('.no-result')
const notFoundDiv = document.querySelector('.notfound-result')
const bigDiv = document.querySelector('.big-result')
const mainResult = document.querySelector('.main-result')
const locationName = document.querySelector('.name-location')
const tempText = document.querySelector('.weather-now-info')
const maxTempText = document.querySelector('.max-temp-txt')
const minTempText = document.querySelector('.min-temp-txt')
const condiText = document.querySelector('.weather-now-condition')
const humidityText = document.querySelector('.hudimity-txt')
const windText = document.querySelector('.wind-txt')
const feelText = document.querySelector('.feel-txt')
const weatherImg = document.querySelector('.weather-now-img')
const forecastDiv = document.querySelector('.forecast-weather')

const apiKey = document.querySelector('#copy-right').getAttribute('error').replace(/[^a-zA-Z0-9]/g, '')

const showDisplayDiv = (div) => {
  [bigDiv, notFoundDiv, noDiv].forEach(section => section.style.display = 'none')
  div.style.display = 'block'
}
showDisplayDiv(noDiv)

searchBtn.addEventListener('click', () => {
  if (locationInput.value.trim() != '') {
    updateWeatherInfo(locationInput.value)
    locationInput.blur()
  }
})

locationInput.addEventListener('keydown', (e) => {
  if (e.key == 'Enter' &&  locationInput.value.trim() != '') {
    updateWeatherInfo(locationInput.value)
    locationInput.blur()
  }
})

const getFetchData = async (endPoint, loca) => {
  const apiUrl = `https://api.openweathermap.org/data/2.5/${endPoint}?q=${loca}&appid=${apiKey}&units=metric&lang=vi`
  try {
    const res = await fetch(apiUrl)
    return res.json()  
  } catch (err) {
    console.error(err)
  }
}

const getWeatherIcon = (id) => {
  if (id <= 232) return 'thunderstorm.svg'
  if (id <= 321) return 'drizzle.svg'
  if (id <= 531) return 'rain.svg'
  if (id <= 622) return 'snow.svg'
  if (id <= 781) return 'atmosphere.svg'
  if (id <= 800) return 'clear.svg'
  else return 'clouds.svg'
}

const updateWeatherInfo = async (loca) => {
  const weatherData = await getFetchData('weather', loca)
  if (weatherData.cod != 200) {
    showDisplayDiv(notFoundDiv)
    return
  }

  const {
    name: locat,
    main: { temp, humidity, feels_like, temp_max, temp_min },
    weather: [{ id, description }],
    wind: { speed }
  } = weatherData

  locationName.textContent = locat
  tempText.textContent = `${Math.round(temp)}°C`
  condiText.textContent = description.charAt(0).toUpperCase() + description.slice(1)
  feelText.textContent = `${Math.round(feels_like)}°C`
  maxTempText.textContent = `${Math.round(temp_max)}°C`
  minTempText.textContent = `${Math.round(temp_min)}°C`
  windText.textContent = `${speed} M/s`
  humidityText.textContent = `${humidity}%`
  weatherImg.src = `/static/svg/assets/${getWeatherIcon(id)}`
  
  await updateForecastsInfo(loca)
  showDisplayDiv(bigDiv)
}

const updateForecastsInfo = async (loca) => {
  const forecastData = await getFetchData('forecast', loca)
  const timeTaken = '12:00:00'

  forecastDiv.innerHTML = ''
  forecastData.list.forEach(f => {
    if (f.dt_txt.includes(timeTaken))  {
      updateForecastItems(f)
    }
  }
  )
}

const updateForecastItems = (weatherData) => {
  const {
    dt_txt: date,
    weather: [{ id }],
    main: { temp }
  } = weatherData

  const dateTaken = new Date(date)
  const dateResult = dateTaken.toLocaleDateString('vi-VN', {
    weekday: 'long',  
    day: 'numeric',   
    month: 'numeric'  
  })

  const forcastItem = `
    <div class="forecast-item">
      <h6 class="forecast-iem-date text-center">${dateResult}</h6>
      <div class="w-100 d-flex justify-content-center">
        <img src="/static/svg/assets/${getWeatherIcon(id)}" class="forecast-img">
      </div>
      <h6 class="text-center">${Math.round(temp)}°C</h6>
    </div>
  `
  forecastDiv.insertAdjacentHTML('beforeend', forcastItem)
}
