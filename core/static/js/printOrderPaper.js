function imprimirComanda(div){
    let comanda = document.getElementById(div).innerHTML;
    let conteudoHTML = document.body.innerHTML;

    document.body.innerHTML = comanda;
    window.print();

    document.body.innerHTML = conteudoHTML;
}