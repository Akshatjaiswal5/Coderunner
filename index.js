function run(){
 const code=document.getElementById("codebox");
 const shell=document.getElementById("shellbox");

 api='https://newsapi.org/v2/everything?q=tesla&from=2021-09-01&sortBy=publishedAt&apiKey=';
 api+=code.value;
 fetch(api)
  .then(response => response.json())
  .then(data => JSON.stringify(data))
  .then(data => shell.innerHTML=data);
}