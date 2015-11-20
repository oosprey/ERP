#coding=UTF-8
from models import *

from django.contrib import admin

Registers = (
    WeldingMaterialApplyCard,
    StoreRoom,
    WeldingMaterialHumitureRecord,
    WeldingMaterialBakeRecord,
    SteelMaterialPurchasingEntry,
    SteelMaterial,
    BoardSteelMaterialLedger,
    BarSteelMaterialLedger,
    CommonSteelMaterialReturnCardInfo,
    CommonSteelMaterialApplyCardInfo,
    BoardSteelMaterialReturnCardContent,
    BoardSteelMaterialApplyCardContent,
    BarSteelMaterialReturnCardContent,
    BarSteelMaterialApplyCardContent,
    WeldRefund,
    AuxiliaryTool,
    AuxiliaryToolApplyCard,
    AuxiliaryToolEntryCard,
    WeldMaterialEntry,
    WeldMaterialEntryItems,
    WeldStoreList,
    WeldStoreThread,
    OutSideBuyingEntry,
    OutSideBuyingItems,
)

for reg in Registers:
    admin.site.register(reg)
