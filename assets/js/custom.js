const BasketDeleteLogic = {
    url: `${location.origin}/api/basket-item/delete/`,

    deleteBasketItem(basket_item_id){
        return fetch(`${this.url}`, {
            method : 'POST',
            credentials: 'include',
            headers: {
                'Content-type' : 'application/json',
                'Authorization' : `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'basket_item_id' : basket_item_id
            })
        })
    }
}

const basketItem = document.querySelector('.remove-item');
basketItem.onclick = function(){
    const basket_item_id = parseInt(this.getAttribute('data'));
    BasketDeleteLogic.deleteBasketItem(basket_item_id);
    window.location.reload();
}

