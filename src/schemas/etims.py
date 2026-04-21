from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class ETIMSItem(BaseModel):
    item_nm: str = Field(..., description="Item Name")
    qty: float = Field(..., gt=0)
    prc: float = Field(..., gt=0)
    tax_ty_cd: str = "A"  # A = 16% VAT


class ETIMSInvoice(BaseModel):
    invc_no: str
    spt_amt: float
    tax_bl_amt: float
    vatt_amt: float
    tot_amt: float
    items: List[ETIMSItem]
    regr_dt: datetime = Field(default_factory=datetime.now)
