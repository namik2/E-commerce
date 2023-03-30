const WishlistLogic = {
    url: `${location.origin}/api/wishlist/`,

    addProduct(productId) {
        return fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
            })

        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert(data.message);
            } else {
                alert(data.message)
            }
        });
    }
}


    
document.querySelectorAll('.link-wishlist').forEach(link => {
    link.onclick = function (e) {
        
        const productId = this.getAttribute('data');
        WishlistLogic.addProduct(productId);
    }
})


document.querySelectorAll('.link-wishlist1').forEach(link => {
    link.onclick = function (e) {
        
        const productId = this.getAttribute('data');
        WishlistLogic.addProduct(productId);
    }
})


document.querySelector('.add-to-wishlist').onclick = function () {
        const productId = this.getAttribute('data');
        WishlistLogic.addProduct(productId);
    }

