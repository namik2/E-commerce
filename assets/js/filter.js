const FilterLogic = {
  url: `${location.origin}/api/product/`,

  filterProduct(categoryId) {
    let url = this.url;
    if (categoryId) {
      url += `?categoryId=${categoryId}`;
    }
    fetch(url).then(res => res.json()).then(data => {
      document.getElementById('products-list').innerHTML = ""
      for (let i in data) {
        // console.log(data[i]['product_size'])
        for (let x in data[i].category) {
          if (data[i]['category'][x] == categoryId) {
            document.getElementById('products-list').innerHTML += `<li class="item first product-list">
                        <div class="product-image"> <a href="{% url 'product_detail' product.pk %}" title="HTC Rhyme Sense">
                            <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense"> </a> </div>
                        <div class="product-shop">
                          <h2 class="product-name"><a href="{% url 'product_detail' product.pk %}"
                              title="HTC Rhyme Sense">${data[i]['title']}</a></h2>
                          <div class="ratings">
                            <div class="rating-box">
                              <div style="width:50%" class="rating"></div>
                            </div>
                            <p class="rating-links"> <a href="#/review/product/list/id/167/category/35/">1 Review(s)</a> <span
                                class="separator">|</span> <a href="#review-form">Add Your Review</a> </p>
                          </div>
                          <div class="desc std">
                            <p>${data[i]['description']}<a class="link-learn" title=""
                                href="{% url 'product_detail' product.pk %}">Learn More</a> </p>
                          </div>
                          <div class="price-box">
        
                            <p class="special-price"> <span class="price-label"></span> <span class="price"> ${data[i]['price']} </span>
                              </span> </p>
                            <p class="old-price"> <span class="price-label"></span> <span class="price"> $442.99 </span> </p>
                          </div>
                          <div class="actions">
        
                            <!-- <button class="add-card" data="${data[i]['id']}">Add To Card</button> -->
        
                            <button id="add-to-basket" data="${data[i]['id']}" class="button btn-cart ajx-cart" title="Add to Cart"
                            type="button"><span>Add to Cart</span></button>
        
                              <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#"
                                  data="${data[i]['id']}"><span data="${data[i]['id']}">Add
                                    to Wishlist</span></a> 
                                    
                                    <!-- <a title="Add to Compare" class="button link-compare"
                                  href="#"><span>Add to Compare</span></a> </span> -->
                          </div>
                        </div>
                      </li>`

          }
        }
        // if (data[i]['color'] == colorId) {
        //   document.getElementById('products-list').innerHTML += `<p>test</p>`

        // }
      }
    });

  }

};

let filterCategory = document.getElementsByClassName('category-field');
for (let i = 0; i < filterCategory.length; i++) {
  filterCategory[i].onclick = function () {
    const categoryId = this.getAttribute('data');
    FilterLogic.filterProduct(categoryId);

  }
}

let filterColor = document.getElementsByClassName('color-field');
for (let i = 0; i < filterColor.length; i++) {
  filterColor[i].onclick = function () {
    const colorId = this.getAttribute('data');
    FilterLogic.filterProduct(colorId);

  }
}


