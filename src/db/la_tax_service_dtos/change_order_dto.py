class ChangeOrderDTO:
    def __init__(self):
        print('in ChangeOrdeDTO __init__')
        self._tax_year = None
        self._fips_code = None
        self._assessment_no = None
        self._ward = None
        self._assessor_ref_no = None
        self._place_fips = None
        self._parcel_address = None
        self._assessment_type = None
        self._assessment_status = None
        self._homestead_exempt = None
        self._homestead_percent = None
        self._restoration_tax_exempt = None
        self._taxpayer_name = None
        self._contact_name = None
        self._taxpayer_addr1 = None
        self._taxpayer_addr2 = None
        self._taxpayer_addr3 = None
        self._tc_fee_pd = None
        self._reason = None
        self._check_no = None
        self._check_amount = None
        self._assess_values = []
        # ... other attributes ...


    @property
    def tax_year(self):
        return self._tax_year

    # Setter method (setter)
    @tax_year.setter
    def tax_year(self,value):
        print(f'In tax_year {value}')
        if value is None:
            raise ValueError("Whatever")
        self._tax_year = value

    @property
    def fips_code(self):
        return self._fips_code
        
    @fips_code.setter
    def fips_code(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._fips_code = value

    @property
    def assessment_no(self):
        return self._assessment_no
        
    @assessment_no.setter
    def assessment_no(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._assessment_no = value

    @property
    def ward(self):
        return self._ward
        
    @ward.setter
    def ward(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._ward = value

    @property
    def assessor_ref_no(self):
        return self._assessor_ref_no
        
    @assessor_ref_no.setter
    def assessor_ref_no(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._assessor_ref_no = value

    @property
    def place_fips(self):
        return self._place_fips
        
    @place_fips.setter
    def place_fips(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._place_fips = value

    @property
    def parcel_address(self):
        return self._parcel_address
        
    @parcel_address.setter
    def parcel_address(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._parcel_address = value

    @property
    def assessment_type(self):
        return self._assessment_type
        
    @assessment_type.setter
    def assessment_type(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._assessment_type = value

    @property
    def assessment_status(self):
        return self._assessment_status
        
    @assessment_status.setter
    def assessment_status(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._assessment_status = value

    @property
    def homestead_exempt(self):
        return self._homestead_exempt
        
    @homestead_exempt.setter
    def homestead_exempt(self,value):
        if value < 0:
            return ValueError("Whatever")
        self._homestead_exempt = value

    @property
    def homestead_percent(self):
        return self._homestead_percent
        
    @homestead_percent.setter
    def homestead_percent(self, value):
        if value < 0:
            return ValueError("Whatever")
        return self._homestead_percent

    @property
    def restoration_tax_exempt(self):
        return self._restoration_tax_exempt
        
    @restoration_tax_exempt.setter
    def restoration_tax_exempt(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._restoration_tax_exempt = value

    @property
    def taxpayer_name(self):
        return self._taxpayer_name
        
    @taxpayer_name.setter
    def taxpayer_name(self, value):
        print(f'in taxyper_name {value}')
        if value is None:
            return ValueError("Whatever")
        self._taxpayer_name = value

    @property
    def contact_name(self):
        return self._contact_name
        
    @contact_name.setter
    def contact_name(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._contact_name = value

    @property
    def taxpayer_addr1(self):
        return self._taxpayer_addr1
        
    @taxpayer_addr1.setter
    def taxpayer_addr1(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._taxpayer_addr1 = value

    @property
    def taxpayer_addr2(self):
        return self._taxpayer_addr2
        
    @taxpayer_addr2.setter
    def taxpayer_addr2(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._taxpayer_addr2 = value

    @property
    def taxpayer_addr3(self):
        return self._taxpayer_addr3
        
    @taxpayer_addr3.setter
    def taxpayer_addr3(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._taxpayer_addr3= value

    @property
    def tc_fee_pd(self):
        return self._tc_fee_pd
        
    @tc_fee_pd.setter
    def tc_fee_pd(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._tc_fee_pd = value

    @property
    def reason(self):
        return self._reason
        
    @reason.setter
    def reason(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._reason = value

    @property
    def check_no(self):
        return self._check_no
        
    @check_no.setter
    def check_no(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._check_no= value

    @property
    def check_amount(self):
        return self._check_amount
        
    @check_amount.setter
    def check_amount(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._check_amount = value

    @property
    def assess_values(self):
        return self._assess_values
        
    @assess_values.setter
    def assess_values(self, value):
        if value < 0:
            return ValueError("Whatever")
        self._assess_values = value

       

