function entry_confirm(eid){
    
}

var mid;
function change_item(itemid){
    mid = itemid;
    var a = $("tr#"+mid).find("td");
    $("input#id_remark").val(a.eq(9).text());
    $("input#id_date").val(a.eq(10).text());
    $("input#id_price").val(a.eq(11).text());

}

function save_item(){
    Dajaxice.storage.entryItemSave(save_item_callback,{"form":$("#entry_item_form").serialize(),"mid":mid});
}

function save_item_callback(data){
    if(data.flag){
        $("div#items_table").html(data.html);
        alert(data.message);
    }
    else{
        alert(data.message);
    }
    
}

function entryconfirm(eid){
    var entry_code = $("#input_entry_code").val();
    Dajaxice.storage.entryConfirm(entry_confirm_callback,{"eid":eid,"entry_code":entry_code}); 
}

function entry_confirm_callback(data){
    if(data.flag){
        alert("入库单确认成功");
    }
    else{
        alert("入库单确认失败");
    }
}
