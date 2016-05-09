$("#id_bid_date").datetimepicker({
    format:'yyyy-mm-dd',
    weekStart:1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight:1,
    startView:2,
    forceParse:0,
    minView:2
});
$("#id_bid_delivery_date").datetimepicker({
    format:'yyyy-mm-dd',
    weekStart:1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight:1,
    startView:2,
    forceParse:0,
    minView:2
});
$("#id_bid_datetime").datetimepicker({
    format:'yyyy-mm-dd',
    weekStart:1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight:1,
    startView:2,
    forceParse:0,
    minView:2
});
$("#apply_confirm").click(function(){
      var form = $(this).parents("form");
      var bidapplyform = form;
      var bid_apply_id=$("#bid_apply_div").attr("bidapplyid");
      Dajaxice.purchasing.saveBidApply(function(data){
    window.location.reload();
      },{'form':$(form).serialize(true),'bid_apply_id':bid_apply_id});

});

$("#apply_submit").click(function(){
      var bid_apply_id=$("#bid_apply_div").attr("bidapplyid");
      Dajaxice.purchasing.submitBidApply(function(data){
    window.location.reload();
      },{bid_apply_id:bid_apply_id});

});

$("#apply_comment_confirm").click(function(){
    var bid_apply_id=$("#bid_apply_div").attr("bidapplyid");
    var usertitle=$("#comment_add").attr("usertitle");
    alert(usertitle);
    Dajaxice.purchasing.BidApplyComment(function(data){
        window.location.reload();
    },{
        "bid_apply_id":bid_apply_id,
        "usertitle":usertitle,
        "comment":$("#comment_area").val()
    });
});
$("#apply_logistical_confirm").click(function(){
    alert($("#comment_add").attr("usertitle"));
    Dajaxice.purchasing.BidApplyLogistical(function(data){
        alert(data.status);
    if(data.status==0)window.location.reload();
    else alert("表单填写有误！");
    },{
    "form":$("#logistical_form").serialize(true),
    "bid_apply_id":$("#bid_apply_div").attr("bidapplyid"),
    "usertitle":$("#comment_add").attr("usertitle") 
});
});