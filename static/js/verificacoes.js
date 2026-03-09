// let nome= prompt("como você se chama?")
// // "lucas" = a ''
// // 1 === '1' -> falso
// if (nome == null){
//     alert("recarregue a pagina")
// }
// else{
//     let correto =confirm("você se chama" + nome +"?")
//
//     if (correto)  {
//         alert(nome + " Bem vindo(a) ao site de cursos")}
//     else{
//         alert("recarregue a página")}
// }
//

function limpainputsLogin(){
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')
    const inputNome = document.getElementById('input-nome') // Adicionado para o cadastro

    if(inputEmail) inputEmail.value = '';
    if(inputSenha) inputSenha.value = '';
    if(inputNome) inputNome.value = '';

    if(inputEmail) inputEmail.classList.remove('is-invalid');
    if(inputSenha) inputSenha.classList.remove('is-invalid');
    if(inputNome) inputNome.classList.remove('is-invalid');
}

document.addEventListener("DOMContentLoaded", function () {
    // FORMULÁRIO DE LOGIN
    const formLogin = document.getElementById('form-login')
    if (formLogin) {
        formLogin.addEventListener("submit", function (event){
            const inputEmail = document.getElementById('input-email')
            const inputSenha = document.getElementById('input-senha')
            let temErro = false

            if (inputEmail.value === ''){
                inputEmail.classList.add('is-invalid'); temErro = true;
            } else {
                inputEmail.classList.remove('is-invalid');
            }

            if (inputSenha.value === ''){
                inputSenha.classList.add('is-invalid'); temErro = true;
            } else {
                inputSenha.classList.remove('is-invalid');
            }

            if (temErro){
                event.preventDefault();
                alert("Preencha todos os campos");
            }
        })
    }

    // FORMULÁRIO DE CADASTRO
    const formCadastro = document.getElementById('form-cadastro') // Definindo a variável
    if (formCadastro) {
        formCadastro.addEventListener("submit", function (event){
            const inputNome = document.getElementById('input-nome') // ID correto
            const inputEmail = document.getElementById('input-email')
            const inputSenha = document.getElementById('input-senha')
            let temErro = false

            if (inputNome && inputNome.value === ''){
                inputNome.classList.add('is-invalid'); temErro = true;
            } else if(inputNome) {
                inputNome.classList.remove('is-invalid');
            }

            if (inputEmail.value === ''){
                inputEmail.classList.add('is-invalid'); temErro = true;
            } else {
                inputEmail.classList.remove('is-invalid');
            }

            if (inputSenha.value === ''){
                inputSenha.classList.add('is-invalid'); temErro = true;
            } else {
                inputSenha.classList.remove('is-invalid');
            }

            if (temErro){
                event.preventDefault();
                alert("Preencha todos os campos");
            }
        })
    }
})
