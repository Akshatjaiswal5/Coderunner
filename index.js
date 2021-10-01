function run(){
 const code=document.getElementById("codebox");
 const shell=document.getElementById("shellbox");

 var myBlob = new Blob(["CONTENT"], {type: 'text/plain'});
 var anchor = document.createElement("a");
 anchor.download = "demo.txt";
 anchor.url = window.URL.createObjectURL(myBlob);
 anchor.click();

 api='https://newsapi.org/v2/everything?q=tesla&from=2021-09-01&sortBy=publishedAt&apiKey=';
 api+=code.value;
 fetch(api)
  .then(response => response.json())
  .then(data => JSON.stringify(data))
  .then(data => shell.innerHTML=data);
}