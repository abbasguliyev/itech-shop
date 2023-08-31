// $(document).ready(function () {
//     $(".add-to-cart").click(function (e) {
//         // console.log(e.target.parentElement.children[0].outerText)
//         // console.log(sessionStorage.getItem("products"))
//         console.log(sessionStorage.getItem("products"))
//         var prod = e.target.parentElement.children[0].outerText;
//         if(sessionStorage.getItem("products")) {
//             // products = []
//             // products.push(sessionStorage.getItem("products"));
//             products = JSON.parse("[" + sessionStorage.getItem("products") + "]");
//         } else {
//             products = []
//         }
//         products.push(prod)
//         sessionStorage.setItem("products", products);
//         console.log("PRODUCTS =====> ", sessionStorage.getItem("products"))
//     });
// });
