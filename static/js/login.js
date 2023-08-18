function login() {
    var phoneInput = document.getElementById("phoneInput").value;
    // 로그인 처리 및 적립금 정보를 얻어오는 로직을 추가
    // 로그인 후, 적립금 페이지로 이동
    window.location.href = "main.html" + encodeURIComponent(phoneInput);
  }