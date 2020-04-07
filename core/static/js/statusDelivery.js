let pedidoID = document.getElementsByClassName('id_pedido');
let status = document.getElementsByClassName('status');
console.log(status);
console.log(pedidoID);

for (let index = 0; index < status.length; index++) {
    console.log(status[index].innerHTML);
    if (status[index].innerHTML == 'Em preparo'){
        status[index].style.color = 'red';
        pedidoID[index].style.color = 'red';
    }

    else if (status[index].innerHTML == 'Em entrega'){
        status[index].style.color = 'orange';
        pedidoID[index].style.color = 'orange';
    }

    else if (status[index].innerHTML == 'Concluído'){
        status[index].style.color = 'green';
        pedidoID[index].style.color = 'green';
    }
}