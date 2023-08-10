/*
    Made by Lamberto Ruiz Martínez
    GitHub: https://github.com/LambertoRM/
*/

function imagen_subida(){
    document.getElementById('archivo').onchange = function () {
        console.log(this.value);
        document.getElementById('label_archivo').innerHTML = document.getElementById('archivo').files[0].name;
    }
}

function gif(){
    document.getElementById('loading_gif').style.display = "block";
}