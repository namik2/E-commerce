const BasketLogic = {
    url: `${location.origin}/api/basket/`,

    addProduct(productId, quantity) {
        return fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
                'quantity': quantity,
            })
        }).then(response => response.json()).then(data => {
            console.log(data);
            
            if (data.success) {
                alert(data.message);
            }
            document.getElementById('cart-sidebar').innerHTML = "";
            document.querySelector('.top-cart-content').style.display = "block";
            for (let i in data) {
                document.getElementById('cart-sidebar').innerHTML += `<li class="item first" id="item-first">
                <div class="item-inner"><a class="product-image"
                        title="a"
                        href="#l"><img
                            alt=""
                            src="${data[i]['product']['cover_image']}"></a>
                    <div class="product-details">
                        <div class="access"><a class="btn-remove1"
                                title="Remove This Item" href="#">Remove</a> <a
                                class="btn-edit" title="Edit item" href="#"><i
                                    class="icon-pencil"></i><span
                                    class="hidden">Edit item</span></a> </div>
                        <!--access--> <strong>${data[i]['quantity']}</strong> x <span
                            class="price">${data[i]['product']['price']}</span>
                        <p class="product-name"><a href="#">${data[i]['product']['title']}</a></p>
                    </div>
                </div>
            </li>`;
            }
        });
    },
}

const addToBasket = document.getElementById('add-to-basket');
addToBasket.onclick = function () {
    
    const productId = this.getAttribute('data');
    const quantity = parseInt(document.getElementById('qty').value)
    BasketLogic.addProduct(productId, quantity);

}



let addToCard = document.getElementsByClassName('btn-cart');
for (let i = 0; i < addToCard.length; i++) {
    addToCard[i].onclick = function () {
        const productId = this.getAttribute('data');
        const quantity = 1;
        BasketLogic.addProduct(productId, quantity);

    }
}


let addFromWishlist = document.getElementsByClassName('add-from-wishlist');
for (let i = 0; i < addFromWishlist.length; i++) {
    addFromWishlist[i].onclick = function () {
        const productId = this.getAttribute('data');
        const quantity = 1;
        BasketLogic.addProduct(productId, quantity);

    }
}