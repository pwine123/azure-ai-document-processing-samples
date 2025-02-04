from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
import json

class TaxAddress(BaseModel):
    """
    A class representing an address in a tax document.
    Attributes:
    street: Street address
    city: City, e.g. Waterloo
    province: Province, e.g. ON
    postal_code: Postal code, e.g. N2T 2M5
    """
    street: Optional[str] = Field(
        description='Street address, e.g. 345 Test Street'
    )
    city: Optional[str] = Field(
        description='City, e.g. Waterloo'
    )
    province: Optional[str] = Field(
        description='Province, e.g. ON'
    )
    postal_code: Optional[str] = Field(
        description='Postal code, e.g. N2T 2M5'
    )

    @staticmethod
    def example():
        """
        Creates an empty example TaxAddress object.
        Returns:
        TaxAddress: An empty TaxAddress object.
        """
        return TaxAddress(
            street='',
            city='',
            province='',
            postal_code=''
        )

    def to_dict(self):
        """
        Converts the TaxAddress object to a dictionary.
        Returns:
        dict: The TaxAddress object as a dictionary.
        """
        return {
            'street': self.street,
            'city': self.city,
            'province': self.province,
            'postal_code': self.postal_code
        }

class TaxDocument(BaseModel):
    """
    A class representing a tax document.
    Attributes:
    first_name: First name of the person.
    last_name: Last name of the person.
    sin: Social Insurance Number (SIN) of the person.
    date_of_birth: Date of birth of the person.
    marital_status: Marital status of the person.
    language_of_correspondence: Language of correspondence.
    residence_province: Province of residence on December 31, 2023.
    current_province: Current province if different from mailing address.
    business_province: Province where business had a permanent establishment if self-employed in 2023.
    address: Mailing address of the person.
    spouse_first_name: First name of the spouse or common-law partner.
    spouse_sin: SIN of the spouse or common-law partner.
    spouse_net_income: Net income from line 23600 of their return to claim certain credits.
    """
    first_name: Optional[str] = Field(
        description='First name of the person, e.g. John'
    )
    last_name: Optional[str] = Field(
        description='Last name of the person, e.g. Doe'
    )
    sin: Optional[str] = Field(
        description='Social Insurance Number (SIN) of the person, e.g. 999555123'
    )
    date_of_birth: Optional[str] = Field(
        description='Date of birth of the person, e.g. 1977-10-05'
    )
    marital_status: Optional[str] = Field(
        description='Marital status on December 31, 2023, e.g. Single'
    )
    language_of_correspondence: Optional[str] = Field(
        description='Language of correspondence, e.g. English'
    )
    residence_province: Optional[str] = Field(
        description='Province of residence on December 31, 2023, e.g. Ontario'
    )
    current_province: Optional[str] = Field(
        description='Current province if different from mailing address, e.g. Ontario'
    )
    business_province: Optional[str] = Field(
        description='Province where business had a permanent establishment if self-employed in 2023, e.g. Ontario'
    )
    address: Optional[TaxAddress] = Field(
        description='Mailing address of the person'
    )
    spouse_first_name: Optional[str] = Field(
        description="First name of the spouse or common-law partner, e.g. Jane"
    )
    spouse_sin: Optional[str] = Field(
        description="SIN of the spouse or common-law partner, e.g. 999555124"
    )
    spouse_net_income: Optional[float] = Field(
        description="Net income from line 23600 of their return to claim certain credits, e.g. 150000.00"
    )

    @staticmethod
    def example():
        """
        Creates an empty example TaxDocument object.
        Returns:
        TaxDocument: An empty TaxDocument object.
        """
        return TaxDocument(
            first_name='',
            last_name='',
            sin='',
            date_of_birth='',
            marital_status='',
            language_of_correspondence='',
            residence_province='',
            current_province='',
            business_province='',
            address=TaxAddress.example(),
            spouse_first_name='',
            spouse_sin='',
            spouse_net_income=0.0
        )
    @staticmethod
    def from_json(json_str: str):
        """
        Creates an Invoice object from a JSON string.

        Args:
            json_str: The JSON string representing the Invoice object.

        Returns:
            Invoice: An Invoice object.
        """

        json_content = json.loads(json_str)

        def create_tax_address(address):
            """
            Creates an TaxAddress object from a dictionary.

            Args:
                address: A dictionary representing an TaxAddress object.

            Returns:
                InvoiceAddress: An TaxAddress object.
            """

            if address is None:
                return None

            return TaxAddress(
                street=address.get('street', None),
                city=address.get('city', None),
                province=address.get('province', None),
                postal_code=address.get('postal_code', None)
              
            )

        return TaxDocument(
            first_name=json_content.get('first_name', None),
            last_name=json_content.get('last_name', None),
            sin=json_content.get('sin', None),
            date_of_birth=json_content.get('date_of_birth', None),
            marital_status=json_content.get('marital_status', None),
            language_of_correspondence=json_content.get('language_of_correspondence', None),
            residence_province=json_content.get('residence_province', None),
            current_province=json_content.get('current_province', None),
            business_province=json_content.get('business_province', None),
            address=create_tax_address(json_content.get('address', None)),
            spouse_first_name=json_content.get('spouse_first_name', None),
            spouse_sin=json_content.get('spouse_sin', None),
            spouse_net_income=json_content.get('spouse_net_income', None)
        )    
    
    def to_dict(self):
        """
        Converts the TaxDocument object to a dictionary.
        Returns:
        dict: The TaxDocument object as a dictionary.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'sin': self.sin,
            'date_of_birth': self.date_of_birth,
            'marital_status': self.marital_status,
            'language_of_correspondence': self.language_of_correspondence,
            'residence_province': self.residence_province,
            'current_province': self.current_province,
            'business_province': self.business_province,
            'address': self.address.to_dict() if self.address else None,
            'spouse_first_name': self.spouse_first_name,
            'spouse_sin': self.spouse_sin,
            'spouse_net_income': self.spouse_net_income
        }
