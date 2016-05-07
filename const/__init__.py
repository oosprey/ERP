# coding: UTF-8

BIDFORM_STATUS_CREATE=10
BIDFORM_STATUS_SELECT_SUPPLIER=20
BIDFORM_STATUS_INVITE_BID=30
BIDFORM_STATUS_PROCESS_FOLLOW=40
BIDFORM_STATUS_CHECK_STORE=50
BIDFORM_STATUS_COMPLETE=60
BIDFORM_STATUS_STOP=-1

BIDFORM_PART_STATUS_CREATE=10
#BIDFORM_PART_STATUS_ESTABLISHMENT=20
#BIDFORM_PART_STATUS_APPROVED=30
BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED=40
BIDFORM_PART_STATUS_INVITE_BID_APPLY_SELECT=50
BIDFORM_PART_STATUS_INVITE_BID_FILL=55
BIDFORM_PART_STATUS_INVITE_BID_CARRY=95
BIDFORM_PART_STATUS_INVITE_BID_COMPLETE=97
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
#   (BIDFORM_PART_STATUS_ESTABLISHMENT,u"标单编制"),
#   (BIDFORM_PART_STATUS_APPROVED,u"标单审批"),
    (BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED,u"供应商选择"),
    (BIDFORM_PART_STATUS_INVITE_BID_APPLY_SELECT,u"招标申请选择"),
    (BIDFORM_PART_STATUS_INVITE_BID_FILL,u"招标申请填写"),

    (BIDFORM_PART_STATUS_INVITE_BID_CARRY,u"招标中"),
    (BIDFORM_PART_STATUS_INVITE_BID_COMPLETE,u"中标确认"),
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
ORDERFORN_STATUS_AUDIT = 2
ORDERFORN_STATUS_APPROVED = 3
ORDERFORN_STATUS_FINISH= 4

ORDERFORM_STATUS_CHOICES = (
    (ORDERFORN_STATUS_BEGIN, u"创建中订购单"),
    (ORDERFORN_STATUS_ESTABLISHMENT, u"创建完成订购单"),
    (ORDERFORN_STATUS_AUDIT,u"审核通过订购单"),
    (ORDERFORN_STATUS_APPROVED,u"批准通过订购单"),
    (ORDERFORN_STATUS_FINISH, u"已终止历史订购单"),
)

RECHECK_CHOICE = (
    (True,u"是"),
    (False,u"否"),
)

MAIN_MATERIEL = "main_materiel"
AUXILIARY_MATERIEL = "auxiliary_materiel"
FIRST_FEEDING = "first_feeding"
OUT_PURCHASED = "out_purchased"
WELD_MATERIAL = "weld_material"
COOPERANT = "cooperant"

INVENTORY_TYPE = (
    (MAIN_MATERIEL, u"主材定额"),
    (AUXILIARY_MATERIEL, u"辅料定额"),
    (FIRST_FEEDING, u"先投件明细"),
    (OUT_PURCHASED, u"外购件明细"),
    (WELD_MATERIAL, u"焊材定额"),
    (COOPERANT, u"工序性外协明细")
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

ENTRYTYPE_CHOICES_2 = (
    (ENTRYTYPE_BOARD,u"板材"),
    (ENTRYTYPE_BAR,u"型材"),
)

BOARD_STEEL = 0
BAR_STEEL = 1
STEEL_TYPE = (
    (BOARD_STEEL,u'板材'),
    (BAR_STEEL,u'型材'),
)

WELDING = 0
STEEL = 1
AUXILIARY_TOOL =2
OUTSIDEBUYING =3

MATERIAL_TYPE=(
    (WELDING,u'焊材'),
    (STEEL,u'钢材'),
    (AUXILIARY_TOOL,u'辅助工具'),
    (OUTSIDEBUYING,u'外购件'),
)

KILOGRAM = 0
TON = 1
WEIGHT_MANAGEMENT=(
    (KILOGRAM,u'千克'),
    (TON,u'顿'),
)

SQUARE_METER = 0

AREA_MANAGEMENT=(
    (SQUARE_METER,u'平方米'),
)

METER = 0
CENTIMETER =1

LENGHT_MANAGEMENT=(
    (METER,u'米'),
    (CENTIMETER,u"厘米"),
)









PAGE_ELEMENTS = 10



NEWS_CATEGORY_COMPANYNEWS = "companynews"
NEWS_CATEGORY_IMPORTINFO = "importinfo"
NEWS_CATEGORY_DOCUMENTS = "documents"

NEW_CATEGORY_CHOICES = (
    (NEWS_CATEGORY_COMPANYNEWS, u"公司新闻"),
    (NEWS_CATEGORY_IMPORTINFO, u"重要通知"),
)

NEWS_MAX_LENGTH = 10000000
#-------------库存管理----------------#
STORAGESTATUS_PURCHASER = 0
STORAGESTATUS_INSPECTOR = 1
STORAGESTATUS_KEEPER = 2
STORAGESTATUS_REFUNDER = 3
STORAGESTATUS_AUDITOR = 4
STORAGESTATUS_PROPOSER = 5

STORAGESTATUS_END = -2
ENTRYSTATUS_CHOICES = (
    (STORAGESTATUS_PURCHASER,u"待采购员确认"),
    (STORAGESTATUS_INSPECTOR,u"待检查确认"),
    (STORAGESTATUS_KEEPER,u"待库管确认"),
    (STORAGESTATUS_END,u"结束"),
)
ENTRYSTATUS_LIST = [x[0] for x in ENTRYTYPE_CHOICES]
APPLYCARDSTATUS_CHOICES = (
    (STORAGESTATUS_AUDITOR,u"待审核人确认"),
    (STORAGESTATUS_INSPECTOR,u"待检查确认"),
    (STORAGESTATUS_KEEPER,u"待库管确认"),
    (STORAGESTATUS_END,u"结束"),
)
APPLYCARDSTATUS_LIST = [ x[0] for x in APPLYCARDSTATUS_CHOICES ]
APPLYCARD_APPLICANT=0
APPLYCARD_AUDITOR=1
APPLYCARD_INSPECTOR=2
APPLYCARD_KEEPER=3
APPLYCARD_END = 4
APPLYCARD_STATUS_CHOICES=(
        (APPLYCARD_APPLICANT,u'领用申请'),
        (APPLYCARD_AUDITOR,u'领用审核'),
        (APPLYCARD_INSPECTOR,u'领用检查'),
        (APPLYCARD_KEEPER,u'领用发料'),
        (APPLYCARD_END,u"领用完成"),
        )

AUXILIARY_TOOL_APPLY_CARD_CREATED=0
AUXILIARY_TOOL_APPLY_CARD_APPLYED=1
AUXILIARY_TOOL_APPLY_CARD_COMMITED=2
AUXILIARY_TOOL_APPLY_CARD_END=3
AUXILIARY_TOOL_APPLY_CARD_STATUS=(
        (AUXILIARY_TOOL_APPLY_CARD_CREATED,u'主管'),
        (AUXILIARY_TOOL_APPLY_CARD_APPLYED,u'领料'),
        (AUXILIARY_TOOL_APPLY_CARD_COMMITED,u'发料'),
        (AUXILIARY_TOOL_APPLY_CARD_END,u'完成'),
        )



REFUNDSTATUS_CHOICES = (
    (STORAGESTATUS_REFUNDER,u"退库人"),
    (STORAGESTATUS_KEEPER,u"库管员"),
    (STORAGESTATUS_END,u"结束"),
)

STORAGEDEPARTMENT_CHOICES=( 
    (-1,u'------'),
    (1,u'焊一组'),
    (2,u'焊二组'),
    (3,u'焊三组'),
    (4,u'电焊组'),
)

AUTH_TYPE_CHOICES = (
    (0, u"采购管理"),
    (1, u"库存管理"),
    (2, u"生产管理"),
    (3, u"技术资料管理")
)

AUXILIARY_TOOLS_MODELS_CHOICES=(
        (0,u'碳棒'),
        (1,u'面罩'),
        (2,u'白黑玻璃'),
        (3,u'安全帽'),
    )
STORAGE_ENTRY_TYPE_WELD = 0
STORAGE_ENTRY_TYPE_STEEL = 1

STORAGE_ENTRY_TYPECHOICES=(
    (0,u"焊材"),
    (1,u"钢材"),
)

ITEM_STATUS_NORMAL = 0
ITEM_STATUS_SPENT = 1
ITEM_STATUS_OVERDUE = 2
ITEM_STATUS_SCRAPPED = 3
WELD_ITEM_STATUS_CHOICES = (
    (ITEM_STATUS_NORMAL,u"正常使用"),
    (ITEM_STATUS_SPENT,u"已用完"),
    (ITEM_STATUS_OVERDUE,u"已过期"),
    (ITEM_STATUS_SCRAPPED,u"已报废"),
)

#技术资料管理
H1 = "0"
J = "2"
R = "3"
ZM = "4"
GY = "5"
DY = "6"
XZ = "7"

CIRCULATION_CHOICES = (
    (H1, "H1"),
    (J, "J"),
    (ZM, "ZM"),
    (R, "R"),
    (GY, "GY"),
    (DY, "DY"),
    (XZ, "XZ"),
)

W = "0"
W1 = "1"
W2 = "2"
W3 = "3"
W4 = "4"
W5 = "5"
W6 = "6"
W25 = "7"
P01 = "8"
P02 = "9"
R = "10"
R1 = "11"
R2 = "12"
Z = "13"
H = "14"
M = "15"
L = "16"
Y = "17"
G = "18"
G1 = "19"
G2 = "20"
X = "21"
J = "22"
DY = "23"
PROCESSING_CHOICES = (
    (W, "W"),    
    (W1, "W1"),
    (W2, "W2"),
    (W3, "W3"),
    (W4, "W4"),
    (W5, "W5"),
    (W6, "W6"),
    (W25, "W25"),
    (P01, "P01"),
    (P02, "P02"),
    (R, "R"),
    (R1, "R1"),
    (R2, "R2"),
    (Z, "Z"),
    (H, "H"),
    (M, "M"),
    (L, "L"),
    (Y, "Y"),
    (G, "G"),
    (G1, "G1"),
    (G2, "G2"),
    (X, "X"),
    (J, "J"),
    (DY, "DY"),
)


WELD_ROD = "weld_rod"
WELD_WIRE = "weld_wire"
WELD_RIBBON = "weld_ribbon"
WELD_FLUX = "weld_flux"
WELD = "weld"
SHEET = "sheet"
PROFILE = "profile"
PURCHASED = "purchased"
OTHER = "other"
AUXILIARY_TOOL = "auxiliary_tool"
MATERIAL_CATEGORY_CHOICES = (
    (WELD_ROD, u"焊条"),
    (WELD_WIRE, u"焊丝"),
    (WELD_RIBBON, u"焊带"),
    (WELD_FLUX, u"焊剂"),
    (SHEET, u"板材"),
    (PROFILE, u"型材"),
    (PURCHASED, u"外购件"),
    (AUXILIARY_TOOL,u"辅助工具"),
    (OTHER, u"其他"),
)

WELD_TYPE_LIST = [WELD_ROD,WELD_WIRE,WELD_RIBBON,WELD_FLUX]
PURCHASED_TYPE_LIST = [PURCHASED,]
SHEET_TYPE_LIST = [SHEET,]
PROFILE_TYPE_LIST = [PROFILE,]
AUXILIARY_TOOL_TYPE_LIST = [AUXILIARY_TOOL,]
MATERIEL_TYPE_CHOICES = (
    (WELD, u"焊材"),
    (SHEET, u"板材"),
    (PROFILE, u"型材"),
    (PURCHASED, u"外购件"),
    (AUXILIARY_TOOL, u"辅助工具"),
) 

RT = "RT"
UT = "UT"
MT = "MT"
PT = "PT"
VT = "VT"

NONDESTRUCTIVE_INSPECTION_TYPE = (
    (RT, "RT"),
    (UT, "UT"),
    (MT, "MT"),
    (PT, "PT"),
    (VT, "VT"),
)

CYLIDER_TRANSFER_CARD = "cylider_transfer_card"
CAP_TRANSFER_CARD = "cap_transfer_card"

TRANSFER_CARD_TYPE_CHOICES = (
    (CYLIDER_TRANSFER_CARD, u"筒体流转卡"),  
    (CAP_TRANSFER_CARD, u"封头流转卡"),
)


CARD_TYPE_TO_HTML = {
    CYLIDER_TRANSFER_CARD: "techdata/widgets/cylider_transfer_card.html",
    CAP_TRANSFER_CARD: "techdata/widgets/cap_transfer_card.html",
}

MARK_WRITE = "mark_write"
MARK_REVIEW = "mark_review"
MARK_PROOFREAD = "mark_proofread"
MARK_APPROVE = "mark_approve"
MARK_QUOTA = "mark_quota"
MARK_STATISTIC = "mark_statistic"

HEATTREATMENTCARD_ATTR_TEM_START = "temperature_start"
HEATTREATMENTCARD_ATTR_TEM_END = "temperature_end"
HEATTREATMENTCARD_ATTR_TEM_TOP = "temperature_top"
HEATTREATMENTCARD_ATTR_TEM_UP_SPEED = "temperature_up_speed"
HEATTREATMENTCARD_ATTR_TEM_DOWN_SPEED = "temperature_down_speed"
HEATTREATMENTCARD_ATTR_TEM_TIME = "time"

FLUSH_WELD = "FLUSH_WELD"
HORIZONTAL_WELD = "HORIZONTAL_WELD"
OVERHEAD_WELD = "OVERHEAD_WELD"
VERTICAL_WELD = "VERTICAL_WELD"
WIDE_WELD = "WIDE_WELD"

WELD_POSITION_CHOICES = (
    (FLUSH_WELD, u"平焊"),
    (HORIZONTAL_WELD, u"横焊"),
    (OVERHEAD_WELD, u"仰焊"),
    (VERTICAL_WELD, u"立向上焊"),
    (WIDE_WELD, u"全位置焊")
)

#生产管理
PRODUCTION_PLAN_STAUTS_CHOICES = (
    ("",u"---------"),
    (1, u"必保"),
    (2, u"在制"),
)

#焊缝焊接接头  焊工持证项目
SMAW_Fell = "SMAW-Fell-5FG-12/60-Fef3J"
GMAW_Fell = "GMAW-Fell-3G-14-FefS-11/15"
SAW_1G_07 = "SAW-1G07/09/19"
WELD_CERTIFICATION = (
    (SMAW_Fell, "SMAW-Fell-5FG-12/60-Fef3J"),
    (GMAW_Fell, "GMAW-Fell-3G-14-FefS-11/15"),
    (SAW_1G_07, "SAW-1G-07/09/19"),
)
#焊接工艺评定编号
RH24_13_09 = "RH24-13-09"
RH24_13_36 = "RH24-13-36"
PROCEDURE_QUALIFICATION_INDEX = (
    (RH24_13_09, "RH24-13-09"),
    (RH24_13_36, "RH24-13-36"),
)


#标单评论人属性
Z_APPLY_OPERATOR=1
Z_APPLY_LEAD=2
Z_NEED=3
Z_CENTRALIZE=4
Z_LOGISTICAL=5
Z_COMPANY=6
G_OPERATOR=7
G_LEAD=8
G_QUALITY=9
G_ECONOMIC=10
G_COMPREHENSIVE=11
Q_OPERATOR=12
Q_NEED_TECH=13
Q_NEED_LEAD=14
Q_COMPREHENSIVE=15
Q_COMPANY=16
COMMENT_USER_CHOICE=(
	(Z_APPLY_OPERATOR,u"申请表经办人"),
	(Z_APPLY_LEAD,u"申请表申请主管"),
	(Z_NEED,u"申请表需求单位"),
	(Z_CENTRALIZE,u"申请表归口部门"),
	(Z_LOGISTICAL,u"申请表物流采控"),
	(Z_COMPANY,u"申请表公司意见"),
	(G_OPERATOR,u"审核表经办人"),
	(G_LEAD,u"审核表主管领导"),
	(G_QUALITY,u"审核表质量部"),
	(G_ECONOMIC,u"审核表经济运行部"),
	(G_COMPREHENSIVE,u"审核表综合管理部"),
	(Q_OPERATOR,u"比质卡经办人"),
	(Q_NEED_TECH,u"比质卡需求技术"),
	(Q_NEED_LEAD,u"比质卡需求领导"),
	(Q_COMPREHENSIVE,u"比质卡综合管理"),
	(Q_COMPANY,u"比质卡公司")
)




BIDFORM_PART_STATUS_INVITE_BID_APPLY_FILL=10
BIDFORM_PART_STATUS_INVITE_BID_APPLY_OPERATOR_COMMENT=20
BIDFORM_PART_STATUS_INVITE_BID_APPLY_LEAD_COMMENT=30
BIDFORM_PART_STATUS_INVITE_BID_APPLY_NEED_COMMENT=40
BIDFORM_PART_STATUS_INVITE_BID_APPLY_CENTRALIZE_COMMENT=50
BIDFORM_PART_STATUS_INVITE_BID_APPLY_LOGISTICAL_COMMENT=60
BIDFORM_PART_STATUS_INVITE_BID_APPLY_COMPANY_COMMENT=70

BIDFORM_PART_STATUS_INVITE_BID_CHECK_FILL=80
BIDFORM_PART_STATUS_INVITE_BID_CHECK_OPERATOR_COMMENT=90
BIDFORM_PART_STATUS_INVITE_BID_CHECK_LEAD_COMMENT=100
BIDFORM_PART_STATUS_INVITE_BID_CHECK_QUALITY_COMMENT=110
BIDFORM_PART_STATUS_INVITE_BID_CHECK_ECONOMIC_COMMENT=120
BIDFORM_PART_STATUS_INVITE_BID_CHECK_COMPREHENSIVE_COMMENT=130

BIDFORM_PART_STATUS_INVITE_BID_QUALITY_FILL=140
BIDFORM_PART_STATUS_INVITE_BID_QUALITY_OPERATOR_COMMENT=150
BIDFORM_PART_STATUS_INVITE_BID_QUALITY_NEED_TECH_COMMENT=160
BIDFORM_PART_STATUS_INVITE_BID_QUALITY_NEED_LEAD_COMMENT=170
BIDFORM_PART_STATUS_INVITE_BID_QUALITY_COMPREHENSIVE_COMMENT=180
BIDFORM_PART_STATUS_INVITE_BID_QUALITY_COMPANY_COMMENT=190




COMMENT_STATUS_CHOICES=(
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_FILL,u"申请表填写"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_OPERATOR_COMMENT,u"申请经办人意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_LEAD_COMMENT,u"申请表申请领导意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_NEED_COMMENT,u"申请表需求部门意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_CENTRALIZE_COMMENT,u"申请表归口部门意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_LOGISTICAL_COMMENT,u"申请表物流采控部门意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_APPLY_COMPANY_COMMENT,u"申请表公司意见"),

	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_FILL,u"审核表填写"),
	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_OPERATOR_COMMENT,u"审核表经办人意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_LEAD_COMMENT,u"审核表主管领导意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_QUALITY_COMMENT,u"审核表质量部意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_ECONOMIC_COMMENT,u"审核表经济运行部意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_CHECK_COMPREHENSIVE_COMMENT,u"审核表综合管理部意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_FILL,u"比质卡填写"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_OPERATOR_COMMENT,u"比质卡经办人意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_NEED_TECH_COMMENT,u"比质卡需求技术意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_NEED_LEAD_COMMENT,u"比质卡需求领导意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_COMPREHENSIVE_COMMENT,u"比质卡综合管理意见"),
	(BIDFORM_PART_STATUS_INVITE_BID_QUALITY_COMPANY_COMMENT,u"比质卡公司意见")
)

