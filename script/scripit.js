function getRndInteger(min,max){
    let numero = Math.floor(Math.random() * (max - min + 1 ))
 + min;
 return numero
}
function Revelar(e){
    e.style.color = "black";
  
}

function sorteador(){
    let cqtde = document.getElementById('qtde')
    let cmin = document.getElementById('min')
    let cmax = document.getElementById('max')
    let cnumeros = document.getElementById('numeros')
    let crevelar = document.getElementById('revelar') 
    console.log(crevelar.value)
    

    let qtde =  parseInt(cqtde.value);
    let min = parseInt(cmin.value);
    let max = parseInt(cmax.value);
    
    let numero = 0;
    let texto = "";

    for (let i = 1; i <= qtde ; i++) {
        numero =  getRndInteger(min,max);
        if(crevelar.checked==false){ 
            texto += `<p class ="numero">${numero}</p>`
        }
        else{
            texto +=  `<p class ="numerorevel" onclick="Revelar(this)">${numero}</p>`
        }
    }   

    cnumeros.innerHTML = texto;
}
