window.addEventListener('load', async function(){
    let response = await fetch('http://127.0.0.1:8000/api/products/');
    let items = await response.json();
    console.log('items', items)
    for(let item of items){
        description = item.description
        if(item.description.length > 400){
            description = description.substring(0, 400)
            description += '...'
        }

        document.querySelector('#products-list').innerHTML += `
        <li class="item even">
        <div class="product-image"> <a href="${location.origin}/product_detail/${item.id}" > <img class="small-image" src="${item.field_name}" alt="Microsoft Natural Keyboard"> </a> </div>
        <div class="product-shop">
          <h2 class="product-name"><a href="${location.origin}/product_detail/${item.id}" id="title">${item.title}</a></h2>
          <div class="desc std">
            <p>${description} &nbsp;<a class="link-learn" title="" href="${location.origin}/product_detail/${item.id}">Learn More</a></p>
          </div>
          <div class="price-box"> <span class="regular-price"> <span class="price">$${item.price}</span> </span> </div>
          <div class="actions">
            <button id="add-to-cart" onclick="addToBasket()" class="button btn-cart ajx-cart" title="Add to Cart" type="submit"><span>Add to Cart</span></button>
            <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#"><span>Add to Wishlist</span></a> <a title="Add to Compare" class="button link-compare" href="#"><span>Add to Compare</span></a> </span> </div>
        </div>
      </li>`
      


      
    }
    
    
})

// async function addToBasket(){
//     alert('Added to basket')
//     // let response = await fetch('http://127.0.0.1:8000/api/basketitem/');
//     let formData = {
//         'title': document.querySelector('#title').innerHTML,
//     }
//     console.log('formData', formData)
// }




