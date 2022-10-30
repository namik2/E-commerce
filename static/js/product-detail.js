window.addEventListener('load', async function(){
    let response = await fetch('http://127.0.0.1:8000/api/products/');
    var url = $(location).attr('href').split( '/' );
    var id = url[ url.length - 2 ];
    let items = await response.json();
    let item = items.find(item => item.id == id);


      document.querySelector('#product-detail').innerHTML += `
      <div class="product-name">
        <h1>${item.title}</h1>
      </div>
      <div class="ratings">
        <div class="rating-box">
          <div style="width:60%" class="rating"></div>
        </div>
        <p class="rating-links"> <a href="#">1 Review(s)</a> <span class="separator">|</span> <a href="#">Add Your Review</a> </p>
      </div>
      <div class="price-block">
        <div class="price-box">
          <p class="special-price"> <span class="price-label">Special Price</span> <span id="product-price-48" class="price"> $${item.price} </span> </p>
          <p class="old-price"> <span class="price-label">Regular Price:</span> <span class="price"> $315.99 </span> </p>
        </div>
        <p class="availability in-stock pull-right"><span>In Stock</span></p>
      </div>
      <div class="short-description">
        <h2>Quick Overview</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla. Donec a neque libero. Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem. </p>
      </div>
      <div class="add-to-box">
        <div class="add-to-cart">
          <div class="pull-left">
            <div class="custom pull-left">
              <!-- <button onClick="var result = document.getElementById('qty'); var qty = result.value; if( !isNaN( qty ) &amp &amp  qty &gt; result.value--;return false;" class="reduced items-count" type="button"><i class="fa fa-minus">&nbsp;</i></button> -->
              <input type="text" class="input-text qty" title="Qty" value="1" maxlength="12" id="qty" name="qty">
              <button onClick="var result = document.getElementById('qty'); var qty = result.value; if( !isNaN( qty )) result.value++;return false;" class="increase items-count" type="button"><i class="fa fa-plus">&nbsp;</i></button>
            </div>
          </div>
          <button onClick="productAddToCartForm.submit(this)" class="button btn-cart" title="Add to Cart" type="button"><span>Add to Cart</span></button>
        </div>
        <div class="email-addto-box">
          <p class="email-friend"><a href="#" class=""><span>Email to a Friend</span></a></p>
          <ul class="add-to-links">
            <li> <a class="link-wishlist" href="#"><span>Add to Wishlist</span></a></li>
            <li><span class="separator">|</span> <a class="link-compare" href="#"><span>Add to Compare</span></a></li>
          </ul>
        </div>
      </div>`

    })