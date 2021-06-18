const form = document.getElementById("register-form")
form.addEventListener("submit", event => {
  event.preventDefault()
  const formData = new FormData(form)
  const data = {}
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    data[key] = value
    /* USER CODE Begin: Validate data */
  }
  if(data['password'] != data['confirmpassword'])
  {
    alert('รหัสผ่านกับยืนยันรหัสผ่านไม่ตรงกัน')
    document.getElementsByName('password')[0].value = ""
    document.getElementsByName('confirmpassword')[0].value = ""
  }else
  {
    console.log(data)
  }
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
})