from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
from sqlalchemy import event
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



class NOALTCChangeOrder(Base):
    __tablename__ = "noa_ltc_change_order"

    id = db.Column(db.Integer(), primary_key=True)
    tax_year = db.Column(db.String(4), nullable=False)
    fips_code = db.Column(db.String(5), nullable=False)
    assessment_no = db.Column(db.String(20), nullable=False)
    id_com = db.Column(db.String(25), nullable=False)
    batch_no = db.Column(db.String(12), nullable=False)
    ltc_nbr_total = db.Column(db.String(20), nullable=False)
    batch_created = db.Column(db.String(22), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    batch_updated = db.Column(db.String(22), nullable=False)          
    batch_submitted = db.Column(db.String(22), nullable=False)       
    batch_approved  = db.Column(db.String(22), nullable=False)         
    batch_rejected = db.Column(db.String(22), nullable=False)        
    reject_reason = db.Column(db.String(22), nullable=False)          
    approved_by = db.Column(db.String(20), nullable=False)            
    received_by = db.Column(db.String(20), nullable=False)            
    batch_submitted_by = db.Column(db.String(20), nullable=False)     
    co_detail_id = db.Column(db.String(25), nullable=False)            
    fk_co_master = db.Column(db.String(15), nullable=False)            
    status_cod  = db.Column(db.String(10), nullable=False)            
    status_date  = db.Column(db.String(22), nullable=False)            
    ltc_comment  = db.Column(db.String(100), nullable=False)            
    batch_item_no = db.Column(db.String(10), nullable=False)           
    ward = db.Column(db.String(4), nullable=False)                   
    assessment_type = db.Column(db.String(2), nullable=False)         
    taxpayer_name  = db.Column(db.String(50), nullable=False)          
    contact_name  = db.Column(db.String(50), nullable=False)           
    taxpayer_addr1 = db.Column(db.String(40), nullable=False)         
    taxpayer_addr2 = db.Column(db.String(40), nullable=False)          
    taxpayer_addr3 = db.Column(db.String(40), nullable=False)         
    tc_fee_pd  = db.Column(db.String(1), nullable=False)              
    reason  = db.Column(db.String(255), nullable=False)                 
    chk_no  = db.Column(db.String(20), nullable=False)                 
    chk_amt = db.Column(db.String(9), nullable=False)                 
    prop_desc = db.Column(db.String(255), nullable=False)               
    parcel_add  = db.Column(db.String(50), nullable=False)             
    place_fips = db.Column(db.String(5), nullable=False)              
    assessor_ref_no = db.Column(db.String(15), nullable=False)         
    assessment_status = db.Column(db.String(2), nullable=False)       
    homestead_exempt = db.Column(db.String(1), nullable=False)        
    homestead_percent = db.Column(db.String(3), nullable=False)       
    restoration_tax_expmt = db.Column(db.String(1), nullable=False)  
    co_submitted_by  = db.Column(db.String(20), nullable=False)        
    id_cav  = db.Column(db.String(25), nullable=False)                 
    changeordersdetailsid  = db.Column(db.String(25), nullable=False)  
    presentdescription = db.Column(db.String(30), nullable=False)   
    presentexempt  = db.Column(db.String(7), nullable=False)         
    presenttotalassessed  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    presenthomesteadcredit = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    presenttaxpayershare  = db.Column(db.Numeric(precision=15, scale=2) ,default=0.0)
    presentquantity  = db.Column(db.String(8), nullable=False)        
    presentunits = db.Column(db.String(255), nullable=False)           
    reviseddescription = db.Column(db.String(50), nullable=False)  
    revisedexempt = db.Column(db.String(7), nullable=False)  
    revisedtotalassessed  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedhomesteadcredit  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedtaxpayershare  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedunits = db.Column(db.String(1), nullable=False)           
    revisedquantity  = db.Column(db.String(8), nullable=False)





