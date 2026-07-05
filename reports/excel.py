"""Excel Report Generator Simplified V3.0"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Border,Side
from openpyxl.utils import get_column_letter
class ExcelReport:
    def __init__(self,symbol,technical,support,volume,smart_money,divergence,pattern,final_score,df):
        self.symbol=symbol; self.technical=technical; self.support=support or {}
        self.volume=volume or {}; self.smart_money=smart_money or {}
        self.divergence=divergence or {}; self.pattern=pattern or {}
        self.final_score=final_score or {}; self.df=df; self.wb=Workbook()
        thin=Side(style="thin"); self.border=Border(left=thin,right=thin,top=thin,bottom=thin)
        self.hfill=PatternFill("solid",fgColor="D9EAD3"); self.tfill=PatternFill("solid",fgColor="1F4E78")
        self.hfont=Font(bold=True); self.tfont=Font(bold=True,color="FFFFFF",size=13)
    def _title(self,ws,t):
        ws.merge_cells("A1:B1"); c=ws["A1"]; c.value=t; c.fill=self.tfill; c.font=self.tfont
    def _row(self,ws,r,k,v):
        ws.cell(r,1).value=k; ws.cell(r,2).value=v
    def _width(self,ws):
        for idx,col in enumerate(ws.columns,1):
            m=0
            for cell in col:
                if cell.__class__.__name__=="MergedCell": continue
                if cell.value is not None: m=max(m,len(str(cell.value)))
            ws.column_dimensions[get_column_letter(idx)].width=m+4
    def summary_sheet(self):
        ws=self.wb.active; ws.title="Summary"; self._title(ws,"Iran Analyzer")
        r=3
        for k,v in [("Symbol",self.symbol),("Last Close",self.technical.get("last_close")),("Trend",self.technical.get("trend")),("Final Score",self.final_score.get("final_score")),("Signal",self.final_score.get("signal"))]:
            self._row(ws,r,k,v); r+=1
        self._width(ws)
    def technical_sheet(self):
        ws=self.wb.create_sheet("Technical"); self._title(ws,"Technical"); r=3
        d={}; d.update(self.technical); d.update(self.support); d.update(self.volume); d.update(self.smart_money); d.update(self.divergence); d.update(self.pattern)
        for k,v in d.items(): self._row(ws,r,k,v); r+=1
        self._width(ws)
    def raw_data_sheet(self):
        ws=self.wb.create_sheet("RawData")
        for c,h in enumerate(self.df.columns,1): ws.cell(1,c).value=h
        for r,row in enumerate(self.df.itertuples(index=False),2):
            for c,v in enumerate(row,1): ws.cell(r,c).value=v
        self._width(ws)
    def save(self):
        os.makedirs("output",exist_ok=True); p=f"output/{self.symbol}_analysis.xlsx"; self.wb.save(p); print(p)
    def export(self):
        self.summary_sheet(); self.technical_sheet(); self.raw_data_sheet(); self.save()
