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
    auth_token = db.Column(db.String(32), nullable=False)
    tax_year = db.Column(db.String(4), nullable=True)
    fips_code = db.Column(db.String(5), nullable=True)
    assessment_no = db.Column(db.String(20), nullable=True)
    id_com = db.Column(db.String(25), nullable=True)
    batch_no = db.Column(db.String(12), nullable=True)
    ltc_nbr_total = db.Column(db.String(20), nullable=True)
    batch_created = db.Column(db.String(22), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    batch_updated = db.Column(db.String(22), nullable=True)          
    batch_submitted = db.Column(db.String(22), nullable=True)       
    batch_approved  = db.Column(db.String(22), nullable=True)         
    batch_rejected = db.Column(db.String(22), nullable=True)        
    reject_reason = db.Column(db.String(22), nullable=True)          
    approved_by = db.Column(db.String(20), nullable=True)            
    received_by = db.Column(db.String(20), nullable=True)            
    batch_submitted_by = db.Column(db.String(20), nullable=True)     
    co_detail_id = db.Column(db.String(25), nullable=True)            
    fk_co_master = db.Column(db.String(15), nullable=True)            
    status_cod  = db.Column(db.String(10), nullable=True)            
    status_date  = db.Column(db.String(22), nullable=True)            
    ltc_comment  = db.Column(db.String(100), nullable=True)            
    batch_item_no = db.Column(db.String(10), nullable=True)           
    ward = db.Column(db.String(4), nullable=True)                   
    assessment_type = db.Column(db.String(2), nullable=True)         
    taxpayer_name  = db.Column(db.String(50), nullable=True)          
    contact_name  = db.Column(db.String(50), nullable=True)           
    taxpayer_addr1 = db.Column(db.String(40), nullable=True)         
    taxpayer_addr2 = db.Column(db.String(40), nullable=True)          
    taxpayer_addr3 = db.Column(db.String(40), nullable=True)         
    tc_fee_pd  = db.Column(db.String(1), nullable=True)              
    reason  = db.Column(db.String(255), nullable=True)                 
    chk_no  = db.Column(db.String(20), nullable=True)                 
    chk_amt = db.Column(db.String(9), nullable=True)                 
    prop_desc = db.Column(db.String(255), nullable=True)               
    parcel_add  = db.Column(db.String(50), nullable=True)             
    place_fips = db.Column(db.String(5), nullable=True)              
    assessor_ref_no = db.Column(db.String(15), nullable=True)         
    assessment_status = db.Column(db.String(2), nullable=True)       
    homestead_exempt = db.Column(db.String(1), nullable=True)        
    homestead_percent = db.Column(db.String(3), nullable=True)       
    restoration_tax_expmt = db.Column(db.String(1), nullable=True)  
    co_submitted_by  = db.Column(db.String(20), nullable=True)        
    id_cav  = db.Column(db.String(25), nullable=True)                 
    changeordersdetailsid  = db.Column(db.String(25), nullable=True)  
    presentdescription = db.Column(db.String(30), nullable=True)   
    presentexempt  = db.Column(db.String(7), nullable=True)         
    presenttotalassessed  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    presenthomesteadcredit = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    presenttaxpayershare  = db.Column(db.Numeric(precision=15, scale=2) ,default=0.0)
    presentquantity  = db.Column(db.String(8), nullable=True)        
    presentunits = db.Column(db.String(255), nullable=True)           
    reviseddescription = db.Column(db.String(50), nullable=True)  
    revisedexempt = db.Column(db.String(7), nullable=True)  
    revisedtotalassessed  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedhomesteadcredit  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedtaxpayershare  = db.Column(db.Numeric(precision=10, scale=2) ,default=0.0)
    revisedunits = db.Column(db.String(1), nullable=True)           
    revisedquantity  = db.Column(db.String(8), nullable=True)





