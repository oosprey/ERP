#!/usr/bin/env python
# coding=utf-8

from dajax.core import Dajax
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from const.models import WorkOrder,Materiel
from production.models import *
from production.forms import *
from techdata.models import Processing, CirculationRoute
from django.db import connection
from django.db.models import Q,Sum
from storage.utils import get_weld_filter
from const.forms import WorkOrderForm
from production.forms import *
from django.contrib.auth.models import User
from users.models import UserInfo
from const import *

def getQ(con):
    query_set = Q()
    for k,v in con.items():
         if v:
             query_set.add(Q(**{k: v}), Q.AND)
    return query_set

@dajaxice_register
def getFileList(request, id_work_order):
    """
    Lei
    """
    syn_size_file_list_status = SynthesizeFileListStatus.objects.filter(order_id__id = id_work_order)
    syn_size_file_list = []
    for item in syn_size_file_list_status:
        syn_size_file_list.append([(status, getattr(item,status)) for status in SYNSIZE_FILE_LIST_STATUS])
    context = {
        "syn_size_file_list":zip(syn_size_file_list_status, syn_size_file_list),
    }
    html = render_to_string("production/synthesize_detail_filelist.html",context)
    return html

@dajaxice_register
def changeFileList(request, status, workorder_id, is_check):
    """
    Lei
    """
    syn_size_file_status = SynthesizeFileListStatus.objects.get(order = workorder_id)
    setattr(syn_size_file_status,status,is_check)
    syn_size_file_status.save()
    return 

@dajaxice_register
def getHourSearch(request, form):
    """
    Lei
    """
    hour_message_search_form = HourMessageSearchForm(deserialize_form(form))
    if hour_message_search_form.is_valid():
        process_detail_list  = ProcessDetail.objects.filter(getQ(hour_message_search_form.cleaned_data))
    else:
        print hour_message_search_form.errors
    context = {
            "process_detail_list":process_detail_list
        }

    html = render_to_string("production/man_hour_message_list.html",context)
    return html

@dajaxice_register
def getHourSummarize(request, form):
    """
    Lei
    """
    hour_summarize_form = HourSummarizeForm(deserialize_form(form))
    if hour_summarize_form.is_valid():
        select = {'month': connection.ops.date_trunc_sql('month', 'complete_process_date')}
        process_detail_list  = ProcessDetail.objects.exclude(complete_process_date = None).filter(getQ(hour_summarize_form.cleaned_data))\
        .extra(select=select).values('month','materiel_belong__order','materiel_belong__order__order_index', 'productionworkgroup', 'productionworkgroup__name').annotate(Sum('work_hour'))
    else:
        print hour_message_search_form.errors
    context = {
        "process_detail_list":process_detail_list
    }
    html = render_to_string("production/widgets/man_hour_table.html",context)
    return html

@dajaxice_register
def getSummarizeTicket(request, work_order_id, groupNumId, date):
    """
    Lei
    """
    year,month = date.split("-")
    process_detail_list = ProcessDetail.objects.filter(Q(materiel_belong__order=work_order_id)&Q(productionworkgroup=groupNumId)&Q(complete_process_date__year=year)&Q(complete_process_date__month=month)).order_by('complete_process_date')
    work_order = process_detail_list[0].materiel_belong.order.order_index
    group_num = process_detail_list[0].productionworkgroup.name
    context = {
        "work_order":work_order,
        "group_num":group_num,
        "process_detail_list":process_detail_list
    }
    html = render_to_string("production/man_hour_summarize_table.html",context)
    return html

@dajaxice_register
def getPartTicket(request, work_order_id, groupNumId, date):
    """
    Lei
    """
    year,month = date.split("-")
    process_detail_list = list(ProcessDetail.objects.filter(Q(materiel_belong__order=work_order_id)&Q(productionworkgroup=groupNumId)&Q(complete_process_date__year=year)&Q(complete_process_date__month=month)).order_by('materiel_belong'))
    work_order = process_detail_list[0].materiel_belong.order.order_index
    group_num = process_detail_list[0].productionworkgroup.name
    process_detail_list.extend([ProcessDetail()] * ((4-len(process_detail_list))%4))
    context = {
        "work_order":work_order,
        "group_num":group_num,
        "process_detail_list":process_detail_list
    }
    html = render_to_string("production/man_hour_part_ticket.html",context)
    return html


@dajaxice_register
def workorderSearch(request, form):
    """
    kad
    """
    search_form = WorkOrderProductionSearchForm(deserialize_form(form))
    if search_form.is_valid():
        workorder_set  = WorkOrder.objects.filter(getQ(search_form.cleaned_data))
    html = render_to_string("production/widgets/production_plan_select_table.html",{"workorder_set":workorder_set})
    data = {
        "html":html,
    }
    return simplejson.dumps(data)

@dajaxice_register
def workorderAdd(request, checkList):
    """
    kad
    """
    for i in checkList:
        wo_obj = WorkOrder.objects.get(order_index = i)
        obj = ProductionPlan(order = wo_obj)
        obj.save()
    prodplan_set = ProductionPlan.objects.all()
    html = render_to_string("production/widgets/production_plan_table.html", {"prodplan_set":prodplan_set})
    data = {
        "html":html,
    }
    return simplejson.dumps(data)

@dajaxice_register
def prodplanDelete(request, planid):
    """
    kad
    """
    try:
        prodplan_obj = ProductionPlan.objects.get(plan_id = planid)
        prodplan_obj.delete()
        flag = True
    except Exception,e:
        print e
        flag = False
    data = {
        "flag":flag,
    }
    return simplejson.dumps(data)

@dajaxice_register
def getProductPlanForm(request, planid):
    prodPlanForm = ProdPlanForm(instance = ProductionPlan.objects.get(plan_id = planid))
    return simplejson.dumps(prodPlanForm.as_p())
    
@dajaxice_register
def prodplanUpdate(request, form, planid):
    """
    kad
    """
    prodplan_obj = ProductionPlan.objects.get(plan_id = planid)
    prodplan_form = ProdPlanForm(deserialize_form(form), instance=prodplan_obj)
    if prodplan_form.is_valid():
        prodplan_form.save()
        message = u"修改成功"
        flag = True
    else:
        message = u"修改失败"
        flag = False
    prodplan_set = ProductionPlan.objects.all()
    html = render_to_string("production/widgets/production_plan_table.html", {"prodplan_set":prodplan_set})

    data ={
        "html":html,
        "message":message,
        "flag":flag,
    }
    return simplejson.dumps(data)

@dajaxice_register
def prodplanSearch(request, form):
    """
    kad
    """
    search_form = ProductionPlanSearchForm(deserialize_form(form))
    if search_form.is_valid():
        prodplan_set  = ProductionPlan.objects.filter(getQ(search_form.cleaned_data))
        html = render_to_string("production/widgets/production_plan_table.html",{"prodplan_set":prodplan_set})
    else:
        print search_form.errors
    data = {
        "html":html,
    }
    return simplejson.dumps(data)

@dajaxice_register
def taskAllocationSearch(request, form):
    form = TaskAllocationForm(deserialize_form(form))
    items_list1 = {}
    items_list2 = {}
    if form.is_valid():
        conditions = form.cleaned_data
        q1 = (conditions['workorder']!="-1" and Q(materiel_belong__order=conditions['workorder'])) or None
        q2 = (conditions['identifier'] and Q(materiel_belong__index=conditions['identifier'])) or None
        q3 = (conditions['processnumber'] and Q(name=conditions['processnumber'])) or None
        q4 = None
        from django.contrib.auth.models import User
        from users.models import UserInfo
        if conditions['groupnumber']:
            group = UserInfo.objects.get(name = conditions['groupnumber'])
            q4 = (conditions['groupnumber'] and Q(operator = group.user)) or None
        """q4 = (conditions['groupnumber'] and Q(operator__userinfo__name=conditions['groupnumber'])) or None"""
        query_set = filter(lambda x:x!=None,[q1,q2,q3,q4])
        query = q1 or q2 or q3 or q4
        if query == None:
            items_set1 = Processing.objects.filter(operate_date = None).filter(operator = None)
            items_set2 = Processing.objects.filter(operate_date = None).exclude(operator = None)
        else:
            if query_set :
                query_conditions=reduce(lambda x,y:x&y,query_set)
                items_set1 = Processing.objects.filter(operate_date = None).filter(operator = None).filter(query_conditions)
                items_set2 = Processing.objects.filter(operate_date = None).exclude(operator = None).filter(query_conditions)
            else:
                items_set1 = Processing.objects.filter(operate_date = None).filter(operator = None)
                items_set2 = Processing.objects.filter(operate_date = None).exclude(operator = None)
        for item in items_set2:
            if item.operator != None:
                item.operator.info = item.operator.userinfo

        if conditions['task_allocation_status'] == "-1":
            items_list1 = items_set1
            items_list2 = items_set2
        elif conditions['task_allocation_status'] == "0":
            items_list1 = items_set1
        else:
            items_list2 = items_set2
                    
    user_list = UserInfo.objects.all()
    context = {
        "items_list1":items_list1,
        "items_list2":items_list2,
        "user_list":user_list,
        "taskallocationform":form,
    }
    html = render_to_string("production/table/task_allocation_table.html",context)
    return simplejson.dumps({"html":html})

@dajaxice_register
def taskConfirmSearch(request, form):
    form = TaskConfirmForm(deserialize_form(form))
    items_list1 = {}
    items_list2 = {}
    if form.is_valid():
        conditions = form.cleaned_data
        q1 = (conditions['workorder']!="-1" and Q(materiel_belong__order=conditions['workorder'])) or None
        q2 = (conditions['identifier'] and Q(materiel_belong__index=conditions['identifier'])) or None
        q3 = (conditions['processnumber'] and Q(name=conditions['processnumber'])) or None
        q4 = None
        from django.contrib.auth.models import User
        from users.models import UserInfo
        if conditions['groupnumber']:
            group = UserInfo.objects.get(name = conditions['groupnumber'])
            q4 = (conditions['groupnumber'] and Q(operator = group.user)) or None
        query_set = filter(lambda x:x!=None,[q1,q2,q3,q4])
        query = q1 or q2 or q3 or q4
        if query == None:
            items_set1 = Processing.objects.filter(operate_date = None).exclude(operator = None)
            items_set2 = Processing.objects.exclude(operate_date = None)
        else:
            if query_set:
                query_conditions=reduce(lambda x,y:x&y,query_set)
                items_set1 = Processing.objects.filter(query_conditions).filter(operate_date = None).exclude(operator = None)
                items_set2 = Processing.objects.exclude(operate_date = None).filter(query_conditions)
            else:
                items_set1 = Processing.objects.filter(operate_date =  None).exclude(operator = None)
                items_set2 = Processing.objects.exclude(operate_date = None)
        for item in items_set1:
            if item.operator != None:
                item.operator.info = item.operator.userinfo
        for item in items_set2:
            if item.operator != None:
                item.operator.info = item.operator.userinfo
        if conditions['task_confirm_status'] == "-1":
            items_list1 = items_set1
            items_list2 = items_set2
        elif conditions['task_confirm_status'] == "0":
            items_list1 = items_set1
        else:
            items_list2 = items_set2
    
    user_list = UserInfo.objects.all()
    context = {
        "items_list1":items_list1,
        "items_list2":items_list2,
        "user_list":user_list,
        "taskallocationform":form,
    }
    html = render_to_string("production/table/task_confirm_table.html",context)
    return simplejson.dumps({"html":html})

@dajaxice_register
def taskAllocationRemove(request, form, mid):
   item = Processing.objects.get(id = mid)
   item.operator = None
   item.save()
   return taskAllocationSearch(request, form)
   
@dajaxice_register
def taskAllocationSubmit(request, form, mid, groupid):
    item = Processing.objects.get(id = mid)
    from django.contrib.auth.models import User
    user = User.objects.get(id = groupid)
    item.operator = user
    item.save()
    return taskAllocationSearch(request, form)
      
@dajaxice_register
def taskConfirmFinish(request, form, mid):
    item = Processing.objects.get(id = mid)
    import datetime
    item.operate_date = datetime.datetime.today();
    print datetime.datetime.today()
    item.save()
    return taskConfirmSearch(request, form)


@dajaxice_register
def ledgerSearch(request, form):
    search_form = LedgerSearchForm(deserialize_form(form))
    if search_form.is_valid():
        materiel_list  = SubMateriel.objects.filter(getQ(search_form.cleaned_data))
        html = render_to_string("production/widgets/designBOM_table_list.html",{"BOM":materiel_list})
    else:
        print search_form.errors
    return simplejson.dumps({ "html" : html})

@dajaxice_register
def weldPartOrderInfo(request, iid):
    """
    Lei
    """
    materielObj = SubMateriel.objects.get(id = iid)
    materielObj.processDetailObj = list(ProcessDetail.objects.filter(materiel_belong = materielObj))
    materielObj.processDetailObj.extend([ProcessDetail()] * (12-len(materielObj.processDetailObj)))
    html = render_to_string("production/widgets/weld_part_order_info_table.html",{"materielObj":materielObj})
    return simplejson.dumps({ "html" : html})

@dajaxice_register
def getProductionUser(request, form):
    """
    Lei
    """
    production_user_search_form = ProductionUserSearchForm(deserialize_form(form))
    if production_user_search_form.is_valid():
        production_user_list  = ProductionUser.objects.filter(getQ(production_user_search_form.cleaned_data))
    html = render_to_string("production/widgets/production_user_table.html",{"production_user_list":production_user_list})
    return html

@dajaxice_register
def getUser(request, form):
    """
    Lei
    """
    user_choose_form = UserChooseForm(deserialize_form(form))
    if user_choose_form.is_valid():
        user_list = UserInfo.objects.filter(getQ(user_choose_form.cleaned_data)).order_by("productionuser")
    html = render_to_string("production/widgets/user_table.html",{"user_list":user_list})
    return html

@dajaxice_register
def prodUserModify(request, produserid):
    """
    Lei
    """
    productionUserForm = ProductionUserForm(instance = ProductionUser.objects.get(id = produserid))
    return productionUserForm.as_p()

@dajaxice_register
def saveProdUserModify(request, form, produserid):
    prod_user_obj = ProductionUser.objects.get(id = produserid)
    prod_user_form = ProductionUserForm(deserialize_form(form),instance = prod_user_obj)
    if prod_user_form.is_valid():
        prod_user_form.save()
        message = u"修改成功"
    else:
        message = u"修改失败"
    return message

@dajaxice_register
def prodUserDelete(request, uid):
    """
    Lei
    """
    produser_obj = ProductionUser.objects.get(id = uid)
    produser_obj.delete()
    return uid

@dajaxice_register
def addProdUser(request, checkUserList):
    """
    Lei
    """
    for username in checkUserList:
        userInfor_obj = UserInfo.objects.get(user__username = username)
        prod_user_obj = ProductionUser()
        prod_user_obj.production_user_id = userInfor_obj
        prod_user_obj.save()
    return

    # prodplan_set = ProductionPlan.objects.all()
    # html = render_to_string("production/widgets/production_plan_table.html", {"prodplan_set":prodplan_set})
    # data = {
    #     "html":html,
    # }
# def addProductionUser(request, form):
#     """
#     Lei
#     """
#     production_user_search_form = productionUserSearchForm(deserialize_form(form))
#     if production_user_search_form.is_valid():
#         print production_user_search_form.cleaned_data
#         production_user_name = roduction_user_search_form.cleaned_data["production_user_id__username__contains"]
#         users=User.objects.all()
#         productionUser = ProductionUser()
#         productionUser.production_user_id.username = production_user_search_form.cleaned_data["production_user_id__username__contains"]
#         productionUser.production_work_group.name = production_user_search_form.cleaned_data["production_work_group"]
#         productionUser.save()
#         message = u"生产人员添加成功"
#         print "ssssssssssss"
        
#         print "ddddddddddddd"
#     else:
#         message=u"添加失败,生产人员用户名不能为空！"
#     return message
