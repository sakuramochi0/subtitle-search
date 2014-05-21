$(function(){
    $(document).ready(function(){
	$('table.sieve').sieve();
    });
  //   $('#search-text').keyup(function(){
  //   var line = 1;
  //   if (!$(this).val()) {
  //       // 検索文字列無し
  //       $('table tr').show();
  //   } else {
  //       // 検索文字列有り
  //       $('table tr').hide();
  //       $('table tr th').parent().show(); // header
  // 	var hit = $('table tr:contains(' + this.value + ')');
  // 	hit.css('background-color', 'pink');
  // 	hit.show();
  // 	hit = hit.prevAll().eq(1);
  // 	hit.show();
  // 	hit.css('background-color', '#yellow');
  // 	for (var i; i<line*2+1; i++) {
  // 	    hit.show();
  // 	    hit = hit.next();
  // 	}
  //   }
  // });
});
