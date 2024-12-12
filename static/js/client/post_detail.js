const formComment = document.querySelector("[form-comment]")
const btnTTS = document.querySelector('.btn-tts')
const postAudio = document.querySelector('#post-audio')
const btnEnjoy = document.querySelector(".btn-enjoy")
const btnShare = document.querySelector('.btn-share')
const divFontSize = document.querySelector('.div-font-size')
const btnFontSize = document.querySelector('.btn-font-size')
const closeFontSize = divFontSize.querySelector('#close-font-size')

formComment.addEventListener("click", () => {
  const checkUser = formComment.getAttribute("user");
  if (!checkUser) {
    window.location.href = "/login/";
  }
});

const getCookie = (name) => {
  const cookies = document.cookie?.split(";") || [];
  const cookie = cookies.find((c) => c.trim().startsWith(`${name}=`));
  return cookie ? decodeURIComponent(cookie.trim().substring(name.length + 1)) : null;
};
const csrftoken = getCookie("csrftoken");

btnEnjoy.addEventListener("click", (e) => {
  const checkUser = document.querySelector("[form-comment]").getAttribute("user");
  if (!checkUser) {
    window.location.href = "/login/";
    e.preventDefault();
    return;
  } else {
    e.preventDefault();
    const postSlug = btnEnjoy.getAttribute("data-post-slug");
    $.ajax({
      type: "POST",
      url: `/posts/${postSlug}/`,
      data: {
        enjoy: 'Hello world',
        csrfmiddlewaretoken: csrftoken,
      },
      success: (res) => {
        if (res.status === "added") {
          btnEnjoy.innerHTML = '<i class="fa-solid fa-bookmark"></i> Đã lưu';
        } else {
          btnEnjoy.innerHTML = '<i class="fa-regular fa-bookmark"></i> Lưu';
        }
      },
    });
  }
});

btnShare.addEventListener('click', async () => {
  if (navigator.share) {
    try {
      await navigator.share({
        title: document.title,
        text: 'Xem bài viết này',
        url: window.location.href
      }) 
    } catch (error) {
      console.log(error)
    }
  } else {
    alert('Trình duyệt không hỗ trợ chia sẻ')
  }
})

btnTTS.addEventListener('click', (e) => {
  e.preventDefault()
  const postSlug = btnTTS.getAttribute('data-post-slug')
  $('#loading').show()
  $.ajax({
    type: "POST",
    url: `/posts/${postSlug}/`,
    data: {
      tts: 'Hello world',
      csrfmiddlewaretoken: csrftoken,
    },
    success: (res) => {
      postAudio.classList.remove('d-none')
      $('#tts-audio').attr('src', res.audio_url)
      $('#tts-audio')[0].play()
    },
    error: () => {
      alert('Có lỗi xảy ra')
    }, 
    complete: () => {
      $('#loading').hide()
    }
  });
})

$('#close-audio').click(() => {
  var audio = $('#tts-audio')[0]
  audio.pause()
  audio.currentTime = 0;
  postAudio.classList.add('d-none')
}) 

btnFontSize.addEventListener('click', () => {
  divFontSize.classList.toggle('d-none')
})

closeFontSize.addEventListener('click', () => {
  if (!divFontSize.classList.contains('d-none')) {
    divFontSize.classList.add('d-none')
  }
})


const divContentPost = document.querySelector('.post-content');
const fsSmaller = document.querySelector('.fs-smaller');
const fsBigger = document.querySelector('.fs-bigger');
const reloadFs = document.querySelector('.reload-fs');

const setFontSize = (size) => {
  divContentPost.style.fontSize = `${size}px`;
  localStorage.setItem('fontSize', `${size}px`);
  updateButtonState(size);
};

const updateButtonState = (size) => {
  fsSmaller.style.color = size <= 16 ? '#b9b9b9' : 'black';
  fsBigger.style.color = size >= 24 ? '#b9b9b9' : 'black';
};

window.addEventListener('load', () => {
  const savedFontSize = localStorage.getItem('fontSize');
  const initialSize = savedFontSize ? parseInt(savedFontSize) : 20;
  setFontSize(initialSize);
});

fsBigger.addEventListener('click', () => {
  let currentSize = parseInt(window.getComputedStyle(divContentPost).fontSize);
  if (currentSize < 24) setFontSize(currentSize + 2);
});

fsSmaller.addEventListener('click', () => {
  let currentSize = parseInt(window.getComputedStyle(divContentPost).fontSize);
  if (currentSize > 16) setFontSize(currentSize - 2);
});

reloadFs.addEventListener('click', () => setFontSize(20));
