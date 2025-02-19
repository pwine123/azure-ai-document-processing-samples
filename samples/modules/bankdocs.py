from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel, Field
import json

class DocumentDetails(BaseModel):
    company_name: Optional[str] = Field(description="Name of the company")
    program_name: Optional[str] = Field(description="Name of the program")
    report_date: Optional[str] = Field(description="Report date")
    location_address: Optional[str] = Field(description="Location address")
    city: Optional[str] = Field(description="City")
    state: Optional[str] = Field(description="State")
    zip_code: Optional[str] = Field(description="Zip code")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return DocumentDetails(**json.loads(json_str))

class AdvisorDetails(BaseModel):
    name: Optional[str] = Field(description="Name of the advisor")
    phone: Optional[str] = Field(description="Phone number of the advisor")
    resource_line: Optional[str] = Field(description="Resource line")
    website: Optional[str] = Field(description="Website")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return AdvisorDetails(**json.loads(json_str))

class AccountDetails(BaseModel):
    account_name: Optional[str] = Field(description="Name of the account")
    account_number: Optional[str] = Field(description="Account number")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return AccountDetails(**json.loads(json_str))

class AccountSummary(BaseModel):
    value_on_may_31: Optional[float] = Field(description="Value on May 31")
    value_on_june_30: Optional[float] = Field(description="Value on June 30")
    accrued_interest_may_31: Optional[float] = Field(description="Accrued interest on May 31")
    accrued_interest_june_30: Optional[float] = Field(description="Accrued interest on June 30")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return AccountSummary(**json.loads(json_str))

class AccountGrowth(BaseModel):
    value_at_year_end_2022: Optional[float] = Field(description="Value at year end 2022")
    net_deposits_withdrawals: Optional[float] = Field(description="Net deposits/withdrawals")
    dividend_interest_income: Optional[float] = Field(description="Dividend/interest income")
    change_in_accrued_interest: Optional[float] = Field(description="Change in accrued interest")
    change_in_market_value: Optional[float] = Field(description="Change in market value")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return AccountGrowth(**json.loads(json_str))

class BalanceSheetItem(BaseModel):
    value: Optional[float] = Field(description="Value of the item")
    percentage: Optional[float] = Field(description="Percentage of the item")

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return BalanceSheetItem(**json.loads(json_str))

class BalanceSheet(BaseModel):
    cash_and_money_balances: BalanceSheetItem
    cash_alternatives: BalanceSheetItem
    equities: BalanceSheetItem
    fixed_income: BalanceSheetItem
    non_traditional: BalanceSheetItem
    commodities: BalanceSheetItem
    other: BalanceSheetItem
    total_assets: BalanceSheetItem

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return BalanceSheet(**json.loads(json_str))

class IndexPerformance(BaseModel):
    index: str
    june_2023_change: float
    year_to_date_change: float

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return IndexPerformance(**json.loads(json_str))

class MarketPerformance(BaseModel):
    indices: List[IndexPerformance]

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return MarketPerformance(**json.loads(json_str))

class InterestRates(BaseModel):
    three_month_treasury_bills: float
    one_month_libor: float

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return InterestRates(**json.loads(json_str))

class AccountValueChanges(BaseModel):
    opening_value: float
    withdrawals_fees: float
    dividend_interest_income: float
    change_in_accrued_interest: float
    change_in_market_value: float
    closing_value: float

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return AccountValueChanges(**json.loads(json_str))

class DividendInterestIncome(BaseModel):
    taxable_dividends: float
    taxable_interest: float
    tax_exempt_interest: float
    tax_exempt_accrued_interest_paid: float
    tax_exempt_accrued_interest_received: float
    total: float

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return DividendInterestIncome(**json.loads(json_str))

class GainsLosses(BaseModel):
    short_term: float
    long_term: float
    total: float

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        return GainsLosses(**json.loads(json_str))

class RealizedGainsLosses(GainsLosses):
    pass

class UnrealizedGainsLosses(GainsLosses):
    pass

class FinancialReport(BaseModel):
    document_details: DocumentDetails
    advisor_details: AdvisorDetails
    account_details_list: List[AccountDetails]
    account_summary: AccountSummary
    account_growth: AccountGrowth
    balance_sheet: BalanceSheet
    market_performance: MarketPerformance
    interest_rates: InterestRates
    account_value_changes_june_2023: AccountValueChanges
    account_value_changes_year_to_date: AccountValueChanges
    dividend_interest_income_june_2023: DividendInterestIncome
    dividend_interest_income_year_to_date: DividendInterestIncome
    realized_gains_losses_june_2023: RealizedGainsLosses
    realized_gains_losses_year_to_date: RealizedGainsLosses
    unrealized_gains_losses_june_2023: UnrealizedGainsLosses

    def to_dict(self):
        return self.dict()

    @staticmethod
    def from_json(json_str: str):
        json_content = json.loads(json_str)
        return FinancialReport(
            document_details=DocumentDetails.from_json(json.dumps(json_content.get('document_details', {}))),
            advisor_details=AdvisorDetails.from_json(json.dumps(json_content.get('advisor_details', {}))),
            account_details_list=[AccountDetails.from_json(json.dumps(ad)) for ad in json_content.get('account_details_list', [])],
            account_summary=AccountSummary.from_json(json.dumps(json_content.get('account_summary', {}))),
            account_growth=AccountGrowth.from_json(json.dumps(json_content.get('account_growth', {}))),
            balance_sheet=BalanceSheet.from_json(json.dumps(json_content.get('balance_sheet', {}))),
            market_performance=MarketPerformance.from_json(json.dumps(json_content.get('market_performance', {}))),
            interest_rates=InterestRates.from_json(json.dumps(json_content.get('interest_rates', {}))),
            account_value_changes_june_2023=AccountValueChanges.from_json(json.dumps(json_content.get('account_value_changes_june_2023', {}))),
            account_value_changes_year_to_date=AccountValueChanges.from_json(json.dumps(json_content.get('account_value_changes_year_to_date', {}))),
            dividend_interest_income_june_2023=DividendInterestIncome.from_json(json.dumps(json_content.get('dividend_interest_income_june_2023', {}))),
            dividend_interest_income_year_to_date=DividendInterestIncome.from_json(json.dumps(json_content.get('dividend_interest_income_year_to_date', {}))),
            realized_gains_losses_june_2023=RealizedGainsLosses.from_json(json.dumps(json_content.get('realized_gains_losses_june_2023', {}))),
            realized_gains_losses_year_to_date=RealizedGainsLosses.from_json(json.dumps(json_content.get('realized_gains_losses_year_to_date', {}))),
            unrealized_gains_losses_june_2023=UnrealizedGainsLosses.from_json(json.dumps(json_content.get('unrealized_gains_losses_june_2023', {})))
        )