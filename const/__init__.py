# coding: UTF-8

BIDFORM_STATUS_CREATE=10
BIDFORM_STATUS_SELECT_SUPPLIER=20
BIDFORM_STATUS_INVITE_BID=30
BIDFORM_STATUS_PROCESS_FOLLOW=40
BIDFORM_STATUS_CHECK_STORE=50
BIDFORM_STATUS_COMPLETE=60
BIDFORM_STATUS_STOP=-1

BIDFORM_PART_STATUS_CREATE=10
BIDFORM_PART_STATUS_ESTABLISHMENT=20
BIDFORM_PART_STATUS_APPROVED=30
BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED=40
BIDFORM_PART_STATUS_INVITE_BID_APPLY=50
BIDFORM_PART_STATUS_INVITE_BID_BRANCECORPOR_AOORIVED=60
BIDFORM_PART_STATUS_INVITE_BID_BINHAICORPOR_AOORIVED=70
BIDFORM_PART_STATUS_INVITE_BID_BIDINVITATION_AOORIVED=80
BIDFORM_PART_STATUS_INVITE_BID_WINBIDNOTICE_AOORIVED=90
BIDFORM_PART_STATUS_PROCESS_FOLLOW=100
BIDFORM_PART_STATUS_CHECK=110
BIDFORM_PART_STATUS_STORE=120
BIDFORM_PART_STATUS_COMPLETE=130
BIDFORM_PART_STATUS_STOP=-1


BIDFORM_STATUS_CHOICES=(

    (BIDFORM_STATUS_CREATE,u"标单生成"),
    (BIDFORM_STATUS_SELECT_SUPPLIER,u"供应商选择"),
    (BIDFORM_STATUS_INVITE_BID,u"招标"),
    (BIDFORM_STATUS_PROCESS_FOLLOW,u"过程跟踪"),
    (BIDFORM_STATUS_CHECK_STORE,u"检查入库"),
    (BIDFORM_STATUS_COMPLETE,u"标单完成"),
    (BIDFORM_STATUS_STOP,u"标单终止")
    
)

BIDFORM_PART_STATUS_CHOICES=(
    
    (BIDFORM_PART_STATUS_CREATE,u"标单创建"),
    (BIDFORM_PART_STATUS_ESTABLISHMENT,u"标单编制"),
    (BIDFORM_PART_STATUS_APPROVED,u"标单审批"),
    (BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED,u"供应商选择"),
    (BIDFORM_PART_STATUS_INVITE_BID_APPLY,u"招标申请"),
    (BIDFORM_PART_STATUS_INVITE_BID_BRANCECORPOR_AOORIVED,u"分公司领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_BINHAICORPOR_AOORIVED,u"滨海公司领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_BIDINVITATION_AOORIVED,u"滨海招标办领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_WINBIDNOTICE_AOORIVED,u"中标通知书"),
    (BIDFORM_PART_STATUS_PROCESS_FOLLOW,u"进程跟踪"),
    (BIDFORM_PART_STATUS_CHECK,u"标单检验"),
    (BIDFORM_PART_STATUS_STORE,u"标单入库"),
    (BIDFORM_PART_STATUS_COMPLETE,u"标单完成"),
    (BIDFORM_PART_STATUS_STOP,u"标单终止")
)

APPROVED_PASS=0
APPROVED_NOT_PASS=1
APPROVED_RESULT_CHOICES=(
    (APPROVED_PASS,u"通过"),
    (APPROVED_NOT_PASS,u"不通过")
)
IDENTITYERROR = "登录帐号或密码有错误！"

ORDERFORN_STATUS_BEGIN = 0
ORDERFORN_STATUS_ESTABLISHMENT = 1
ORDERFORN_STATUS_FINISH = 2

ORDERFORM_STATUS_CHOICES = (
    (ORDERFORN_STATUS_BEGIN, u"创建中订购单"),
    (ORDERFORN_STATUS_ESTABLISHMENT, u"创建完成订购单"),
    (ORDERFORN_STATUS_FINISH, u"已终止历史订购单"),
)

INVENTORY_TYPE = (
    (0, u"主材定额"),
    (1, u"辅料定额"),
    (2, u"先投件明细"),
    (3, u"外购件明细"),
    (4, u"铸锻件明细"),
)

SELL_TYPE = (
    (0, u"内销"),
    (1, u"外销"),
)

IMPLEMENT_CLASS_CHOICES = (
    (0, u"招标"),
    (1, u"议标"),
)

SEX_CHOICES = (
    (0, u"男"),
    (1, u"女"),
)
INDEX_LIST = tuple(
    (i, str(i)) for i in xrange(1, 11)
)

ARRIVAL_CHECK_FIELDS = {"mat":"material_confirm","sof":"soft_confirm","ins":"inspect_confirm"}

REVIEW_COMMENTS_CHOICE_WAIT = -1

REVIEW_COMMENTS_CHOICES = (
    (-1,u"未审核"),
    (0,u"通过"),
    (1,u"不通过"),
)
MAIN_MATERIEL = "main_materiel"
SUPPORT_MATERIEL = "support_materiel"
MATERIEL_CHOICE = (
    (MAIN_MATERIEL, u"主材"),
    (SUPPORT_MATERIEL, u"辅材"),
)

ENTRYTYPE_WELD = 0
ENTRYTYPE_NORMTEILE = 1
ENTRYTYPE_ASSISTTOOL = 2
ENTRYTYPE_FORGING = 4

ENTRYTYPE_CHOICES = (
    (ENTRYTYPE_WELD,u"焊材"),
    (ENTRYTYPE_FORGING,u"锻件"),
    (ENTRYTYPE_NORMTEILE,u"标准件"),
    (ENTRYTYPE_ASSISTTOOL,u"辅助工具"),
)


ENTRYTYPE_BOARD = 0
ENTRYTYPE_BAR = 1

ENTRYTYPE_CHOICES_2 = {
    (ENTRYTYPE_BOARD,u"板材"),
    (ENTRYTYPE_BAR,u"型材"),
}

KILOGRAM = 0
TON = 1

WEIGHT_MANAGEMENT={
    (KILOGRAM,u'千克'),
    (TON,u'顿')
}

SQUARE_METER = 0

AREA_MANAGEMENT={
    (SQUARE_METER,u'平方米')
}









PAGE_ELEMENTS = 10



NEWS_CATEGORY_COMPANYNEWS = "companynews"
NEWS_CATEGORY_IMPORTINFO = "importinfo"
NEWS_CATEGORY_DOCUMENTS = "documents"

NEW_CATEGORY_CHOICES = (
    (NEWS_CATEGORY_COMPANYNEWS, u"公司新闻"),
    (NEWS_CATEGORY_IMPORTINFO, u"重要通知"),
)

NEWS_MAX_LENGTH = 10000000

ENTRYSTATUS_PURCHASER = 0
ENTRYSTATUS_INSPECTOR = 1
ENTRYSTATUS_KEEPER = 2
ENTRYSTATUS_END = 3
ENTRYSTATUS_CHOICES = (
    (ENTRYSTATUS_PURCHASER,u"采购"),
    (ENTRYSTATUS_INSPECTOR,u"检查"),
    (ENTRYSTATUS_KEEPER,u"库管"),
    (ENTRYSTATUS_END,u"结束"),
)



AUTH_TYPE_CHOICES = (
    (0, u"采购管理"),
    (1, u"库存管理"),
    (2, u"生产管理"),
    (3, u"技术资料管理")
)
