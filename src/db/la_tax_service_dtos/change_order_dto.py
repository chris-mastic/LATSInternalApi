class ChangeOrderDTO:
    def __init__(self):
        print('in ChangeOrdeDTO __init__')
        self._auth_token = None
        self._tax_year = None
        self._fips_code = None
        self._assessment_no = None
        self._id_com = None
        self._batch_no = None
        self._ltc_nbr_total = None
        self._batch_created = None
        self._status = None
        self._batch_updated = None
        self._batch_submitted = None
        self._batch_approved = None
        self._batch_rejected = None
        self._reject_reason = None
        self._approved_by = None
        self._received_by = None
        self._batch_submitted_by = None
        self._co_detail_id = None
        self._fk_co_master = None
        self._status_cod = None
        self._status_date = None
        self._ltc_comment = None
        self._batch_item_no = None
        self._ward = None
        self._assessment_type = None
        self._taxpayer_name = None
        self._contact_name = None
        self._taxpayer_addr1 = None
        self._taxpayer_addr2 = None
        self._taxpayer_addr3 = None
        self._tc_fee_pd = None
        self._reason = None
        self._chk_no = None
        self._chk_amt = None
        self._prop_desc = None
        self._parcel_add = None
        self._place_fips = None
        self._assessor_ref_no = None
        self._assessment_status = None
        self._homestead_exempt = None
        self._homestead_percent = None
        self._restoration_tax_expmt = None
        self._co_submitted_by = None
        self._id_cav = None
        self._changeordersdetailsid = None
        self._presentdescription = None
        self._presentexempt = None
        self._presenttotalassessed = None
        self._presenthomesteadcredit = None
        self._presenttaxpayershare = None
        self._presentquantity = None
        self._presentunits = None
        self._reviseddescription = None
        self._revisedexempt = None
        self._revisedtotalassessed = None
        self._revisedhomesteadcredit = None
        self._revisedtaxpayershare = None
        self._revisedunits = None
        self._revisedquantity = None

        #self._assess_values = []

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._auth_token = str(value)

    @property
    def tax_year(self):
        return self._tax_year

    # Setter method (setter)
    @tax_year.setter
    def tax_year(self, value):
        # print(f'In tax_year {value}')
        # if value is None:
        #     raise ValueError("Whatever")
        self._tax_year = str(value)

    @property
    def fips_code(self):
        return self._fips_code

    @fips_code.setter
    def fips_code(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._fips_code = str(value)

    @property
    def assessment_no(self):
        return self._assessment_no

    @assessment_no.setter
    def assessment_no(self, value):
        # if value is None:
        #     return ValueError("Invalid altid")
        self._assessment_no = str(value)

    @property
    def ward(self):
        return self._ward

    @ward.setter
    def ward(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._ward = value

    @property
    def assessor_ref_no(self):
        return self._assessor_ref_no

    @assessor_ref_no.setter
    def assessor_ref_no(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._assessor_ref_no = str(value)

    @property
    def place_fips(self):
        return self._place_fips

    @place_fips.setter
    def place_fips(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._place_fips = str(value)

    @property
    def parcel_add(self):
        return self._parcel_add

    @parcel_add.setter
    def parcel_add(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._parcel_add = str(value)

    @property
    def assessment_type(self):
        return self._assessment_type

    @assessment_type.setter
    def assessment_type(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._assessment_type = str(value)

    @property
    def assessment_status(self):
        return self._assessment_status

    @assessment_status.setter
    def assessment_status(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._assessment_status = str(value)

    @property
    def homestead_exempt(self):
        return self._homestead_exempt

    @homestead_exempt.setter
    def homestead_exempt(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._homestead_exempt = str(value)

    @property
    def homestead_percent(self):
        return self._homestead_percent

    @homestead_percent.setter
    def homestead_percent(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._homestead_percent = str(value)

    @property
    def restoration_tax_expmt(self):
        return self._restoration_tax_expmt

    @restoration_tax_expmt.setter
    def restoration_tax_expmt(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._restoration_tax_expmt = str(value)

    @property
    def taxpayer_name(self):
        return self._taxpayer_name

    @taxpayer_name.setter
    def taxpayer_name(self, value):
        # print(f'in taxyper_name {value}')
        # if value is None:
        #     return ValueError("Whatever")
        self._taxpayer_name = str(value)

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._contact_name = str(value)

    @property
    def taxpayer_addr1(self):
        return self._taxpayer_addr1

    @taxpayer_addr1.setter
    def taxpayer_addr1(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._taxpayer_addr1 = str(value)

    @property
    def taxpayer_addr2(self):
        return self._taxpayer_addr2

    @taxpayer_addr2.setter
    def taxpayer_addr2(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._taxpayer_addr2 = str(value)

    @property
    def taxpayer_addr3(self):
        return self._taxpayer_addr3

    @taxpayer_addr3.setter
    def taxpayer_addr3(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._taxpayer_addr3 = str(value)

    @property
    def tc_fee_pd(self):
        return self._tc_fee_pd

    @tc_fee_pd.setter
    def tc_fee_pd(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._tc_fee_pd = str(value)

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._reason = str(value)

    @property
    def chk_no(self):
        return self._chk_no

    @chk_no.setter
    def chk_no(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._chk_no = str(value)

    @property
    def chk_amt(self):
        return self._chk_amt

    @chk_amt.setter
    def chk_amt(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._chk_amt = str(value)

    @property
    def id_com(self):
        return self._id_com

    @id_com.setter
    def id_com(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._id_com = str(value)

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_no = str(value)

    @property
    def ltc_nbr_total(self):
        return self._ltc_nbr_total

    @ltc_nbr_total.setter
    def ltc_nbr_total(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._ltc_nbr_total = str(value)

    @property
    def batch_created(self):
        return self._batch_created

    @batch_created.setter
    def batch_created(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_created = str(value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._status = str(value)

    @property
    def batch_updated(self):
        return self._batch_updated

    @batch_updated.setter
    def batch_updated(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_updated = str(value)

    @property
    def batch_submitted(self):
        return self._batch_submitted

    @batch_submitted.setter
    def batch_submitted(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_submitted = str(value)

    @property
    def batch_approved(self):
        return self._batch_approved

    @batch_approved.setter
    def batch_approved(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_approved = str(value)

    @property
    def batch_rejected(self):
        return self._batch_rejected

    @batch_rejected.setter
    def batch_rejected(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_rejected = str(value)

    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._reject_reason = str(value)

    @property
    def approved_by(self):
        return self._approved_by

    @approved_by.setter
    def approved_by(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._approved_by = str(value)

    @property
    def received_by(self):
        return self._received_by

    @received_by.setter
    def received_by(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._received_by = str(value)

    @property
    def batch_submitted_by(self):
        return self._batch_submitted_by

    @batch_submitted_by.setter
    def batch_submitted_by(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_submitted_by = str(value)

    @property
    def co_detail_id(self):
        return self._co_detail_id

    @co_detail_id.setter
    def co_detail_id(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._co_detail_id = str(value)

    @property
    def fk_co_master(self):
        return self._fk_co_master

    @fk_co_master.setter
    def fk_co_master(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._fk_co_master = str(value)

    @property
    def status_cod(self):
        return self._status_cod

    @status_cod.setter
    def status_cod(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._status_cod = str(value)

    @property
    def status_date(self):
        return self._status_date

    @status_date.setter
    def status_date(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._status_date = str(value)

    @property
    def ltc_comment(self):
        return self._ltc_comment

    @ltc_comment.setter
    def ltc_comment(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._ltc_comment = str(value)

    @property
    def batch_item_no(self):
        return self._batch_item_no

    @batch_item_no.setter
    def batch_item_no(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._batch_item_no = str(value)

    @property
    def prop_desc(self):
        return self._prop_desc

    @prop_desc.setter
    def prop_desc(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._prop_desc = str(value)

    @property
    def co_submitted_by(self):
        return self._co_submitted_by

    @co_submitted_by.setter
    def co_submitted_by(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._co_submitted_by = str(value)

    @property
    def id_cav(self):
        return self._id_cav

    @id_cav.setter
    def id_cav(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._id_cav = str(value)

    @property
    def changeordersdetailsid(self):
        return self._changeordersdetailsid

    @changeordersdetailsid.setter
    def changeordersdetailsid(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._changeordersdetailsid = str(value)

    @property
    def presentdescription(self):
        return self._presentdescription

    @presentdescription.setter
    def presentdescription(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presentdescription = str(value)

    @property
    def presentexempt(self):
        return self._presentexempt

    @presentexempt.setter
    def presentexempt(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presentexempt = str(value)

    @property
    def presenttotalassessed(self):
        return self._presenttotalassessed

    @presenttotalassessed.setter
    def presenttotalassessed(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presenttotalassessed = str(value)

    @property
    def presenthomesteadcredit(self):
        return self._presenthomesteadcredit

    @presenthomesteadcredit.setter
    def presenthomesteadcredit(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presenthomesteadcredit = str(value)

    @property
    def presenttaxpayershare(self):
        return self._presenttaxpayershare

    @presenttaxpayershare.setter
    def presenttaxpayershare(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presenttaxpayershare = str(value)

    @property
    def presentquantity(self):
        return self._presentquantity

    @presentquantity.setter
    def presentquantity(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presentquantity = str(value)

    @property
    def presentunits(self):
        return self._presentunits

    @presentunits.setter
    def presentunits(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._presentunits = str(value)

    @property
    def reviseddescription(self):
        return self._reviseddescription

    @reviseddescription.setter
    def reviseddescription(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._reviseddescription = str(value)

    @property
    def revisedexempt(self):
        return self._revisedexempt

    @revisedexempt.setter
    def revisedexempt(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedexempt = str(value)

    @property
    def revisedtotalassessed(self):
        return self._revisedtotalassessed

    @revisedtotalassessed.setter
    def revisedtotalassessed(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedtotalassessed = str(value)

    @property
    def revisedhomesteadcredit(self):
        return self._revisedhomesteadcredit

    @revisedhomesteadcredit.setter
    def revisedhomesteadcredit(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedhomesteadcredit = str(value)

    @property
    def revisedtaxpayershare(self):
        return self._revisedtaxpayershare

    @revisedtaxpayershare.setter
    def revisedtaxpayershare(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedtaxpayershare = str(value)

    @property
    def revisedunits(self):
        return self._revisedunits

    @revisedunits.setter
    def revisedunits(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedunits = str(value)

    @property
    def revisedquantity(self):
        return self._revisedquantity

    @revisedquantity.setter
    def revisedquantity(self, value):
        # if value < 0:
        #     return ValueError("Whatever")
        self._revisedquantity = str(value)
