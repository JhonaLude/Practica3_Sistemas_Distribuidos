function run(url){

document.getElementById("resultado").textContent = "Procesando...";

fetch(url)
.then(response => response.json())
.then(data => {
    document.getElementById("resultado").textContent = data.resultado;
});

}