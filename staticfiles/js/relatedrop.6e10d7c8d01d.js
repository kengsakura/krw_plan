  function check(){
  if (document.getElementById('_password').value == document.getElementById('_repassword').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = ' ตรง';
    document.getElementById('submit').disabled = false;
  } else {
  document.getElementById('message').style.color = 'red';
  document.getElementById('message').innerHTML = ' ไม่ตรง';
  document.getElementById('submit').disabled = true;
  }
  }