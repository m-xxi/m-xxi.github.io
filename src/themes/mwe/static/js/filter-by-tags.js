function SelectHashTagFromURLold(){
  var url=window.location.href;

  var found_tag=url.search('/#')
    console.log(url)

  if(found_tag >=0 ){
    let tag_slug = url.substring(found_tag);
      console.log(tag_slug)
    var element = document.getElementById("option-tag-0"); 
          console.log(element)
      // "+tag_slug);
    element.selected = 'selected';

var select = document.getElementById( 'tags-form' );
          console.log(select)
for ( var i = 0, l = select.options.length, o; i < l; i++ )
{
  o = select.options[i];
  if ( o.value === tag_slug )
  {
    o.selected = true;
  }
}
  }

}

function SelectHashTagFromURL(){
  var url=window.location.href;

  var found_tag=url.search('/#')
    console.log(url)

  if(found_tag >=0 ){
    let tag_slug = url.substring(found_tag+2);
    console.log(tag_slug)

    var element = document.getElementById("option-tag-0"); 
          console.log(element)
      // "+tag_slug);
    element.selected = true;

    select = document.getElementById('tags-id');
    console.log(select)
    for ( var i = 0, l = select.options.length, o; i < l; i++ )
    {
      o = select.options[i];
      if ( o.value === tag_slug )
      {
        o.selected = true;
      }
    }
    SelectArticlesFromTags(select);
  }

}
document.addEventListener('DOMContentLoaded', SelectHashTagFromURL(), false);

function SelectArticlesFromTagsOnClick(tag_index){

  var element = document.getElementById("option-tag-"+tag_index.toString());
  element.selected = true;

}

function SelectArticlesFromTags(sel) {
var selected_tags=Array.from(sel.selectedOptions).map(option => "c-tag-"+option.index)

// console.log(selected_tags)

  var x = document.getElementsByClassName('c-article');
  var count=0
  for (i = 0; i < x.length; i++) {
    //recorro todos los artículos
    count=0;
    // console.log(x[i].classList.value())
    for (var j=0; j<selected_tags.length;j++){

      if(x[i].classList.contains(selected_tags[j])){
        count++;
      }
    }
    if(count===selected_tags.length){
      x[i].style.display='block';
    }else{
      x[i].style.display='none';
    }
  }


  SetVisibleTagsFromArticles(sel);

}
function Get_tag_list_from_article(art){
    var index=0;
    var tag_list=Array.from(art.classList)
    let list=art.classList;
    for (let x of list.values()) {
      if  (x.startsWith('c-tag-')) {
        tag_list[index]=x.substring(6) 
        index++;
      }
    }
    // returns a list with the indexes of the tags from the article art
    return tag_list.slice(0,index)
}

function SetVisibleTagsFromArticles(sel) {

var visible_tags=Array.from(sel)
for (var j=0; j<visible_tags.length;j++){
          visible_tags[j]=0;
      }
// tengo que hacer un array de ceros del largo de la cantidad de opciones de sel
// 
  var x = document.getElementsByClassName('c-article');
  var count=0
  for (i = 0; i < x.length; i++) {
    //recorro todos los artículos pero opero solo sobre los visibles
    if(x[i].style.display!='none'){
      var article_tags=Get_tag_list_from_article(x[i])
      // console.log(x[i].classList.value())
      // console.log(article_tags)
      for (var j=0; j<article_tags.length;j++){
          visible_tags[parseInt(article_tags[j])]=1;
      }
    }
  }
// Get each tag by their id and set the display depending on visible_tags
    for (i = 0; i < visible_tags.length; i++) {
        var element = document.getElementById("option-tag-"+i.toString());
        if (visible_tags[i]===1){
            element.style.display = "block";
        }else {
            element.style.display = "none";
        }
    }
}
