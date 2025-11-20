<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SiKiBiDi System</title>

<style>
/* ===== NỀN BODY LỚN ===== */
body {
    margin: 0;
    padding: 0;
    background: url("tumblr_1d630f6c1cc1060d4508b364d7478c12_96bc866c_540.gif") no-repeat center center fixed;
    background-size: cover;
    font-family: Arial, sans-serif;
    color: white;
}

/* ===== LOGIN BOX ===== */
#loginBox {
    width: 85%;
    max-width: 350px;
    margin: 90px auto;
    padding: 18px;
    text-align: center;
    border-radius: 15px;

    background: url("d66a1f1b2b3bfe7dffba1a8802402796.gif") no-repeat center center;
    background-size: cover;

    border: 8px solid transparent;
    border-image: url("9Z0EOC.gif") 30 round;
    animation: borderRun 4s linear infinite;
}

@keyframes borderRun {
    from { border-image-slice: 10; }
    to   { border-image-slice: 40; }
}

input {
    width: 93%;
    padding: 10px;
    margin-top: 7px;
    border-radius: 6px;
    border: none;
}

button {
    width: 95%;
    padding: 10px;
    margin-top: 12px;
    border: none;
    background: #0066ff;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 6px;
    cursor: pointer;
}

/* ===== MENU ===== */
#menu {
    display: none;
    padding: 20px;
}

.menuBox {
    position: relative;
    background: url("hinh-anh-gif-thanh-pho-hien-dai.gif") no-repeat center center;
    background-size: cover;
    padding: 15px;
    margin-bottom: 18px;
    border-radius: 12px;
    border: 6px solid transparent;
    border-image: url("9Z0EOC.gif") 30 round;
    animation: borderRun 4s linear infinite;
    overflow: hidden;
}

/* Overlay chữ nổi bật */
.menuBox::after {
    content: "";
    position:absolute;
    top:0; left:0; width:100%; height:100%;
    background: url("2f6d5L.gif") no-repeat center center;
    background-size: cover;
    opacity:0.3;
    pointer-events:none;
}

.menuBox h3 { margin: 0 0 10px 0; color: #00e1ff; }

/* OUTPUT BOX */
.output {
    margin-top: 10px;
    padding: 10px;
    background: rgba(0,0,0,0.4);
    border-radius: 6px;
    max-height: 200px;
    overflow-y: auto;
}
</style>
</head>
<body>

<!-- ========== LOGIN ========== -->
<div id="loginBox">
    <h2>Đăng Nhập Hệ Thống</h2>
    <input id="user" type="text" placeholder="Tên đăng nhập">
    <input id="pass" type="password" placeholder="Mật khẩu">
    <button onclick="login()">Đăng Nhập</button>
    <p id="loginMsg"></p>
</div>

<!-- ========== MENU ========== -->
<div id="menu">

    <!-- CHECK BAN -->
    <div class="menuBox">
        <h3>Check Ban UID</h3>
        <input id="banUID" placeholder="Nhập UID">
        <button onclick="checkBan()">Kiểm Tra</button>
        <div id="banResult" class="output"></div>
    </div>

    <!-- GỬI EMAIL KHÔI PHỤC -->
    <div class="menuBox">
        <h3>Khôi Phục Email</h3>
        <input id="emailInput" placeholder="Nhập Email">
        <button onclick="sendEmail()">Gửi</button>
        <div id="emailResult" class="output"></div>
    </div>

    <!-- JOIN CLAN -->
    <div class="menuBox">
        <h3>Tham Gia Quân Đoàn</h3>
        <input id="clanID" placeholder="UID Quân Đoàn">
        <input id="tokenID" placeholder="Token của bạn">
        <button onclick="joinClan()">Tham Gia</button>
        <div id="clanResult" class="output"></div>
    </div>

    <!-- UPDATE BIO -->
    <div class="menuBox">
        <h3>Update Bio</h3>
        <input id="bioToken" placeholder="Nhập Access Token">
        <input id="newBio" placeholder="Nhập Bio mới">
        <button onclick="updateBio()">Cập Nhật</button>
        <div id="bioResult" class="output"></div>
    </div>

</div>

<script>
/* ===== LOGIN ===== */
function login() {
    let u = document.getElementById("user").value;
    let p = document.getElementById("pass").value;

    if (u === "Sikibidi" && p === "sikibidi888") {
        document.getElementById("loginMsg").innerHTML = "Đăng nhập thành công ✔️";
        document.getElementById("loginBox").style.display = "none";
        document.getElementById("menu").style.display = "block";
    } else {
        document.getElementById("loginMsg").innerHTML = "Sai tài khoản hoặc mật khẩu ❌";
    }
}

/* ===== HÀM CHUNG XỬ LÝ API ===== */
async function handleAPI(url, outputBox, successCheck) {
    try {
        let res = await fetch(url);
        let data = await res.json();

        let jsonHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";

        if(successCheck(data)) {
            outputBox.innerHTML = "Thành công ✔️<br>" + jsonHTML;
        } else {
            outputBox.innerHTML = "Lỗi ❌<br>" + jsonHTML;
        }
    } catch(err) {
        outputBox.innerHTML = "Lỗi ❌<br>" + err;
    }
}

/* ===== CHECK BAN ===== */
function checkBan() {
    let uid = document.getElementById("banUID").value;
    let box = document.getElementById("banResult");
    if(!uid) return box.innerHTML="Vui lòng nhập UID ❌";

    let url = `https://amin-team-api.vercel.app/check_banned?player_id=${uid}`;
    handleAPI(url, box, data => data && data.banned === false);
}

/* ===== GỬI EMAIL ===== */
function sendEmail() {
    let email = document.getElementById("emailInput").value;
    let box = document.getElementById("emailResult");
    if(!email) return box.innerHTML="Vui lòng nhập Email ❌";

    let url = `https://fearless-opt-api.vercel.app/opt?email=${email}&password=fearless&action=email`;
    handleAPI(url, box, data => data && (data.message === "sent" || data.success));
}

/* ===== JOIN CLAN ===== */
function joinClan() {
    let clan = document.getElementById("clanID").value;
    let token = document.getElementById("tokenID").value;
    let box = document.getElementById("clanResult");
    if(!clan || !token) return box.innerHTML="Thiếu UID hoặc Token ❌";

    let url = `https://ffguildapi-live.vercel.app/joinclan?clan_id=${clan}&jwt_token=${token}`;
    handleAPI(url, box, data => data && data.success);
}

/* ===== UPDATE BIO ===== */
function updateBio() {
    let token = document.getElementById("bioToken").value;
    let bio = document.getElementById("newBio").value;
    let box = document.getElementById("bioResult");
    if(!token || !bio) return box.innerHTML="Vui lòng nhập đầy đủ ❌";

    let url = `https://bio.thug4ff.com/update_bio?access_token=${token}&bio=${encodeURIComponent(bio)}&key=nexx`;
    handleAPI(url, box, data => data && (data.success || data.status === "success"));
}
</script>

</body>
</html>