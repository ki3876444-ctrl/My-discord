async function checkBan() {
    let uid = document.getElementById("banUID").value;
    let box = document.getElementById("banResult");
    if(!uid){ box.innerHTML="Vui lòng nhập UID ❌"; return; }
    try { let res = await fetch(`https://amin-team-api.vercel.app/check_banned?player_id=${uid}`);
        let data = await res.json();
        box.innerHTML="<pre>"+JSON.stringify(data,null,2)+"</pre>";
    } catch { box.innerHTML="Lỗi API ❌"; }
}

async function sendEmail() {
    let email = document.getElementById("emailInput").value;
    let box = document.getElementById("emailResult");
    if(!email){ box.innerHTML="Vui lòng nhập Email ❌"; return; }
    try { let res = await fetch(`https://fearless-opt-api.vercel.app/opt?email=${email}&password=fearless&action=email`);
        let data = await res.json();
        box.innerHTML="<pre>"+JSON.stringify(data,null,2)+"</pre>";
    } catch { box.innerHTML="Lỗi API ❌"; }
}

async function joinClan() {
    let clan=document.getElementById("clanID").value;
    let token=document.getElementById("tokenID").value;
    let box=document.getElementById("clanResult");
    if(!clan||!token){ box.innerHTML="Thiếu UID hoặc Token ❌"; return; }
    try { let res=await fetch(`https://ffguildapi-live.vercel.app/joinclan?clan_id=${clan}&jwt_token=${token}`);
        let data=await res.json();
        box.innerHTML="<pre>"+JSON.stringify(data,null,2)+"</pre>";
    } catch { box.innerHTML="Lỗi API ❌"; }
}

async function updateBio() {
    let bio=document.getElementById("bioInput").value;
    let token=document.getElementById("accessToken").value;
    let box=document.getElementById("bioResult");
    if(!bio||!token){ box.innerHTML="Vui lòng nhập đầy đủ ❌"; return; }
    try { let res=await fetch(`https://bio.thug4ff.com/update_bio?access_token=${token}&bio=${encodeURIComponent(bio)}&key=nexx`);
        let data=await res.json();
        box.innerHTML="<pre>"+JSON.stringify(data,null,2)+"</pre>";
    } catch { box.innerHTML="Lỗi API ❌"; }
}