var mid;
var role;
$(document).ready(function(){
    $(document).on("click","#account_search_btn",function(){
        var card_type = $(this).attr("card_type");
        var search_form = $("#account_search_form").serialize();
        Dajaxice.storage.storageAccountSearch(storageaccoutsearch_callback,{"card_type":card_type,"search_form":search_form});
    })
    $(document).on("dblclick","tr[store='true']",function(){
        mid = $(this).attr("id");
        role = $(this).attr("role");
        Dajaxice.storage.storageAccountItemForm(refreshaccountitemform_callback,{"mid":mid,"role":role});
    })
    $(document).on("click","#account_item_save",function(){
        var card_type = $("#account_search_btn").attr("card_type");
        Dajaxice.storage.storageAccountItemModify(storageaccountitemmodify_callback,{"account_item_form":$("#account_item_form").serialize(),"mid":mid,"search_form":$("#account_search_form").serialize(),"card_type":card_type,"role":role});
    })
    $(document).on("click","#account_room_dispatch_btn",function(){
        Dajaxice.storage.storageSteelRoomDispatchList(storageaccoutsearch_callback,{});
    })
})

function storageaccountitemmodify_callback(data){
    $("#account_table").html(data.table_html);
    $("#account_item_form").html(data.form_html);
    update_accout_total_count();
    getSelectItemInfo();
    alert(data.message);
}

function refreshaccountitemform_callback(data){
    $("#account_item_form").html(data.form_html);
    $("div#account_apply_refund_table").html(data.table_html);
    getSelectItemInfo();
    $("#myModal").modal('show');
}

function getSelectItemInfo(){
    var account_thead_html = $("#account_table_thead").html();
    var account_select_item_html = $("tr#"+mid).html();
    $("#show_select_account_item").empty();
    $("#show_select_account_item").append(account_thead_html);
    $("#show_select_account_item").append(account_select_item_html);     
}

function storageaccoutsearch_callback(data){
    $("#account_table").html(data.html); 
    update_accout_total_count();
}
function update_accout_total_count(){
    var account_total_count = $("#account_total_count");
    if(account_total_count != null){
        $(account_total_count).html(cal_account_total_count());
    }
}

function cal_account_total_count(){
    var items = $("tr[name='item_tr']");
    var total_count = 0.0;
    for(var i = 0 ; i < items.length ; i++){
        var a = items.eq(i).children();
        var count = a.eq(a.length-1).text();
        if(!isNaN(count)){
            total_count += parseFloat(count);
        }
    }
    return total_count.toFixed(2);
}
