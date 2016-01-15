#coding: utf=8
from const import PROCESSING_CHOICES, CIRCULATION_CHOICES, NONDESTRUCTIVE_INSPECTION_TYPE
from django.db import models
from const.models import Materiel, Material, WorkOrder
from django.contrib.auth.models import User

class Processing(models.Model):
    materiel_belong = models.ForeignKey(Materiel, verbose_name = u"所属物料")
    name = models.CharField(blank = False, choices = PROCESSING_CHOICES, max_length = 10, verbose_name = u"工序名")
    next_processing = models.ForeignKey('self', null = True, blank = True, verbose_name = u"下一工序")
    is_first_processing = models.BooleanField(blank = False, default = False, verbose_name = u"首道工序")
    instruction = models.CharField(blank = True, null = True, max_length = 10, verbose_name = u"说明")
    index = models.CharField(blank = True, null = True, max_length = 10, verbose_name = u"工号")
    hour = models.FloatField(blank = True, null = True, verbose_name = u"工时")

    technical_requirement = models.CharField(blank = True, null = True, max_length = 1000, verbose_name = u"工艺过程及技术要求")
    operator = models.ForeignKey(User, blank = True, null = True, verbose_name = u"操作者", related_name = "operator")
    inspector = models.ForeignKey(User, blank = True, null = True, verbose_name = u"检查者", related_name = "inspector")
    class Meta:
        verbose_name = u"工序"
        verbose_name_plural = u"工序"

    def __unicode__(self):
        return self.materiel_belong.name + "(%s)" % self.get_name_display()

class ProcessReview(models.Model):
    materiel = models.ForeignKey(Materiel, verbose_name = u"零件")
    problem_statement = models.CharField(blank = True, null = True, max_length = 200, verbose_name = u"存在问题")
    advice_statement = models.CharField(blank = True, null = True, max_length = 200, verbose_name = u"改进建议")
    class Meta:
        verbose_name = u"工艺性审查表"
        verbose_name_plural = u"工艺性审查表"
    def __unicode__(self):
        return self.materiel.name

class CirculationName(models.Model):
    name = models.CharField(blank = False, max_length = 10, choices = CIRCULATION_CHOICES, verbose_name = u"流转简称")
    full_name = models.CharField(blank = True, null = True, max_length = 10, verbose_name = u"流转名称全称")
    class Meta:
        verbose_name = u"流转名称"
        verbose_name_plural = u"流转名称"
    def __unicode__(self):
        return self.get_name_display()

class CirculationRoute(models.Model):
    materiel_belong = models.OneToOneField(Materiel, blank = False, verbose_name = u"所属物料")
    L1 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L1", related_name = "L1")
    L2 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L2", related_name = "L2")
    L3 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L3", related_name = "L3")
    L4 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L4", related_name = "L4")
    L5 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L5", related_name = "L5")
    L6 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L6", related_name = "L6")
    L7 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L7", related_name = "L7")
    L8 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L8", related_name = "L8")
    L9 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L9", related_name = "L9")
    L10 = models.ForeignKey(CirculationName, blank = True, null = True, verbose_name = u"L10", related_name = "L10")
    class Meta:
        verbose_name = u"流转路线"
        verbose_name_plural = u"流转路线"
    def __unicode__(self):
        return self.materiel_belong.name

class WeldSeamType(models.Model):
    name = models.CharField(blank = False, max_length = 100, verbose_name = u"类型名")
    class Meta:
        verbose_name = u"焊缝类型"
        verbose_name_plural = u"焊缝类型"
    def __unicode__(self):
        return self.name

class WeldMethod(models.Model):
    name = models.CharField(blank = False, max_length = 100, verbose_name = u"方法名")
    class Meta:
        verbose_name = u"焊接方法"
        verbose_name_plural = u"焊接方法"
    def __unicode__(self):
        return self.name


class NondestructiveInspection(models.Model):
    name = models.CharField(blank = False, choices = NONDESTRUCTIVE_INSPECTION_TYPE, max_length = 20, verbose_name = u"探伤种类名")
    class Meta:
        verbose_name = u"无损探伤"
        verbose_name_plural = u"无损探伤"
    def __unicode__(self):
        return self.name

class WeldSeam(models.Model):
    materiel_belong = models.ForeignKey(Materiel, verbose_name = u"所属物料")
    weld_index = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"焊缝编号")
    weldseam_type = models.ForeignKey(WeldSeamType, verbose_name = u"焊缝类型")
    weld_method = models.ForeignKey(WeldMethod, verbose_name = u"焊接方法")
    base_metal_thin_1 = models.CharField(blank = False, max_length = 100, verbose_name = u"母材厚度1")
    base_metal_thin_2 = models.CharField(blank = False, max_length = 100, verbose_name = u"母材厚度2")
    length = models.CharField(blank = False, max_length = 100, verbose_name = u"长度")
    weld_material_1 = models.ForeignKey(Material, blank = True, null = True, verbose_name = u"焊材1", related_name = "weld_material_1")
    size_1 = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"规格1")
    weight_1 = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"重量1")
    weld_material_2 = models.ForeignKey(Material, blank = True, null = True, verbose_name = u"焊材2", related_name = "weld_material_2")
    size_2 = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"规格2")
    weight_2 = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"重量2")
    remark = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"备注")

    groove_inspction = models.ManyToManyField(NondestructiveInspection, blank = True, null = True, verbose_name = u"坡口探伤", related_name = "groove_inspction")
    welded_status_inspection = models.ManyToManyField(NondestructiveInspection, blank = True, null = True, verbose_name = u"焊态探伤", related_name = "welded_status_inspection")
    heat_treatment_inspection = models.ManyToManyField(NondestructiveInspection, blank = True, null = True, verbose_name = u"热处理后探伤", related_name = "heat_treatment_inspection")
    pressure_test_inspection = models.ManyToManyField(NondestructiveInspection, blank = True, null = True, verbose_name = u"试压后探伤", related_name = "pressure_test_inspection")

    class Meta:
        verbose_name = u"焊缝"
        verbose_name_plural = u"焊缝"
    def __unicode__(self):
        return self.materiel_belong.name   

class WeldListPageMark(models.Model):
    order = models.OneToOneField(WorkOrder, verbose_name = u"所属工作令")
    writer = models.ForeignKey(User, blank = True, null = True, verbose_name = u"编制人", related_name = "writer")
    reviewer = models.ForeignKey(User, blank = True, null = True, verbose_name = u"审核人", related_name = "reviewer")

    class Meta:
        verbose_name = u"焊缝明细签章"
        verbose_name_plural = u"焊缝明细签章"
    def __unicode__(self):
        return self.order.order_index


