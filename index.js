function run(){
 
  const code=document.getElementById("codebox");
 
  const shell=document.getElementById("shellbox");

  const data = { inputcode: code.value };  
  
  fetch('http://localhost:5000/login',{
   method: 'POST',
   headers:{ 'Content-Type': 'application/json',},
   body:JSON.stringify(data),
  })
  .then(response => response.json())


  .then(response => shell.innerHTML=response.outputcode)
 }
