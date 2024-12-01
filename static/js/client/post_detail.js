const formComment = document.querySelector("[form-comment]");
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

const btnEnjoy = document.querySelector(".btn-enjoy");
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

const btnShare = document.querySelector('.btn-share')
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
