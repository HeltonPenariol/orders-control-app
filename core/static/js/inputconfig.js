function maisTaxaEntrega(){
    let atual = document.getElementById("taxa_entrega").value;
    let novo = atual - (- 0.5);
    document.getElementById("taxa_entrega").value = novo; 
}

function menosTaxaEntrega(){
    let atual = document.getElementById("taxa_entrega").value;
    if(atual > 0){
        let novo = atual - 0.5;
        document.getElementById("taxa_entrega").value = novo;
    }
}

function removerTaxaEntrega(){
    let atual = document.getElementById("taxa_entrega").value;
    if(atual > 0){
        let novo = 0;
        document.getElementById("taxa_entrega").value = novo;
    }
}

function adicionarTaxa(){
    let atual = document.getElementById("taxa_adicional").value;
    let novo = atual - (- 0.5);
    document.getElementById("taxa_adicional").value = novo;   
}

function subtrairTaxa(){
    let atual = document.getElementById("taxa_adicional").value;
    if(atual > 0){
        let novo = atual - 0.5;
        document.getElementById("taxa_adicional").value = novo;
    }
}

function removerTaxa(){
    let atual = document.getElementById("taxa_adicional").value;
    if(atual > 0){
        let novo = 0;
        document.getElementById("taxa_adicional").value = novo;
    }
}
function adicionarDesconto(){
    let atual = document.getElementById("desconto").value;
    let novo = atual - (- 0.5);
    document.getElementById("desconto").value = novo;   
}

function subtrairDesconto(){
    let atual = document.getElementById("desconto").value;
    if(atual > 0){
        let novo = atual - 0.5;
        document.getElementById("desconto").value = novo;
    }
}

function removerDesconto(){
    let atual = document.getElementById("desconto").value;
    if(atual > 0){
        let novo = 0;
        document.getElementById("desconto").value = novo;
    }
}
