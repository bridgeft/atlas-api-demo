# coding: utf-8

"""
    Atlas API

    RESTful API for controlling and interacting with Atlas data  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FirmFilter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'parent_firm_id': 'int',
        'short_name': 'str',
        'relationship_code': 'str',
        'logo_url': 'str',
        'disclosures': 'str',
        'reporting_frequency': 'str',
        'report_on_heldaway_accounts': 'bool',
        'show_bridge_logo': 'bool',
        'show_firm_logo': 'bool',
        'cp_enabled': 'bool',
        'cp_web_reports_enabled': 'bool',
        'cp_printable_reports_enabled': 'bool',
        'cp_invoices_enabled': 'bool',
        'cp_shared_files_enabled': 'bool',
        'cp_heldaways_enabled': 'bool',
        'invoice_header': 'str',
        'invoice_footer': 'str',
        'invoice_from': 'str',
        'invoice_due_date_option': 'str',
        'invoice_include_fee_structures': 'bool',
        'invoice_effective_rates': 'bool',
        'invoice_annualized_effective_rates': 'bool',
        'invoice_show_agreement': 'bool',
        'invoice_not_a_bill_explanation': 'bool',
        'is_active': 'bool',
        'is_billing_active': 'bool',
        'billing_include_accrued_income': 'bool',
        'billing_partition_option': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_firm_id': 'parent_firm_id',
        'short_name': 'short_name',
        'relationship_code': 'relationship_code',
        'logo_url': 'logo_url',
        'disclosures': 'disclosures',
        'reporting_frequency': 'reporting_frequency',
        'report_on_heldaway_accounts': 'report_on_heldaway_accounts',
        'show_bridge_logo': 'show_bridge_logo',
        'show_firm_logo': 'show_firm_logo',
        'cp_enabled': 'cp_enabled',
        'cp_web_reports_enabled': 'cp_web_reports_enabled',
        'cp_printable_reports_enabled': 'cp_printable_reports_enabled',
        'cp_invoices_enabled': 'cp_invoices_enabled',
        'cp_shared_files_enabled': 'cp_shared_files_enabled',
        'cp_heldaways_enabled': 'cp_heldaways_enabled',
        'invoice_header': 'invoice_header',
        'invoice_footer': 'invoice_footer',
        'invoice_from': 'invoice_from',
        'invoice_due_date_option': 'invoice_due_date_option',
        'invoice_include_fee_structures': 'invoice_include_fee_structures',
        'invoice_effective_rates': 'invoice_effective_rates',
        'invoice_annualized_effective_rates': 'invoice_annualized_effective_rates',
        'invoice_show_agreement': 'invoice_show_agreement',
        'invoice_not_a_bill_explanation': 'invoice_not_a_bill_explanation',
        'is_active': 'is_active',
        'is_billing_active': 'is_billing_active',
        'billing_include_accrued_income': 'billing_include_accrued_income',
        'billing_partition_option': 'billing_partition_option'
    }

    def __init__(self, id=None, parent_firm_id=None, short_name=None, relationship_code=None, logo_url=None, disclosures=None, reporting_frequency=None, report_on_heldaway_accounts=None, show_bridge_logo=None, show_firm_logo=None, cp_enabled=None, cp_web_reports_enabled=None, cp_printable_reports_enabled=None, cp_invoices_enabled=None, cp_shared_files_enabled=None, cp_heldaways_enabled=None, invoice_header=None, invoice_footer=None, invoice_from=None, invoice_due_date_option=None, invoice_include_fee_structures=None, invoice_effective_rates=None, invoice_annualized_effective_rates=None, invoice_show_agreement=None, invoice_not_a_bill_explanation=None, is_active=None, is_billing_active=None, billing_include_accrued_income=None, billing_partition_option=None):  # noqa: E501
        """FirmFilter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._parent_firm_id = None
        self._short_name = None
        self._relationship_code = None
        self._logo_url = None
        self._disclosures = None
        self._reporting_frequency = None
        self._report_on_heldaway_accounts = None
        self._show_bridge_logo = None
        self._show_firm_logo = None
        self._cp_enabled = None
        self._cp_web_reports_enabled = None
        self._cp_printable_reports_enabled = None
        self._cp_invoices_enabled = None
        self._cp_shared_files_enabled = None
        self._cp_heldaways_enabled = None
        self._invoice_header = None
        self._invoice_footer = None
        self._invoice_from = None
        self._invoice_due_date_option = None
        self._invoice_include_fee_structures = None
        self._invoice_effective_rates = None
        self._invoice_annualized_effective_rates = None
        self._invoice_show_agreement = None
        self._invoice_not_a_bill_explanation = None
        self._is_active = None
        self._is_billing_active = None
        self._billing_include_accrued_income = None
        self._billing_partition_option = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if parent_firm_id is not None:
            self.parent_firm_id = parent_firm_id
        if short_name is not None:
            self.short_name = short_name
        if relationship_code is not None:
            self.relationship_code = relationship_code
        if logo_url is not None:
            self.logo_url = logo_url
        if disclosures is not None:
            self.disclosures = disclosures
        if reporting_frequency is not None:
            self.reporting_frequency = reporting_frequency
        if report_on_heldaway_accounts is not None:
            self.report_on_heldaway_accounts = report_on_heldaway_accounts
        if show_bridge_logo is not None:
            self.show_bridge_logo = show_bridge_logo
        if show_firm_logo is not None:
            self.show_firm_logo = show_firm_logo
        if cp_enabled is not None:
            self.cp_enabled = cp_enabled
        if cp_web_reports_enabled is not None:
            self.cp_web_reports_enabled = cp_web_reports_enabled
        if cp_printable_reports_enabled is not None:
            self.cp_printable_reports_enabled = cp_printable_reports_enabled
        if cp_invoices_enabled is not None:
            self.cp_invoices_enabled = cp_invoices_enabled
        if cp_shared_files_enabled is not None:
            self.cp_shared_files_enabled = cp_shared_files_enabled
        if cp_heldaways_enabled is not None:
            self.cp_heldaways_enabled = cp_heldaways_enabled
        if invoice_header is not None:
            self.invoice_header = invoice_header
        if invoice_footer is not None:
            self.invoice_footer = invoice_footer
        if invoice_from is not None:
            self.invoice_from = invoice_from
        if invoice_due_date_option is not None:
            self.invoice_due_date_option = invoice_due_date_option
        if invoice_include_fee_structures is not None:
            self.invoice_include_fee_structures = invoice_include_fee_structures
        if invoice_effective_rates is not None:
            self.invoice_effective_rates = invoice_effective_rates
        if invoice_annualized_effective_rates is not None:
            self.invoice_annualized_effective_rates = invoice_annualized_effective_rates
        if invoice_show_agreement is not None:
            self.invoice_show_agreement = invoice_show_agreement
        if invoice_not_a_bill_explanation is not None:
            self.invoice_not_a_bill_explanation = invoice_not_a_bill_explanation
        if is_active is not None:
            self.is_active = is_active
        if is_billing_active is not None:
            self.is_billing_active = is_billing_active
        if billing_include_accrued_income is not None:
            self.billing_include_accrued_income = billing_include_accrued_income
        if billing_partition_option is not None:
            self.billing_partition_option = billing_partition_option

    @property
    def id(self):
        """Gets the id of this FirmFilter.  # noqa: E501

        Unique ID for this firm object  # noqa: E501

        :return: The id of this FirmFilter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirmFilter.

        Unique ID for this firm object  # noqa: E501

        :param id: The id of this FirmFilter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_firm_id(self):
        """Gets the parent_firm_id of this FirmFilter.  # noqa: E501

        ID of the parent firm, if applicable  # noqa: E501

        :return: The parent_firm_id of this FirmFilter.  # noqa: E501
        :rtype: int
        """
        return self._parent_firm_id

    @parent_firm_id.setter
    def parent_firm_id(self, parent_firm_id):
        """Sets the parent_firm_id of this FirmFilter.

        ID of the parent firm, if applicable  # noqa: E501

        :param parent_firm_id: The parent_firm_id of this FirmFilter.  # noqa: E501
        :type: int
        """

        self._parent_firm_id = parent_firm_id

    @property
    def short_name(self):
        """Gets the short_name of this FirmFilter.  # noqa: E501

        The firm short name or \"SNAM\"  # noqa: E501

        :return: The short_name of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this FirmFilter.

        The firm short name or \"SNAM\"  # noqa: E501

        :param short_name: The short_name of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def relationship_code(self):
        """Gets the relationship_code of this FirmFilter.  # noqa: E501

        A system-generated code used for storage purposes  # noqa: E501

        :return: The relationship_code of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._relationship_code

    @relationship_code.setter
    def relationship_code(self, relationship_code):
        """Sets the relationship_code of this FirmFilter.

        A system-generated code used for storage purposes  # noqa: E501

        :param relationship_code: The relationship_code of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._relationship_code = relationship_code

    @property
    def logo_url(self):
        """Gets the logo_url of this FirmFilter.  # noqa: E501

        Public URL of the firm's logo  # noqa: E501

        :return: The logo_url of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this FirmFilter.

        Public URL of the firm's logo  # noqa: E501

        :param logo_url: The logo_url of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def disclosures(self):
        """Gets the disclosures of this FirmFilter.  # noqa: E501

        HTML-encoded disclosures intended for reporting  # noqa: E501

        :return: The disclosures of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._disclosures

    @disclosures.setter
    def disclosures(self, disclosures):
        """Sets the disclosures of this FirmFilter.

        HTML-encoded disclosures intended for reporting  # noqa: E501

        :param disclosures: The disclosures of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._disclosures = disclosures

    @property
    def reporting_frequency(self):
        """Gets the reporting_frequency of this FirmFilter.  # noqa: E501

        See Frequency Codes  # noqa: E501

        :return: The reporting_frequency of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._reporting_frequency

    @reporting_frequency.setter
    def reporting_frequency(self, reporting_frequency):
        """Sets the reporting_frequency of this FirmFilter.

        See Frequency Codes  # noqa: E501

        :param reporting_frequency: The reporting_frequency of this FirmFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["D = Daily", "W = Weekly", "M = Monthly", "Q = Quarterly", "Y = Yearly"]  # noqa: E501
        if reporting_frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `reporting_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(reporting_frequency, allowed_values)
            )

        self._reporting_frequency = reporting_frequency

    @property
    def report_on_heldaway_accounts(self):
        """Gets the report_on_heldaway_accounts of this FirmFilter.  # noqa: E501

        Option to include held-away assets in PDF reports  # noqa: E501

        :return: The report_on_heldaway_accounts of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._report_on_heldaway_accounts

    @report_on_heldaway_accounts.setter
    def report_on_heldaway_accounts(self, report_on_heldaway_accounts):
        """Sets the report_on_heldaway_accounts of this FirmFilter.

        Option to include held-away assets in PDF reports  # noqa: E501

        :param report_on_heldaway_accounts: The report_on_heldaway_accounts of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._report_on_heldaway_accounts = report_on_heldaway_accounts

    @property
    def show_bridge_logo(self):
        """Gets the show_bridge_logo of this FirmFilter.  # noqa: E501

        Show bridge logo?  # noqa: E501

        :return: The show_bridge_logo of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._show_bridge_logo

    @show_bridge_logo.setter
    def show_bridge_logo(self, show_bridge_logo):
        """Sets the show_bridge_logo of this FirmFilter.

        Show bridge logo?  # noqa: E501

        :param show_bridge_logo: The show_bridge_logo of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._show_bridge_logo = show_bridge_logo

    @property
    def show_firm_logo(self):
        """Gets the show_firm_logo of this FirmFilter.  # noqa: E501

        Show firm logo?  # noqa: E501

        :return: The show_firm_logo of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._show_firm_logo

    @show_firm_logo.setter
    def show_firm_logo(self, show_firm_logo):
        """Sets the show_firm_logo of this FirmFilter.

        Show firm logo?  # noqa: E501

        :param show_firm_logo: The show_firm_logo of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._show_firm_logo = show_firm_logo

    @property
    def cp_enabled(self):
        """Gets the cp_enabled of this FirmFilter.  # noqa: E501

        Is the client portal is enabled for the firm's customers?  # noqa: E501

        :return: The cp_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_enabled

    @cp_enabled.setter
    def cp_enabled(self, cp_enabled):
        """Sets the cp_enabled of this FirmFilter.

        Is the client portal is enabled for the firm's customers?  # noqa: E501

        :param cp_enabled: The cp_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_enabled = cp_enabled

    @property
    def cp_web_reports_enabled(self):
        """Gets the cp_web_reports_enabled of this FirmFilter.  # noqa: E501

        Can clients access their own web reports from the portal?  # noqa: E501

        :return: The cp_web_reports_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_web_reports_enabled

    @cp_web_reports_enabled.setter
    def cp_web_reports_enabled(self, cp_web_reports_enabled):
        """Sets the cp_web_reports_enabled of this FirmFilter.

        Can clients access their own web reports from the portal?  # noqa: E501

        :param cp_web_reports_enabled: The cp_web_reports_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_web_reports_enabled = cp_web_reports_enabled

    @property
    def cp_printable_reports_enabled(self):
        """Gets the cp_printable_reports_enabled of this FirmFilter.  # noqa: E501

        Can clients download printable reports?  # noqa: E501

        :return: The cp_printable_reports_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_printable_reports_enabled

    @cp_printable_reports_enabled.setter
    def cp_printable_reports_enabled(self, cp_printable_reports_enabled):
        """Sets the cp_printable_reports_enabled of this FirmFilter.

        Can clients download printable reports?  # noqa: E501

        :param cp_printable_reports_enabled: The cp_printable_reports_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_printable_reports_enabled = cp_printable_reports_enabled

    @property
    def cp_invoices_enabled(self):
        """Gets the cp_invoices_enabled of this FirmFilter.  # noqa: E501

        Can clients view their invoices?  # noqa: E501

        :return: The cp_invoices_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_invoices_enabled

    @cp_invoices_enabled.setter
    def cp_invoices_enabled(self, cp_invoices_enabled):
        """Sets the cp_invoices_enabled of this FirmFilter.

        Can clients view their invoices?  # noqa: E501

        :param cp_invoices_enabled: The cp_invoices_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_invoices_enabled = cp_invoices_enabled

    @property
    def cp_shared_files_enabled(self):
        """Gets the cp_shared_files_enabled of this FirmFilter.  # noqa: E501

        Can clients access shared files?  # noqa: E501

        :return: The cp_shared_files_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_shared_files_enabled

    @cp_shared_files_enabled.setter
    def cp_shared_files_enabled(self, cp_shared_files_enabled):
        """Sets the cp_shared_files_enabled of this FirmFilter.

        Can clients access shared files?  # noqa: E501

        :param cp_shared_files_enabled: The cp_shared_files_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_shared_files_enabled = cp_shared_files_enabled

    @property
    def cp_heldaways_enabled(self):
        """Gets the cp_heldaways_enabled of this FirmFilter.  # noqa: E501

        Can clients access and add heldaway assets?  # noqa: E501

        :return: The cp_heldaways_enabled of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._cp_heldaways_enabled

    @cp_heldaways_enabled.setter
    def cp_heldaways_enabled(self, cp_heldaways_enabled):
        """Sets the cp_heldaways_enabled of this FirmFilter.

        Can clients access and add heldaway assets?  # noqa: E501

        :param cp_heldaways_enabled: The cp_heldaways_enabled of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._cp_heldaways_enabled = cp_heldaways_enabled

    @property
    def invoice_header(self):
        """Gets the invoice_header of this FirmFilter.  # noqa: E501

        HTML invoice header  # noqa: E501

        :return: The invoice_header of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._invoice_header

    @invoice_header.setter
    def invoice_header(self, invoice_header):
        """Sets the invoice_header of this FirmFilter.

        HTML invoice header  # noqa: E501

        :param invoice_header: The invoice_header of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._invoice_header = invoice_header

    @property
    def invoice_footer(self):
        """Gets the invoice_footer of this FirmFilter.  # noqa: E501

        HTML invoice footer  # noqa: E501

        :return: The invoice_footer of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._invoice_footer

    @invoice_footer.setter
    def invoice_footer(self, invoice_footer):
        """Sets the invoice_footer of this FirmFilter.

        HTML invoice footer  # noqa: E501

        :param invoice_footer: The invoice_footer of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._invoice_footer = invoice_footer

    @property
    def invoice_from(self):
        """Gets the invoice_from of this FirmFilter.  # noqa: E501

        The address of the firm  # noqa: E501

        :return: The invoice_from of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._invoice_from

    @invoice_from.setter
    def invoice_from(self, invoice_from):
        """Sets the invoice_from of this FirmFilter.

        The address of the firm  # noqa: E501

        :param invoice_from: The invoice_from of this FirmFilter.  # noqa: E501
        :type: str
        """

        self._invoice_from = invoice_from

    @property
    def invoice_due_date_option(self):
        """Gets the invoice_due_date_option of this FirmFilter.  # noqa: E501

        Option to use for calculating due date. Choices are 30 (30 days from the invoice date), E (end of next month), or the empty string.  # noqa: E501

        :return: The invoice_due_date_option of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._invoice_due_date_option

    @invoice_due_date_option.setter
    def invoice_due_date_option(self, invoice_due_date_option):
        """Sets the invoice_due_date_option of this FirmFilter.

        Option to use for calculating due date. Choices are 30 (30 days from the invoice date), E (end of next month), or the empty string.  # noqa: E501

        :param invoice_due_date_option: The invoice_due_date_option of this FirmFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["30", "E"]  # noqa: E501
        if invoice_due_date_option not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_due_date_option` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_due_date_option, allowed_values)
            )

        self._invoice_due_date_option = invoice_due_date_option

    @property
    def invoice_include_fee_structures(self):
        """Gets the invoice_include_fee_structures of this FirmFilter.  # noqa: E501

        Whether to include a description of the fee structures used in the billing  # noqa: E501

        :return: The invoice_include_fee_structures of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_include_fee_structures

    @invoice_include_fee_structures.setter
    def invoice_include_fee_structures(self, invoice_include_fee_structures):
        """Sets the invoice_include_fee_structures of this FirmFilter.

        Whether to include a description of the fee structures used in the billing  # noqa: E501

        :param invoice_include_fee_structures: The invoice_include_fee_structures of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._invoice_include_fee_structures = invoice_include_fee_structures

    @property
    def invoice_effective_rates(self):
        """Gets the invoice_effective_rates of this FirmFilter.  # noqa: E501

        Whether to include effective rates (total billed divided by total assets) in the invoice  # noqa: E501

        :return: The invoice_effective_rates of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_effective_rates

    @invoice_effective_rates.setter
    def invoice_effective_rates(self, invoice_effective_rates):
        """Sets the invoice_effective_rates of this FirmFilter.

        Whether to include effective rates (total billed divided by total assets) in the invoice  # noqa: E501

        :param invoice_effective_rates: The invoice_effective_rates of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._invoice_effective_rates = invoice_effective_rates

    @property
    def invoice_annualized_effective_rates(self):
        """Gets the invoice_annualized_effective_rates of this FirmFilter.  # noqa: E501

        Whether to show the effective rate as an annual percentage  # noqa: E501

        :return: The invoice_annualized_effective_rates of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_annualized_effective_rates

    @invoice_annualized_effective_rates.setter
    def invoice_annualized_effective_rates(self, invoice_annualized_effective_rates):
        """Sets the invoice_annualized_effective_rates of this FirmFilter.

        Whether to show the effective rate as an annual percentage  # noqa: E501

        :param invoice_annualized_effective_rates: The invoice_annualized_effective_rates of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._invoice_annualized_effective_rates = invoice_annualized_effective_rates

    @property
    def invoice_show_agreement(self):
        """Gets the invoice_show_agreement of this FirmFilter.  # noqa: E501

        Whether to show the disclaimer agreement text, standard from V2 invoices  # noqa: E501

        :return: The invoice_show_agreement of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_show_agreement

    @invoice_show_agreement.setter
    def invoice_show_agreement(self, invoice_show_agreement):
        """Sets the invoice_show_agreement of this FirmFilter.

        Whether to show the disclaimer agreement text, standard from V2 invoices  # noqa: E501

        :param invoice_show_agreement: The invoice_show_agreement of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._invoice_show_agreement = invoice_show_agreement

    @property
    def invoice_not_a_bill_explanation(self):
        """Gets the invoice_not_a_bill_explanation of this FirmFilter.  # noqa: E501

        If true and the invoice doesn't represent a bill (because it'll be withdrawn directly)  # noqa: E501

        :return: The invoice_not_a_bill_explanation of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_not_a_bill_explanation

    @invoice_not_a_bill_explanation.setter
    def invoice_not_a_bill_explanation(self, invoice_not_a_bill_explanation):
        """Sets the invoice_not_a_bill_explanation of this FirmFilter.

        If true and the invoice doesn't represent a bill (because it'll be withdrawn directly)  # noqa: E501

        :param invoice_not_a_bill_explanation: The invoice_not_a_bill_explanation of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._invoice_not_a_bill_explanation = invoice_not_a_bill_explanation

    @property
    def is_active(self):
        """Gets the is_active of this FirmFilter.  # noqa: E501

        Is the firm active?  # noqa: E501

        :return: The is_active of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this FirmFilter.

        Is the firm active?  # noqa: E501

        :param is_active: The is_active of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_billing_active(self):
        """Gets the is_billing_active of this FirmFilter.  # noqa: E501

        Is the billing state active?  # noqa: E501

        :return: The is_billing_active of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_billing_active

    @is_billing_active.setter
    def is_billing_active(self, is_billing_active):
        """Sets the is_billing_active of this FirmFilter.

        Is the billing state active?  # noqa: E501

        :param is_billing_active: The is_billing_active of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._is_billing_active = is_billing_active

    @property
    def billing_include_accrued_income(self):
        """Gets the billing_include_accrued_income of this FirmFilter.  # noqa: E501

        Is accrued income included?  # noqa: E501

        :return: The billing_include_accrued_income of this FirmFilter.  # noqa: E501
        :rtype: bool
        """
        return self._billing_include_accrued_income

    @billing_include_accrued_income.setter
    def billing_include_accrued_income(self, billing_include_accrued_income):
        """Sets the billing_include_accrued_income of this FirmFilter.

        Is accrued income included?  # noqa: E501

        :param billing_include_accrued_income: The billing_include_accrued_income of this FirmFilter.  # noqa: E501
        :type: bool
        """

        self._billing_include_accrued_income = billing_include_accrued_income

    @property
    def billing_partition_option(self):
        """Gets the billing_partition_option of this FirmFilter.  # noqa: E501

        See Frequency Codes  # noqa: E501

        :return: The billing_partition_option of this FirmFilter.  # noqa: E501
        :rtype: str
        """
        return self._billing_partition_option

    @billing_partition_option.setter
    def billing_partition_option(self, billing_partition_option):
        """Sets the billing_partition_option of this FirmFilter.

        See Frequency Codes  # noqa: E501

        :param billing_partition_option: The billing_partition_option of this FirmFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["D = Daily", "W = Weekly", "M = Monthly", "Q = Quarterly", "Y = Yearly"]  # noqa: E501
        if billing_partition_option not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_partition_option` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_partition_option, allowed_values)
            )

        self._billing_partition_option = billing_partition_option

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FirmFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FirmFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other