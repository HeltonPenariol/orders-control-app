var pedidosBalcao = 1;
var pedidosDelivery = 3;
var numeroPedidos = document.getElementById('chartOrders').getContext('2d');

var graficoPedidos = new Chart(numeroPedidos, {
    type: 'doughnut',
    data: {
        labels: ['Balcão', 'Delivery'],
        datasets: [{
            label: 'Número de Pedidos',
            data: [pedidosBalcao, pedidosDelivery],
            backgroundColor: ['#fcb150', '#11a8ab']
        }]
    },
    options: {
        title: {
            display: true,
            fontSize: 22,
            fontColor: '#fff',
            text: 'Número de Pedidos'
        },
        legend: {
            labels: {
                fontColor: '#fff'
            }
        },
    }
})

var totalBalcao = 5;
var totalDelivery = 10;
var comparativoPedidos = document.getElementById('chartComparative').getContext('2d');

var graficoComparativo = new Chart(comparativoPedidos, {
    type: 'doughnut',
    data: {
        labels: ['Balcão', 'Delivery'],
        datasets: [{
            label: 'Gráfico Comparativo',
            data: [totalBalcao, totalDelivery],
            backgroundColor: ['#fcb150', '#11a8ab']
        }]
    },
    options: {
        title: {
            display: true,
            fontSize: 22,
            fontColor: '#fff',
            text: 'Comparativo de Pedidos'
        },
        legend: {
            labels: {
                fontColor: '#fff'
            }
        },
    }
})

var totalDinheiro = 200;
var totalDebito = 300;
var totalCredito = 400;
var fechamentoTotal = document.getElementById('chartIncome').getContext('2d');

var graficoFechamento = new Chart(fechamentoTotal, {
    type: 'doughnut',
    data: {
        labels: ['Dinheiro', 'Débito', 'Crédito'],
        datasets: [{
            label: 'Fechamento Total',
            data: [totalDinheiro, totalDebito, totalCredito],
            backgroundColor: ['#09b858', '#11a8ab', '#fcb150']
        }]
    },
    options: {
        title: {
            display: true,
            fontSize: 22,
            fontColor: '#fff',
            text: 'Comparativo de Pedidos'
        },
        legend: {
            labels: {
                fontColor: '#fff'
            }
        },
    }
})